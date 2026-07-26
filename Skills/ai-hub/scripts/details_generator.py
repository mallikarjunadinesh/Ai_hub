from pathlib import Path

from component_generator import ComponentGenerator
from page_generator import PageGenerator


class DetailsGenerator:

    def __init__(self, repository, output_folder):
        self.repository = repository
        self.output_folder = Path(output_folder) / "items"

    def generate(self):

        self.output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        for agent in self.repository.agents:
            self.__generate_item_page(
                item=agent,
                item_type="Agent"
            )

        for prompt in self.repository.prompts:
            self.__generate_item_page(
                item=prompt,
                item_type="Prompt"
            )

        for skill in self.repository.skills:
            self.__generate_item_page(
                item=skill,
                item_type="Skill"
            )

    def __generate_item_page(
        self,
        item,
        item_type
    ):

        body = []

        body.append(
            ComponentGenerator.breadcrumb(
                [
                    ("Home", "../index.html"),
                    (
                        item.category or "General",
                        f"../domains/{self.__slug(item.category)}.html"
                    ),
                    (item.name, "#")
                ]
            )
        )

        body.append(
            PageGenerator.hero(
                item.name,
                item.description
                or "No description available."
            )
        )

        body.append(
            self.__overview_section(
                item,
                item_type
            )
        )

        body.append(
            self.__section(
                "Objective",
                getattr(
                    item,
                    "objective",
                    ""
                )
            )
        )

        body.append(
            self.__section(
                "Usage",
                getattr(
                    item,
                    "usage",
                    ""
                )
            )
        )

        body.append(
            self.__section(
                "Benefits",
                getattr(
                    item,
                    "benefits",
                    ""
                )
            )
        )
              body.append(
            self.__tags_section(item)
        )

        body.append(
            self.__relationships(item)
        )

        body.append(
            self.__markdown_button(item)
        )

        html = PageGenerator.build(
            item.name,
            "\n".join(body)
        )

        output_file = (
            self.output_folder /
            f"{item.id}.html"
        )

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        print(f"Generated {output_file}")

    def __overview_section(
        self,
        item,
        item_type
    ):

        html = []

        html.append('<div class="domain-grid">')

        html.append(
            ComponentGenerator.stat_card(
                "Type",
                item_type
            )
        )

        html.append(
            ComponentGenerator.stat_card(
                "Category",
                item.category or "General"
            )
        )

        html.append(
            ComponentGenerator.stat_card(
                "Tags",
                len(getattr(item, "tags", []))
            )
        )

        html.append("</div>")

        return PageGenerator.section(
            "Overview",
            "\n".join(html)
        )

    def __section(
        self,
        title,
        value
    ):

        value = value or "Not Available"

        return PageGenerator.section(
            title,
            f"<p>{value}</p>"
        )
          def __tags_section(self, item):

        tags = getattr(item, "tags", [])

        if not tags:
            return PageGenerator.section(
                "Tags",
                "<p>No tags available.</p>"
            )

        html = []

        for tag in tags:
            html.append(
                f'<span class="tag">{tag}</span>'
            )

        return PageGenerator.section(
            "Tags",
            "\n".join(html)
        )

    def __relationships(self, item):

        html = []

        relationships = [
            (
                "Related Agents",
                getattr(item, "related_agents", [])
            ),
            (
                "Related Prompts",
                getattr(item, "related_prompts", [])
            ),
            (
                "Related Skills",
                getattr(item, "related_skills", [])
            )
        ]

        for title, resources in relationships:

            cards = []

            if resources:

                for resource in resources:

                    cards.append(
                        ComponentGenerator.resource_card(
                            title=resource.name,
                            description=resource.description,
                            icon="fa-solid fa-link",
                            link=f"{resource.id}.html"
                        )
                    )

                html.append(
                    PageGenerator.section(
                        title,
                        PageGenerator.card_grid(
                            "\n".join(cards)
                        )
                    )
                )

        if not html:

            return PageGenerator.section(
                "Relationships",
                "<p>No related resources.</p>"
            )

        return "\n".join(html)

    def __markdown_button(self, item):

        if not getattr(item, "path", None):
            return ""

        return PageGenerator.section(
            "Documentation",
            f"""
<a class="domain-card"
href="../{item.path}"
target="_blank">

Open Original Markdown

</a>
"""
        )
          def __slug(self, value):

        if not value:
            return "general"

        return (
            value
            .lower()
            .replace("&", "and")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(" ", "_")
        )
      
      
