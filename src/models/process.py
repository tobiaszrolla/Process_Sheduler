from dataclasses import dataclass, field

@dataclass
class Process:
    pid: int
    arrival_time: float
    burst_time: float

    remaining_time: float = field(init=False)

    start_time: float = field(default=None)
    completion_time: float = field(default=None)

    waiting_time: float = field(default=0.0)
    turnaround_time: float = field(default=0.0)
    response_time: float = field(default=None)

    is_started: bool = field(default=False)
    is_finished: bool = field(default=False)

    def __post_init__(self):
        self.remaining_time = self.burst_time

