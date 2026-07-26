import re
from typing import Dict


class MarkdownParser:
    """
    Parses markdown files containing YAML front matter and markdown sections.
    """

    @staticmethod
    def parse(file_path: str) -> Dict:
        """
        Parse a markdown file and return its metadata, body and sections.
        """

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        metadata = {}
        body = content

        # ----------------------------
        # Parse YAML Front Matter
        # ----------------------------
        if content.startswith("---"):
            parts = content.split("---", 2)

            if len(parts) >= 3:
                yaml_text = parts[1]
                body = parts[2].strip()

                for line in yaml_text.splitlines():

                    line = line.strip()

                    if not line or ":" not in line:
                        continue

                    key, value = line.split(":", 1)

                    metadata[key.strip()] = value.strip()

        metadata["body"] = body
        metadata["sections"] = MarkdownParser.extract_sections(body)

        return metadata

    @staticmethod
    def extract_sections(body: str) -> Dict[str, str]:
        """
        Extract all ## Heading sections.

        Returns:

        {
            "Objective": "...",
            "Usage": "...",
            "Benefits": "...",
            "Output": "...",
            "Notes": "...",
            "Security": "..."
        }
        """

        sections = {}

        pattern = r"^##\s+(.*?)\n(.*?)(?=^##\s+|\Z)"

        matches = re.finditer(
            pattern,
            body,
            flags=re.MULTILINE | re.DOTALL
        )

        for match in matches:

            title = match.group(1).strip()

            content = match.group(2).strip()

            sections[title] = content

        return sections

    @staticmethod
    def get_section(data: Dict, section_name: str) -> str:
        """
        Safely return a section by name.
        """

        return data.get("sections", {}).get(section_name, "")
