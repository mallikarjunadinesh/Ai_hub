import json
from dataclasses import asdict
from pathlib import Path


class JsonGenerator:
    """
    Generates the repository.json file used by AI HUB.
    """

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder)

    def generate(self):

        self.output_folder.mkdir(parents=True, exist_ok=True)

        output_file = self.output_folder / "repository.json"

        data = {
            "agents": [
                asdict(agent)
                for agent in self.repository.agents
            ],
            "prompts": [
                asdict(prompt)
                for prompt in self.repository.prompts
            ],
            "skills": [
                asdict(skill)
                for skill in self.repository.skills
            ]
        }

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Repository JSON generated: {output_file}")
