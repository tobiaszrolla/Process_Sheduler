from src.models.processList import ProcessList
from typing import Tuple
from random import uniform
from src.models.process import Process
from collections import deque


def randForTuple(tup: Tuple[float, float]) -> float:
    return uniform(tup[0], tup[1])

def gererateProcesess(
        process_nr: int, 
        nr_of_IO_break: int, 
        min_max_IO_time: Tuple[float, float], 
        min_max_CPU_time: Tuple[float, float],
        max_arr_time: float) -> ProcessList:
    
    p_list = ProcessList()
    for pid in range(process_nr):
        cpu_bursts = deque()
        io_bursts = deque()
        for i in range(nr_of_IO_break):
            cpu_bursts.append(randForTuple(min_max_CPU_time))
            io_bursts.append(randForTuple(min_max_IO_time))
        cpu_bursts.append(randForTuple(min_max_CPU_time))
        p = Process(
                    pid=pid,
                    arrival_time=uniform(0, max_arr_time),
                    cpu_bursts=cpu_bursts,
                    io_bursts=io_bursts)
        p_list.add_ready(p)

    return p_list   
    