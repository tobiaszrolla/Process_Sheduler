import pytest
from collections import deque

from src.models.process import Process, ProcessState
from src.simulation.cpu import execute_cpu_step
from src.simulation.io import execute_io_step


def test_process_initialization():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )

    assert process.state == ProcessState.READY

    assert process.start_time is None
    assert process.completion_time is None
    assert process.response_time is None

    assert process.cpu_bursts[0] == 10


def test_first_cpu_execution():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )

    run_time = execute_cpu_step(
        process,
        current_time=0,
        quantum=3
    )

    assert run_time == 3

    # quantum expired
    assert process.state == ProcessState.READY

    assert process.cpu_bursts[0] == 7

    assert process.start_time == 0
    assert process.response_time == 0


def test_process_finishes_after_single_burst():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([5]),
        io_bursts=deque([])
    )

    run_time = execute_cpu_step(
        process,
        current_time=0,
        quantum=10
    )

    assert run_time == 5

    assert process.state == ProcessState.FINISHED

    assert process.completion_time == 5

    assert process.response_time == 0

    assert len(process.cpu_bursts) == 0


def test_process_enters_waiting_state():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([5, 3]),
        io_bursts=deque([4])
    )

    execute_cpu_step(
        process,
        current_time=0,
        quantum=5
    )

    assert process.state == ProcessState.WAITING

    assert process.io_bursts[0] == 4

    assert process.cpu_bursts[0] == 3


def test_io_execution_and_return_to_ready():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([5, 3]),
        io_bursts=deque([4])
    )

    execute_cpu_step(process, 0, 5)

    assert process.state == ProcessState.WAITING

    execute_io_step(process, 2)

    assert process.io_bursts[0] == 2

    assert process.state == ProcessState.WAITING

    execute_io_step(process, 2)

    assert len(process.io_bursts) == 0

    assert process.state == ProcessState.READY


def test_multiple_cpu_steps():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )

    t = 0

    r1 = execute_cpu_step(process, t, 3)
    t += r1

    r2 = execute_cpu_step(process, t, 3)
    t += r2

    r3 = execute_cpu_step(process, t, 3)
    t += r3

    assert r1 == 3
    assert r2 == 3
    assert r3 == 3

    assert process.cpu_bursts[0] == 1

    # after quantum expiration
    assert process.state == ProcessState.READY

    assert process.completion_time is None


def test_process_finishes_after_multiple_steps():

    process = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )

    t = 0

    while process.state != ProcessState.FINISHED:

        dt = execute_cpu_step(
            process,
            current_time=t,
            quantum=3
        )

        t += dt

    assert process.state == ProcessState.FINISHED

    assert process.completion_time == 10

    assert len(process.cpu_bursts) == 0