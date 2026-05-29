from collections import deque
from src.models.process import Process
from src.models.processList import ProcessList  
def test_processList_init():
    p = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )
    p2 = Process(
        pid=2,
        arrival_time=0,
        cpu_bursts=deque([10,9]),
        io_bursts=deque([12])
    )
    p3 = Process(
        pid=3,
        arrival_time=0,
        cpu_bursts=deque([110]),
        io_bursts=deque([])
    )
    p_list = ProcessList()

    p_list.add_incoming(p)
    p_list.add_incoming(p2)
    p_list.add_incoming(p3)

    assert p_list.incoming[0] == p
    assert p_list.incoming[1] == p2
    assert p_list.incoming[2] == p3

def test_processList_change():
    p = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )
    p2 = Process(
        pid=2,
        arrival_time=0,
        cpu_bursts=deque([10,9]),
        io_bursts=deque([12])
    )
    p3 = Process(
        pid=3,
        arrival_time=0,
        cpu_bursts=deque([110]),
        io_bursts=deque([])
    )
    p_list = ProcessList()

    p_list.add_incoming(p)
    p_list.add_incoming(p2)
    p_list.add_incoming(p3)

    p_list.move(p, p_list.incoming, p_list.waiting)
    assert p_list.waiting[0] == p
    assert p_list.incoming[0] == p2
    assert p_list.incoming[1] == p3
    