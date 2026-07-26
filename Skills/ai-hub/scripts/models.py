from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Agent:
    """
    Represents an Agent in the repository.
    """

    id: str
    name: str
    description: str = ""

    category: str = "General"

    objective: str = ""
    usage: str = ""
    benefits: str = ""

    sections: Dict[str, str] = field(default_factory=dict)

    tags: List[str] = field(default_factory=list)

    path: str = ""

    related_prompts: List[str] = field(default_factory=list)
    related_skills: List[str] = field(default_factory=list)
    related_agents: List[str] = field(default_factory=list)


@dataclass
class Prompt:
    """
    Represents a Prompt in the repository.
    """

    id: str
    name: str
    description: str = ""

    category: str = "General"

    objective: str = ""
    usage: str = ""
    benefits: str = ""

    argument_hint: str = ""

    agent: Optional[str] = None

    tools: List[str] = field(default_factory=list)

    sections: Dict[str, str] = field(default_factory=dict)

    path: str = ""

    related_skills: List[str] = field(default_factory=list)
    related_agents: List[str] = field(default_factory=list)


@dataclass
class Skill:
    """
    Represents a Skill in the repository.
    """

    id: str
    name: str
    description: str = ""

    category: str = "General"

    objective: str = ""
    usage: str = ""
    benefits: str = ""

    argument_hint: str = ""

    user_invocable: bool = False

    tags: List[str] = field(default_factory=list)

    sections: Dict[str, str] = field(default_factory=dict)

    path: str = ""

    related_agents: List[str] = field(default_factory=list)
    related_prompts: List[str] = field(default_factory=list)
    related_skills: List[str] = field(default_factory=list)


@dataclass
class Repository:
    """
    Represents the complete AI repository.
    """

    agents: List[Agent] = field(default_factory=list)

    prompts: List[Prompt] = field(default_factory=list)

    skills: List[Skill] = field(default_factory=list)
