from pathlib import Path
from typing import Dict


class IdGenerator:
    """
    Generates stable IDs for Agents, Prompts, and Skills.
    """

    def __init__(self):
        self.counters: Dict[str, int] = {
            "AGT": 0,
            "PRM": 0,
            "SKL": 0,
        }

    def next_id(self, prefix: str) -> str:
        """
        Returns the next ID for the given prefix.

        Example:
            AGT-001
            PRM-015
            SKL-008
        """
        if prefix not in self.counters:
            raise ValueError(f"Unknown prefix: {prefix}")

        self.counters[prefix] += 1
        return f"{prefix}-{self.counters[prefix]:03d}"


def ensure_directory(path: str):
    """
    Create a directory if it does not already exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def read_markdown(file_path: str) -> str:
    """
    Reads a markdown file and returns its content.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def normalize_name(name: str) -> str:
    """
    Normalize a name for comparison.
    """
    return (
        name.lower()
        .replace("-", " ")
        .replace("_", " ")
        .strip()
    )
