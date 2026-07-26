from pathlib import Path

from component_generator import ComponentGenerator
from page_generator import PageGenerator


class DetailsGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder)

    def generate(self):

        items_folder = self.output_folder / "items"
        items_folder.mkdir(parents=True, exist_ok=True)

        resources = (
            self.repository.agents
            + self.repository.prompts
            + self.repository.skills
        )

        for resource in resources:
            self.__generate_item_page(resource, items_folder)

        print(f"Generated {len(resources)} detail pages.")

    def __generate_item_page(self, item, output_folder):

        body = []

        body.append(
            ComponentGenerator.breadcrumb(
                [
                    ("Home", "../index.html"),
                    (
                        item.category,
                        f"../domains/{self.__slug(item.category)}.html",
                    ),
                    (item.name, None),
                ]
            )
        )

        body.append(
            f"""
            <section class="hero">
                <h1>{item.name}</h1>
                <p>{item.description}</p>
            </section>
            """
        )

        body.append(self.__overview_section(item))

        body.append(
            self.__section(
                "Objective",
                item.sections.get("Objective", "")
            )
        )

        body.append(
            self.__section(
                "Usage",
                item.sections.get("Usage", "")
            )
        )

        body.append(
            self.__section(
                "Benefits",
                item.sections.get("Benefits", "")
            )
        )
        body.append(self.__tags_section(item))

        body.append(self.__relationships(item))

        body.append(self.__markdown_button(item))

        html = PageGenerator.build(
            title=item.name,
            body="\n".join(body),
            asset_prefix="../",
        )

        output_file = output_folder / f"{item.id}.html"

        output_file.write_text(
            html,
            encoding="utf-8"
        )

    def __overview_section(self, item):

        return f"""
        <section class="section">
            <h2>Overview</h2>

            <div class="stats-grid">

                <div class="stat-card">
                    <strong>Type</strong>
                    <p>{item.__class__.__name__}</p>
                </div>

                <div class="stat-card">
                    <strong>Category</strong>
                    <p>{item.category}</p>
                </div>

            </div>

        </section>
        """

    def __section(self, title, content):

        if not content:
            return ""

        return ComponentGenerator.section(
            title,
            f"<p>{content}</p>"
        )

    def __tags_section(self, item):

        tags = getattr(item, "tags", [])

        if not tags:
            return ""

        html = ""

        for tag in tags:
            html += f'<span class="tag">{tag}</span>'

        return ComponentGenerator.section(
            "Tags",
            html
        )
    def __relationships(self, item):

        html = ""

        relationships = [
            ("Related Agents", getattr(item, "related_agents", [])),
            ("Related Prompts", getattr(item, "related_prompts", [])),
            ("Related Skills", getattr(item, "related_skills", [])),
        ]

        for title, resources in relationships:

            if not resources:
                continue

            html += f"<h3>{title}</h3>"
            html += '<div class="card-grid">'

            for resource in resources:
                html += ComponentGenerator.resource_card(
                    resource,
                    f"{resource.id}.html"
                )

            html += "</div>"

        if not html:
            return ""

        return ComponentGenerator.section(
            "Related Resources",
            html
        )

    def __markdown_button(self, item):

        if not getattr(item, "path", None):
            return ""

        return f"""
        <section class="section">
            <a class="button"
               href="../{item.path}"
               target="_blank">
                Open Original Documentation
            </a>
        </section>
        """

    def __slug(self, text):

        return (
            text.lower()
                .replace(" ", "-")
                .replace("/", "-")
        )
