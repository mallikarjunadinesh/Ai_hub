from pathlib import Path

from component_generator import ComponentGenerator
from page_generator import PageGenerator


class DomainGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder) / "domains"

    def generate(self):
        """
        Generate one HTML page per domain.
        """

        self.output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        for domain in self.__collect_domains():
            self.__generate_domain_page(domain)

    def __generate_domain_page(self, domain):

        body = []

        body.append(
            ComponentGenerator.breadcrumb(
                [
                    ("Home", "../index.html"),
                    (domain["name"], "#")
                ]
            )
        )

        body.append(
            PageGenerator.hero(
                domain["name"],
                f"Browse AI capabilities available for the {domain['name']} domain."
            )
        )

        body.append(
            self.__build_section(
                title="🤖 Agents",
                resources=domain["agents"],
                icon="fa-solid fa-robot"
            )
        )

        body.append(
            self.__build_section(
                title="📝 Prompts",
                resources=domain["prompts"],
                icon="fa-solid fa-file-lines"
            )
        )

        body.append(
            self.__build_section(
                title="⚙ Skills",
                resources=domain["skills"],
                icon="fa-solid fa-screwdriver-wrench"
            )
        )

        html = PageGenerator.build(
            title=domain["name"],
            body="\n".join(body)
        )

        output_file = (
            self.output_folder /
            f"{domain['slug']}.html"
        )

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        print(f"Generated {output_file}")

    def __build_section(
        self,
        title,
        resources,
        icon
    ):

        if not resources:

            return PageGenerator.section(
                title,
                PageGenerator.empty_state(
                    "No resources available."
                )
            )

        cards = []

        for resource in resources:

            cards.append(
                ComponentGenerator.resource_card(
                    title=resource.name,
                    description=resource.description,
                    icon=icon,
                    link=f"../items/{resource.id}.html"
                )
            )

        return PageGenerator.section(
            title,
            PageGenerator.card_grid(
                "\n".join(cards)
            )
        )

    def __collect_domains(self):

        domains = {}

        def get_domain(category):

            category = category or "General"

            if category not in domains:

                domains[category] = {
                    "name": category,
                    "slug": (
                        category
                        .lower()
                        .replace(" ", "_")
                    ),
                    "agents": [],
                    "prompts": [],
                    "skills": []
                }

            return domains[category]

        for agent in self.repository.agents:

            get_domain(
                agent.category
            )["agents"].append(agent)

        for prompt in self.repository.prompts:

            get_domain(
                prompt.category
            )["prompts"].append(prompt)

        for skill in self.repository.skills:

            get_domain(
                skill.category
            )["skills"].append(skill)      
            
        return sorted(
            domains.values(),
            key=lambda domain: domain["name"].lower()
        )
