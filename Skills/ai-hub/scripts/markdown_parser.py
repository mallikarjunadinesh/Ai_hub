import re
from typing import Dict


class MarkdownParser:
    """
    Parses markdown files with YAML front matter.
    """

    @staticmethod
    def parse(file_path: str) -> Dict:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        metadata = {}
        body = content

        # Parse YAML front matter
        if content.startswith("---"):
            parts = content.split("---", 2)

            if len(parts) >= 3:
                yaml_text = parts[1]
                body = parts[2].strip()

                for line in yaml_text.splitlines():
                    if ":" not in line:
                        continue

                    key, value = line.split(":", 1)
                    metadata[key.strip()] = value.strip()

        metadata["body"] = body

        return metadata

    @staticmethod
    def extract_section(body: str, section_name: str) -> str:
        """
        Extracts text under a markdown heading.

        Example:
        ## Objective
        ...
        """

        pattern = rf"##\s*{re.escape(section_name)}\s*(.*?)(?=\n##|\Z)"
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1).strip()

        return ""
