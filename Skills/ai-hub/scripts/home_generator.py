from pathlib import Path

from component_generator import ComponentGenerator


class HomeGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder)

    def generate(self):

        html = []

        html.append(ComponentGenerator.page_header("AI HUB"))

        html.append("""
<section class="hero">

<h1>AI HUB</h1>

<p>
Discover AI Agents, Prompts and Skills across enterprise domains.
</p>

</section>
""")

        html.append(ComponentGenerator.search_bar())

        html.append("""
<section class="section">

<h2>Browse by Domain</h2>

<div class="domain-grid">
""")

        domains = self.__get_domains()

        for domain in domains:

            html.append(
                ComponentGenerator.domain_card(
                    name=domain["name"],
                    agents=domain["agents"],
                    prompts=domain["prompts"],
                    skills=domain["skills"],
                    link=f"domains/{domain['slug']}.html"
                )
            )

        html.append("""
</div>

</section>
""")

        html.append(ComponentGenerator.page_footer())

        self.output_folder.mkdir(parents=True, exist_ok=True)

        output_file = self.output_folder / "index.html"

        output_file.write_text(
            "\n".join(html),
            encoding="utf-8"
        )

        print(f"Generated {output_file}")

    def __get_domains(self):

        domains = {}

        for agent in self.repository.agents:

            category = agent.category or "General"

            domains.setdefault(category, {
                "name": category,
                "slug": category.lower().replace(" ", "_"),
                "agents": 0,
                "prompts": 0,
                "skills": 0
            })

            domains[category]["agents"] += 1

        for prompt in self.repository.prompts:

            category = prompt.category or "General"

            domains.setdefault(category, {
                "name": category,
                "slug": category.lower().replace(" ", "_"),
                "agents": 0,
                "prompts": 0,
                "skills": 0
            })

            domains[category]["prompts"] += 1

        for skill in self.repository.skills:

            category = skill.category or "General"

            domains.setdefault(category, {
                "name": category,
                "slug": category.lower().replace(" ", "_"),
                "agents": 0,
                "prompts": 0,
                "skills": 0
            })

            domains[category]["skills"] += 1

        return sorted(
            domains.values(),
            key=lambda x: x["name"]
        )
