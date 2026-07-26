from pathlib import Path

from component_generator import ComponentGenerator
from page_generator import PageGenerator


class DomainGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder) / "domains"

    def generate(self):

        self.output_folder.mkdir(parents=True, exist_ok=True)

        for domain in self.__get_domains():
            self.__generate_page(domain)

    def __generate_page(self, domain):

        body = []

        body.append(
            ComponentGenerator.breadcrumb([
                ("Home", "../index.html"),
                (domain["name"], "#")
            ])
        )

        body.append(
            PageGenerator.hero(
                domain["name"],
                f"Explore all AI resources available under the {domain['name']} domain."
            )
        )

        body.append(
            self.__resource_section(
                "🤖 Agents",
                domain["agents"],
                "fa-solid fa-robot",
                "../details/agents"
            )
        )

        body.append(
            self.__resource_section(
                "📝 Prompts",
                domain["prompts"],
                "fa-solid fa-file-lines",
                "../details/prompts"
            )
        )

        body.append(
            self.__resource_section(
                "⚙ Skills",
                domain["skills"],
                "fa-solid fa-screwdriver-wrench",
                "../details/skills"
            )
        )

        html = PageGenerator.build(
            domain["name"],
            "\n".join(body)
        )

        file_name = (
            domain["name"]
            .lower()
            .replace(" ", "_")
            + ".html"
        )

        output_file = self.output_folder / file_name

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        print(f"Generated {output_file}")

    def __resource_section(
        self,
        title,
        resources,
        icon,
        folder
    ):

        if not resources:
            return PageGenerator.section(
                title,
                PageGenerator.empty_state("Nothing found.")
            )

        cards = []

        for item in resources:

            cards.append(
                ComponentGenerator.resource_card(
                    title=item.name,
                    description=item.description,
                    icon=icon,
                    link=f"{folder}/{item.id}.html"
                )
            )

        return PageGenerator.section(
            title,
            PageGenerator.card_grid(
                "\n".join(cards)
            )
        )

    def __get_domains(self):

        domains = {}

        def get_domain(category):

            category = category or "General"

            if category not in domains:

                domains[category] = {
                    "name": category,
                    "agents": [],
                    "prompts": [],
                    "skills": []
                }

            return domains[category]

        for agent in self.repository.agents:
            get_domain(agent.category)["agents"].append(agent)

        for prompt in self.repository.prompts:
            get_domain(prompt.category)["prompts"].append(prompt)

        for skill in self.repository.skills:
            get_domain(skill.category)["skills"].append(skill)

        return sorted(
            domains.values(),
            key=lambda d: d["name"]
        )
