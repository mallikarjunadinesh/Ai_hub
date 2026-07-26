from utils import normalize_name


class RelationshipBuilder:
    """
    Builds relationships between Agents, Prompts and Skills.
    """

    def __init__(self, repository):
        self.repository = repository

    def build(self):
        self._link_prompts_to_agents()
        self._link_skills_to_agents()

    def _link_prompts_to_agents(self):
        """
        Connect Prompts to their Agents.
        """

        for prompt in self.repository.prompts:

            if not prompt.agent:
                continue

            for agent in self.repository.agents:

                if normalize_name(agent.name) == normalize_name(prompt.agent):

                    agent.related_prompts.append(prompt.id)

    def _link_skills_to_agents(self):
        """
        Connect Skills to Agents by checking whether
        the skill name appears in the agent document.
        """

        for agent in self.repository.agents:

            try:
                with open(agent.path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
            except Exception:
                continue

            for skill in self.repository.skills:

                if normalize_name(skill.name) in content:

                    agent.related_skills.append(skill.id)

                    skill.related_agents.append(agent.id)
