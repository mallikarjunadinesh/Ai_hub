from pathlib import Path

from models import Agent, Prompt, Skill, Repository
from markdown_parser import MarkdownParser
from utils import IdGenerator


class RepositoryParser:
    """
    Scans the repository and discovers Agents, Prompts and Skills.
    """

    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.repository = Repository()
        self.id_generator = IdGenerator()

    def scan(self):
        self._scan_agents()
        self._scan_prompts()
        self._scan_skills()

        return self.repository

    def _scan_agents(self):
        agents_folder = self.repo_root / "Agents"

        if not agents_folder.exists():
            return

        for file in agents_folder.rglob("*.agent.md"):
            data = MarkdownParser.parse(str(file))

            agent = Agent(
                id=self.id_generator.next_id("AGT"),
                name=data.get("name", file.stem),
                description=data.get("description", ""),
                objective=MarkdownParser.extract_section(
                    data["body"], "Objective"
                ),
                path=str(file.relative_to(self.repo_root)),
            )

            self.repository.agents.append(agent)

    def _scan_prompts(self):
        prompts_folder = self.repo_root / "Prompts"

        if not prompts_folder.exists():
            return

        for file in prompts_folder.rglob("*.prompt.md"):
            data = MarkdownParser.parse(str(file))

            prompt = Prompt(
                id=self.id_generator.next_id("PRM"),
                name=data.get("name", file.stem),
                description=data.get("description", ""),
                argument_hint=data.get("argument-hint", ""),
                agent=data.get("agent"),
                path=str(file.relative_to(self.repo_root)),
            )

            self.repository.prompts.append(prompt)

    def _scan_skills(self):
        skills_folder = self.repo_root / "Skills"

        if not skills_folder.exists():
            return

        for file in skills_folder.rglob("SKILL.md"):
            data = MarkdownParser.parse(str(file))

            skill = Skill(
                id=self.id_generator.next_id("SKL"),
                name=data.get("name", file.parent.name),
                description=data.get("description", ""),
                argument_hint=data.get("argument-hint", ""),
                user_invocable=str(
                    data.get("user-invocable", "false")
                ).lower() == "true",
                path=str(file.relative_to(self.repo_root)),
            )

            self.repository.skills.append(skill)
