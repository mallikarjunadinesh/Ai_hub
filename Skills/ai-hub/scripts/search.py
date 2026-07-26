import json
from pathlib import Path


class SearchIndexGenerator:
    """
    Builds a lightweight search index for AI HUB.
    """

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder)

    def generate(self):

        self.output_folder.mkdir(parents=True, exist_ok=True)

        index = []

        # -------------------------
        # Agents
        # -------------------------

        for agent in self.repository.agents:

            index.append({
                "id": agent.id,
                "type": "Agent",
                "name": agent.name,
                "description": agent.description,
                "category": agent.category,
                "path": agent.path
            })

        # -------------------------
        # Prompts
        # -------------------------

        for prompt in self.repository.prompts:

            index.append({
                "id": prompt.id,
                "type": "Prompt",
                "name": prompt.name,
                "description": prompt.description,
                "category": prompt.category,
                "path": prompt.path
            })

        # -------------------------
        # Skills
        # -------------------------

        for skill in self.repository.skills:

            index.append({
                "id": skill.id,
                "type": "Skill",
                "name": skill.name,
                "description": skill.description,
                "category": skill.category,
                "path": skill.path
            })

        output_file = self.output_folder / "search_index.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=4, ensure_ascii=False)

        print("Search index generated.")
