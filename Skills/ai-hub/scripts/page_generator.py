from component_generator import ComponentGenerator


class PageGenerator:
    """
    Generates a complete HTML page by wrapping page-specific
    content with the common header and footer.
    """

    @staticmethod
    def build(title: str, body: str) -> str:
        html = []

        html.append(ComponentGenerator.page_header(title))
        html.append(body)
        html.append(ComponentGenerator.page_footer())

        return "\n".join(html)

    @staticmethod
    def hero(title: str, description: str) -> str:
        return f"""
<section class="hero">

    <h1>{title}</h1>

    <p>{description}</p>

</section>
"""

    @staticmethod
    def section(title: str, content: str) -> str:
        return f"""
<section class="section">

    <h2>{title}</h2>

    {content}

</section>
"""

    @staticmethod
    def empty_state(message: str) -> str:
        return f"""
<div class="empty-state">

    <p>{message}</p>

</div>
"""

    @staticmethod
    def two_column(left: str, right: str) -> str:
        return f"""
<div class="two-column">

    <div>

        {left}

    </div>

    <div>

        {right}

    </div>

</div>
"""

    @staticmethod
    def card_grid(cards: str) -> str:
        return f"""
<div class="domain-grid">

{cards}

</div>
"""
