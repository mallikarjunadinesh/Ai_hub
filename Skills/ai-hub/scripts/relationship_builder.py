from utils import normalize_name


class RelationshipBuilder:
    """
    Builds relationships between Agents, Prompts and Skills.
    """

    def __init__(self, repository):
        self.repository = repository

    def build(self):

        print("Building relationships...")

        self._link_prompts_to_agents()
        self._link_skills_to_agents()
        self._link_related_skills()

        print("Relationships completed.")

    # -------------------------------------------------------
    # Prompt -> Agent
    # -------------------------------------------------------

    def _link_prompts_to_agents(self):

        for prompt in self.repository.prompts:

            if not prompt.agent:
                continue

            for agent in self.repository.agents:

                if normalize_name(agent.name) == normalize_name(prompt.agent):

                    if prompt.id not in agent.related_prompts:
                        agent.related_prompts.append(prompt.id)

                    if agent.id not in prompt.related_agents:
                        prompt.related_agents.append(agent.id)

    # -------------------------------------------------------
    # Skill -> Agent
    # -------------------------------------------------------

    def _link_skills_to_agents(self):

        for agent in self.repository.agents:

            try:

                with open(agent.path, "r", encoding="utf-8") as f:
                    content = f.read().lower()

            except Exception:
                continue

            for skill in self.repository.skills:

                if normalize_name(skill.name) in content:

                    if skill.id not in agent.related_skills:
                        agent.related_skills.append(skill.id)

                    if agent.id not in skill.related_agents:
                        skill.related_agents.append(agent.id)

    # -------------------------------------------------------
    # Related Skills
    # -------------------------------------------------------

    def _link_related_skills(self):

        for agent in self.repository.agents:

            skills = agent.related_skills

            for i in range(len(skills)):
                for j in range(i + 1, len(skills)):

                    skill1 = self._find_skill(skills[i])
                    skill2 = self._find_skill(skills[j])

                    if not skill1 or not skill2:
                        continue

                    if skill2.id not in skill1.related_skills:
                        skill1.related_skills.append(skill2.id)

                    if skill1.id not in skill2.related_skills:
                        skill2.related_skills.append(skill1.id)

    # -------------------------------------------------------
    # Helper Methods
    # -------------------------------------------------------

    def _find_skill(self, skill_id):

        for skill in self.repository.skills:

            if skill.id == skill_id:
                return skill

        return None
