from pathlib import Path

from component_generator import ComponentGenerator
from page_generator import PageGenerator


class HomeGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder)

    def generate(self):

        body = []

        body.append(
            PageGenerator.hero(
                "AI HUB",
                "Discover AI Agents, Prompts and Skills across enterprise domains."
            )
        )

        body.append(ComponentGenerator.search_bar())

        cards = []

        for domain in self.__get_domains():

            cards.append(
                ComponentGenerator.domain_card(
                    name=domain["name"],
                    agents=domain["agents"],
                    prompts=domain["prompts"],
                    skills=domain["skills"],
                    link=f"domains/{domain['slug']}.html"
                )
            )

        body.append(
            PageGenerator.section(
                "Browse by Domain",
                PageGenerator.card_grid("\n".join(cards))
            )
        )

        html = PageGenerator.build(
            "AI HUB",
            "\n".join(body)
        )

        self.output_folder.mkdir(parents=True, exist_ok=True)

        output_file = self.output_folder / "index.html"

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        print(f"Generated {output_file}")

    def __get_domains(self):

        domains = {}

        def get_domain(category):

            category = category or "General"

            if category not in domains:

                domains[category] = {
                    "name": category,
                    "slug": category.lower().replace(" ", "_"),
                    "agents": 0,
                    "prompts": 0,
                    "skills": 0
                }

            return domains[category]

        for agent in self.repository.agents:
            get_domain(agent.category)["agents"] += 1

        for prompt in self.repository.prompts:
            get_domain(prompt.category)["prompts"] += 1

        for skill in self.repository.skills:
            get_domain(skill.category)["skills"] += 1

        return sorted(
            domains.values(),
            key=lambda x: x["name"]
        )
