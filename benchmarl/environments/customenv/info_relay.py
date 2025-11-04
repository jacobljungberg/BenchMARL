from dataclasses import dataclass, MISSING


@dataclass
class TaskConfig:
    task: str = MISSING 
    parallel: bool = MISSING
    max_cycles: int = MISSING
    num_agents: int = MISSING
    num_bases: int = MISSING
    num_emitters: int = MISSING
    num_messages: int = MISSING
    antenna_used: bool = MISSING
    observe_self: bool = MISSING
    a_max: float = MISSING
    num_CL_episodes: int = MISSING
    num_r_help_episodes: int = MISSING