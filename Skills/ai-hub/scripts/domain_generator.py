from pathlib import Path

from component_generator import ComponentGenerator


class DomainGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder) / "domains"

    def generate(self):

        self.output_folder.mkdir(parents=True, exist_ok=True)

        for domain in self.__get_domains():
            self.__generate_domain_page(domain)

    def __generate_domain_page(self, domain):

        html = []

        html.append(ComponentGenerator.page_header(domain["name"]))

        html.append(f"""
<section class="hero">

<h1>{domain['name']}</h1>

<p>
Explore AI resources available for this domain.
</p>

</section>
""")

        # ---------- Agents ----------
        html.append("<section class='section'>")
        html.append("<h2>🤖 Agents</h2>")

        if domain["agents"]:
            for agent in domain["agents"]:
                html.append(f"""
<div class="domain-card">

<h3>{agent.name}</h3>

<p>{agent.description}</p>

</div>
""")
        else:
            html.append("<p>No agents available.</p>")

        html.append("</section>")

        # ---------- Prompts ----------
        html.append("<section class='section'>")
        html.append("<h2>📝 Prompts</h2>")

        if domain["prompts"]:
            for prompt in domain["prompts"]:
                html.append(f"""
<div class="domain-card">

<h3>{prompt.name}</h3>

<p>{prompt.description}</p>

</div>
""")
        else:
            html.append("<p>No prompts available.</p>")

        html.append("</section>")

        # ---------- Skills ----------
        html.append("<section class='section'>")
        html.append("<h2>⚙ Skills</h2>")

        if domain["skills"]:
            for skill in domain["skills"]:
                html.append(f"""
<div class="domain-card">

<h3>{skill.name}</h3>

<p>{skill.description}</p>

</div>
""")
        else:
            html.append("<p>No skills available.</p>")

        html.append("</section>")

        html.append(ComponentGenerator.page_footer())

        file_name = (
            domain["name"]
            .lower()
            .replace(" ", "_")
            + ".html"
        )

        output_file = self.output_folder / file_name

        output_file.write_text(
            "\n".join(html),
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
            key=lambda x: x["name"]
        )
