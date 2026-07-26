from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Agent:
    id: str
    name: str
    description: str = ""
    objective: str = ""
    category: str = "General"
    tags: List[str] = field(default_factory=list)
    path: str = ""
    related_prompts: List[str] = field(default_factory=list)
    related_skills: List[str] = field(default_factory=list)
    related_agents: List[str] = field(default_factory=list)


@dataclass
class Prompt:
    id: str
    name: str
    description: str = ""
    argument_hint: str = ""
    agent: Optional[str] = None
    tools: List[str] = field(default_factory=list)
    path: str = ""
    related_skills: List[str] = field(default_factory=list)


@dataclass
class Skill:
    id: str
    name: str
    description: str = ""
    argument_hint: str = ""
    user_invocable: bool = False
    category: str = "General"
    path: str = ""
    related_agents: List[str] = field(default_factory=list)
    related_prompts: List[str] = field(default_factory=list)


@dataclass
class Repository:
    agents: List[Agent] = field(default_factory=list)
    prompts: List[Prompt] = field(default_factory=list)
    skills: List[Skill] = field(default_factory=list)
