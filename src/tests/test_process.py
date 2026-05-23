from src.models.process import Process

def test_process_initialization():
    p = Process(pid=1, arrival_time=0, burst_time=10)

    assert p.remaining_time == 10
    assert p.is_started is False
    assert p.is_finished is False