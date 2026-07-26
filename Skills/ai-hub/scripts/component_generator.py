from html import escape


class ComponentGenerator:

    @staticmethod
    def page_header(title="AI HUB"):
        return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{escape(title)}</title>

<link rel="stylesheet" href="assets/css/style.css">

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">

</head>

<body>

<header class="top-header">

    <div class="logo">

        <i class="fa-solid fa-robot"></i>

        <span>AI HUB</span>

    </div>

    <nav>

        <a href="index.html">Home</a>

    </nav>

</header>

<main>
"""

    @staticmethod
    def page_footer():
        return """
</main>

<footer class="footer">

    AI HUB © 2026

</footer>

</body>

</html>
"""

    @staticmethod
    def search_bar():

        return """
<div class="search-container">

    <input
        id="globalSearch"
        type="text"
        placeholder="Search Agents, Prompts, Skills...">

</div>
"""

    @staticmethod
    def domain_card(name,
                    agents,
                    prompts,
                    skills,
                    link):

        return f"""
<a class="domain-card" href="{escape(link)}">

    <h2>{escape(name)}</h2>

    <div class="domain-stats">

        <div>

            <i class="fa-solid fa-robot"></i>

            <span>{agents} Agents</span>

        </div>

        <div>

            <i class="fa-solid fa-file-lines"></i>

            <span>{prompts} Prompts</span>

        </div>

        <div>

            <i class="fa-solid fa-screwdriver-wrench"></i>

            <span>{skills} Skills</span>

        </div>

    </div>

</a>
"""

    @staticmethod
    def section(title, body):

        return f"""
<section class="section">

<h2>{escape(title)}</h2>

{body}

</section>
"""

    @staticmethod
    def stat_card(title, value):

        return f"""
<div class="stat-card">

<h3>{escape(title)}</h3>

<p>{value}</p>

</div>
"""
