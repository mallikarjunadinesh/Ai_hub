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

    # RepositoryParser exposes scan(), not parse()
    repository = parser.scan()

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

    print("\n" + "=" * 60)
    print("AI HUB generation completed successfully!")
    print("=" * 60)
    print(f"\nOutput folder: {output_path}")
    print(f"Open: {output_path / 'index.html'}")


if __name__ == "__main__":
    main()
