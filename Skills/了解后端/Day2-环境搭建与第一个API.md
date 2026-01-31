# Day2：环境搭建与第一个 API（A/B 两条路线）

## 1. 今天的目标
- 跑起来一个本地后端服务（能在浏览器访问到 JSON）
- 理解：路由（Route）= URL + 方法 → 对应一段后端处理函数
- 学会最基本的“启动服务 → 访问接口 → 看返回值”闭环

---

## 2. 你先告诉我（用于选择 A 或 B）
请在终端执行并把输出粘贴给我：

### A 路线（Node.js）
- `node -v`
- `npm -v`

### B 路线（Python）
- `python --version`（或 `py --version`）
- `pip --version`

---

## 3. A 路线：Node.js + Express（上手快）

### 3.1 创建项目
在一个你方便的位置新建文件夹（比如 `backend-day2-node`），然后在终端进入该目录后运行：

- `npm init -y`
- `npm i express`

### 3.2 新建 `index.js`
代码目标：启动一个服务器并提供 2 个接口：
- `GET /health` → 返回 `{ "ok": true }`
- `GET /hello?name=Kai` → 返回 `{ "msg": "Hello, Kai" }`

### 3.3 启动服务
- `node index.js`

然后用浏览器打开：
- `http://localhost:3000/health`
- `http://localhost:3000/hello?name=Kai`

---

## 4. B 路线：Python + FastAPI（语法简洁）

### 4.1 创建虚拟环境（推荐）
在一个你方便的位置新建文件夹（比如 `backend-day2-py`），然后运行：

- `python -m venv .venv`（Windows 可能用 `py -m venv .venv`）
- 激活虚拟环境（PowerShell 一般是）：`.\.venv\Scripts\Activate.ps1`

### 4.2 安装依赖
- `pip install fastapi uvicorn`

### 4.3 新建 `main.py`
代码目标：启动一个服务器并提供 2 个接口：
- `GET /health` → 返回 `{ "ok": true }`
- `GET /hello?name=Kai` → 返回 `{ "msg": "Hello, Kai" }`

### 4.4 启动服务
- `uvicorn main:app --reload --port 8000`

然后用浏览器打开：
- `http://localhost:8000/health`
- `http://localhost:8000/hello?name=Kai`

---

## 5. 今日验收标准（你做到这 3 条就算 Day2 过关）
1. 你能启动服务并在浏览器看到 JSON 返回
2. 你能解释“路由是什么”（URL + 方法 对应一段代码）
3. 你能改一下返回内容（例如把 `Kai` 换成你的名字）
