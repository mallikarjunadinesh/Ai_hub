from parser import RepositoryParser
from relationship_builder import RelationshipBuilder
from json_generator import JsonGenerator
from search import SearchIndexGenerator


def print_summary(repository):

    print("\n" + "=" * 60)
    print("AI HUB Repository Scan Summary")
    print("=" * 60)

    print(f"Agents  : {len(repository.agents)}")
    print(f"Prompts : {len(repository.prompts)}")
    print(f"Skills  : {len(repository.skills)}")

    print("=" * 60)


def main():

    print("Starting AI HUB generation...\n")

    parser = RepositoryParser("../../..")

    repository = parser.scan()

    RelationshipBuilder(repository).build()

    JsonGenerator(
        repository,
        "../output"
    ).generate()

    SearchIndexGenerator(
        repository,
        "../output"
    ).generate()

    print_summary(repository)

    print("\nAI HUB generation completed successfully.")


if __name__ == "__main__":
    main()
