const http = require('http');
const { URL } = require('url');

function sendJson(res, statusCode, data) {
  const body = JSON.stringify(data);

  res.writeHead(statusCode, {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': Buffer.byteLength(body),
  });
  res.end(body);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url ?? '/', `http://${req.headers.host ?? 'localhost'}`);

  if (req.method === 'GET' && url.pathname === '/health') {
    return sendJson(res, 200, { ok: true });
  }

  if (req.method === 'GET' && url.pathname === '/hello') {
    const name = url.searchParams.get('name') || 'world';
    return sendJson(res, 200, { msg: `Hello, ${name}` });
  }

  return sendJson(res, 404, { error: 'Not Found' });
});

const host = process.env.HOST || '127.0.0.1';
let port = Number(process.env.PORT) || 3000;
let usedRandomPortFallback = false;

function startListening() {
  server.listen(port, host);
}

server.on('listening', () => {
  const addr = server.address();
  const actualPort = typeof addr === 'object' && addr ? addr.port : port;
  process.stdout.write(`Server running at http://${host}:${actualPort}\n`);
});

server.on('error', (err) => {
  if (err && (err.code === 'EACCES' || err.code === 'EADDRINUSE') && !usedRandomPortFallback) {
    usedRandomPortFallback = true;
    port = 0;
    startListening();
    return;
  }

  throw err;
});

startListening();
