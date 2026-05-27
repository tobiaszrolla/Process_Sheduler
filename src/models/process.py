from dataclasses import dataclass, field
from enum import Enum
from collections import deque


class ProcessState(Enum):
    READY = "READY"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    FINISHED = "FINISHED"


@dataclass
class Process:
    """
    Represents a process in CPU scheduling simulation.

    Attributes:
        pid: Process identifier
        state: current process state
        arrival_time: Time when process arrives in the system
        cpu_bursts: queq of CPU execution times
        io_bursts: queq of waitings for IO
        start_time: First time process gets CPU
        completion_time: Time when process finishes execution
        waiting_time: Total time spent waiting in ready queue
        response_time: Time from arrival to first CPU access
    """
    pid: int
    arrival_time: int

    cpu_bursts: deque[int]
    io_bursts: deque[int]

    start_time: int = field(default=None)
    completion_time: int = field(default=None)
    response_time: int = field(default=None)

    state: ProcessState = ProcessState.READY

    def current_cpu(self) -> int:
        return self.cpu_bursts[0] if self.cpu_bursts else 0

    def is_finished(self) -> bool:
        return self.state == ProcessState.FINISHED

