from parser import RepositoryParser


def print_summary(repository):
    print("\n" + "=" * 50)
    print("              AI HUB")
    print("=" * 50)

    print(f"Agents  : {len(repository.agents)}")
    print(f"Prompts : {len(repository.prompts)}")
    print(f"Skills  : {len(repository.skills)}")

    print("=" * 50)
    print("Repository scan completed successfully.")
    print("=" * 50)


def main():
    print("Scanning repository...")

    # Repository root (go up three levels from scripts/)
    parser = RepositoryParser("../../..")

    repository = parser.scan()

    print_summary(repository)


if __name__ == "__main__":
    main()
