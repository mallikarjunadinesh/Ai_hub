from pathlib import Path

from parser import RepositoryParser
from relationship_builder import RelationshipBuilder

from json_generator import JsonGenerator
from search import SearchGenerator

from home_generator import HomeGenerator
from domain_generator import DomainGenerator
from details_generator import DetailsGenerator


def main():

    base_path = Path(__file__).parent.parent

    output_path = base_path / "output"

    print("=" * 60)
    print("AI HUB Generator")
    print("=" * 60)

    print("\nScanning repository...")

    parser = RepositoryParser(base_path)

    repository = parser.parse()

    print(
        f"Found "
        f"{len(repository.agents)} Agents, "
        f"{len(repository.prompts)} Prompts, "
        f"{len(repository.skills)} Skills"
    )

    print("\nBuilding relationships...")

    RelationshipBuilder(repository).build()

    print("\nGenerating JSON...")

    JsonGenerator(
        repository,
        output_path
    ).generate()

    SearchGenerator(
        repository,
        output_path
    ).generate()

    print("\nGenerating HTML...")

    HomeGenerator(
        repository,
        output_path
    ).generate()

    DomainGenerator(
        repository,
        output_path
    ).generate()

    DetailsGenerator(
        repository,
        output_path
    ).generate()

    print("\nDone!")

    print(
        f"\nOpen:\n"
        f"{output_path / 'index.html'}"
    )


if __name__ == "__main__":
    main()
