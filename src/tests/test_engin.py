from src.models.process import Process, ProcessState
from collections import deque
from src.models.processList import ProcessList
from src.algorithm.sheduling_algorithm import ShedulingAlgorithm
from src.engin.sheduling_engin import ShedulingEngin

def test_moveToReady():
    p = Process(
        pid=1,
        arrival_time=0,
        cpu_bursts=deque([10]),
        io_bursts=deque([])
    )
    p2 = Process(
        pid=2,
        arrival_time=1,
        cpu_bursts=deque([10,9]),
        io_bursts=deque([12])
    )
    p3 = Process(
        pid=3,
        arrival_time=2,
        cpu_bursts=deque([110]),
        io_bursts=deque([])
    )
    p_list = ProcessList()

    p_list.add_incoming(p)
    p_list.add_incoming(p2)
    p_list.add_incoming(p3)

    eng = ShedulingEngin(ShedulingAlgorithm() , 3, p_list)

    eng.time = 1
    eng.moveIncomingToReady()
    assert len(eng.process_list.incoming) == 1
    assert len(eng.process_list.ready) == 2
    assert eng.process_list.ready[0].state == ProcessState.READY


