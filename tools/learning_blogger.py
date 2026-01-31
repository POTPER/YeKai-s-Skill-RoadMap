import os
import datetime
import re
from typing import List, Dict, Optional

class LearningBlogger:
    def __init__(self, project_root: str):
        self.project_root = project_root
        self.notes_dir = os.path.join(project_root, "Notes")
        self.skills_dir = os.path.join(project_root, "Skills")
        self.templates_dir = os.path.join(project_root, "templates")
        
        # Ensure directories exist
        os.makedirs(self.notes_dir, exist_ok=True)
        os.makedirs(self.skills_dir, exist_ok=True)

    def generate_blog(self, 
                      topic: str, 
                      context_summary: str,
                      context_detail: str,
                      dialogue_summary: List[Dict[str, str]], 
                      core_concepts: List[str], 
                      root_cause_analysis: str,
                      action_items: List[str],
                      open_question: str,
                      tags: List[str]) -> str:
        """
        Generates a blog post from learning dialogue.
        """
        
        # 1. Load Template
        template_path = os.path.join(self.templates_dir, "blog_template.md")
        if not os.path.exists(template_path):
            return f"Error: Template not found at {template_path}"
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # 2. Process Concepts (Generate Wiki Links)
        concept_links = []
        main_concept_link = "Unknown Concept"
        
        if core_concepts:
            # Handle the first concept as the main one
            main_concept_link = self._ensure_concept_link(core_concepts[0])
            # Process all concepts for metadata
            for concept in core_concepts:
                concept_links.append(self._ensure_concept_link(concept))

        # 3. Format Dialogue
        # In a real template engine like Jinja2 this would be easier, 
        # but for zero-dependency we do simple string replacement or manual loop construction
        dialogue_text = ""
        for turn in dialogue_summary:
            role_icon = "🤖 AI" if turn['role'] == 'ai' else "🙋 我"
            dialogue_text += f"### {role_icon}\n{turn['content']}\n\n"

        # 4. Fill Template (Simple Replace)
        # Note: A proper templating engine is recommended for production, 
        # but string replace works for this MVP.
        content = template_content
        
        content = content.replace("{{ topic }}", topic)
        content = content.replace("{{ date }}", datetime.datetime.now().strftime("%Y-%m-%d"))
        content = content.replace("{{ tags }}", ", ".join(tags))
        content = content.replace("{{ concepts_links }}", ", ".join(concept_links))
        
        content = content.replace("{{ context_summary }}", context_summary)
        content = content.replace("{{ context_detail }}", context_detail)
        
        # Hacky replacement for loop in template
        # We replace the entire loop block with generated text
        loop_pattern = re.compile(r"{% for turn in dialogue %}(.*?){% endfor %}", re.DOTALL)
        content = loop_pattern.sub(dialogue_text, content)
        
        content = content.replace("{{ main_concept_link }}", main_concept_link)
        content = content.replace("{{ root_cause_analysis }}", root_cause_analysis)
        
        # Action Items
        action_item_1 = action_items[0] if len(action_items) > 0 else "Review key concepts"
        action_item_2 = action_items[1] if len(action_items) > 1 else "Practice with code"
        content = content.replace("{{ action_item_1 }}", action_item_1)
        content = content.replace("{{ action_item_2 }}", action_item_2)
        
        content = content.replace("{{ open_question }}", open_question)

        # 5. Write File
        safe_topic = re.sub(r'[\\/*?:"<>|]', "", topic).replace(" ", "_")
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{date_str}_{safe_topic}.md"
        file_path = os.path.join(self.notes_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return file_path

    def _ensure_concept_link(self, concept_name: str) -> str:
        """
        Check if concept file exists, return WikiLink.
        If not exists, could optionally create a stub file (skipped for now).
        """
        # Search in Skills directory recursively (simplified to top level for MVP)
        # Ideally we should search recursively
        
        # Return format: [[ConceptName]]
        return f"[[{concept_name}]]"

# For manual testing
if __name__ == "__main__":
    blogger = LearningBlogger(os.getcwd())
    print("LearningBlogger initialized.")
