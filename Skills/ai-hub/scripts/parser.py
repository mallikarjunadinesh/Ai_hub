from pathlib import Path

from markdown_parser import MarkdownParser
from models import Agent, Prompt, Repository, Skill
from utils import IdGenerator


class RepositoryParser:
    """
    Scans the repository and builds the Repository model.
    """

    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

        self.repository = Repository()

        self.id_generator = IdGenerator()

    def scan(self):

        print("Scanning Agents...")
        self._scan_agents()

        print("Scanning Prompts...")
        self._scan_prompts()

        print("Scanning Skills...")
        self._scan_skills()

        return self.repository

    # ---------------------------------------------------------
    # AGENTS
    # ---------------------------------------------------------

    def _scan_agents(self):

        agents_folder = self.repo_root / "Agents"

        if not agents_folder.exists():
            print("Agents folder not found.")
            return

        for file in agents_folder.rglob("*.agent.md"):

            data = MarkdownParser.parse(str(file))

            agent = Agent(

                id=self.id_generator.next_id("AGT"),

                name=data.get("name", file.stem),

                description=data.get("description", ""),

                category=data.get("category", "General"),

                objective=MarkdownParser.get_section(
                    data,
                    "Objective"
                ),

                usage=MarkdownParser.get_section(
                    data,
                    "Usage"
                ),

                benefits=MarkdownParser.get_section(
                    data,
                    "Benefits"
                ),

                sections=data.get("sections", {}),

                tags=self._split_csv(
                    data.get("tags", "")
                ),

                path=str(
                    file.relative_to(self.repo_root)
                )
            )

            self.repository.agents.append(agent)

    # ---------------------------------------------------------
    # PROMPTS
    # ---------------------------------------------------------

    def _scan_prompts(self):

        prompts_folder = self.repo_root / "Prompts"

        if not prompts_folder.exists():
            print("Prompts folder not found.")
            return

        for file in prompts_folder.rglob("*.prompt.md"):

            data = MarkdownParser.parse(str(file))

            prompt = Prompt(

                id=self.id_generator.next_id("PRM"),

                name=data.get("name", file.stem),

                description=data.get("description", ""),

                category=data.get("category", "General"),

                objective=MarkdownParser.get_section(
                    data,
                    "Objective"
                ),

                usage=MarkdownParser.get_section(
                    data,
                    "Usage"
                ),

                benefits=MarkdownParser.get_section(
                    data,
                    "Benefits"
                ),

                argument_hint=data.get(
                    "argument-hint",
                    ""
                ),

                agent=data.get("agent"),

                tools=self._split_csv(
                    data.get("tools", "")
                ),

                sections=data.get("sections", {}),

                path=str(
                    file.relative_to(self.repo_root)
                )
            )

            self.repository.prompts.append(prompt)

    # ---------------------------------------------------------
    # SKILLS
    # ---------------------------------------------------------

    def _scan_skills(self):

        skills_folder = self.repo_root / "Skills"

        if not skills_folder.exists():
            print("Skills folder not found.")
            return

        for file in skills_folder.rglob("SKILL.md"):

            # Ignore AI HUB itself
            if file.parent.name.lower() == "ai-hub":
                continue

            data = MarkdownParser.parse(str(file))

            skill = Skill(

                id=self.id_generator.next_id("SKL"),

                name=data.get(
                    "name",
                    file.parent.name
                ),

                description=data.get(
                    "description",
                    ""
                ),

                category=data.get(
                    "category",
                    "General"
                ),

                objective=MarkdownParser.get_section(
                    data,
                    "Objective"
                ),

                usage=MarkdownParser.get_section(
                    data,
                    "Usage"
                ),

                benefits=MarkdownParser.get_section(
                    data,
                    "Benefits"
                ),

                argument_hint=data.get(
                    "argument-hint",
                    ""
                ),

                user_invocable=str(
                    data.get(
                        "user-invocable",
                        "false"
                    )
                ).lower() == "true",

                tags=self._split_csv(
                    data.get("tags", "")
                ),

                sections=data.get("sections", {}),

                path=str(
                    file.relative_to(self.repo_root)
                )
            )

            self.repository.skills.append(skill)

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @staticmethod
    def _split_csv(value: str):

        if not value:
            return []

        return [
            item.strip()
            for item in value.split(",")
            if item.strip()
        ]
