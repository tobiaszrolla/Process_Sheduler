from src.models.process import Process, ProcessState
from collections import deque


def test_process_initialization():
    p = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )

    assert list(p.cpu_bursts) == [10]
    assert list(p.io_bursts) == []
    assert p.state == ProcessState.READY

    assert p.start_time is None
    assert p.completion_time is None
    assert p.response_time is None