from dataclasses import dataclass, field

@dataclass
class Process:
    """
    Represents a process in CPU scheduling simulation.

    Attributes:
        pid: Process identifier
        arrival_time: Time when process arrives in the system
        burst_time: Total CPU execution time required
        remaining_time: Remaining CPU time to finish execution
        start_time: First time process gets CPU
        completion_time: Time when process finishes execution
        waiting_time: Total time spent waiting in ready queue
        turnaround_time: Total time from arrival to completion
        response_time: Time from arrival to first CPU access
        is_started: Whether process has started execution
        is_finished: Whether process has completed execution
    """
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

    def get_process_on_CPU(arrival_time, self):
        self.arrival_time = arrival_time
    
    @property
    def finished(self) -> bool:
        return self.is_finished
