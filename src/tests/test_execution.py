from src.models.process import Process
from src.simulation.execution import execute_step  

def test_execute_step_first_run():
    p = Process(pid=1, arrival_time=0, burst_time=10)

    run_time = execute_step(p, current_time=0, quantum=3)

    assert run_time == 3
    assert p.remaining_time == 7
    assert p.is_started is True
    assert p.response_time == 0

def test_process_finishes():
    p = Process(pid=1, arrival_time=0, burst_time=5)

    execute_step(p, 0, 5)

    assert p.is_finished is True
    assert p.completion_time == 5
    assert p.turnaround_time == 5
    assert p.waiting_time == 0

def test_multi_step_execution():
    p = Process(pid=1, arrival_time=0, burst_time=10)

    current_time = 0

    run1 = execute_step(p, current_time, quantum=3)
    current_time += run1

    run2 = execute_step(p, current_time, quantum=3)
    current_time += run2

    run3 = execute_step(p, current_time, quantum=3)
    current_time += run3

    assert run1 == 3
    assert run2 == 3
    assert run3 == 3

    assert p.remaining_time == 1  # 10 - 9 = 1
    assert p.is_started is True
    assert p.is_finished is False

    # process should not yet be completed
    assert p.completion_time is None
