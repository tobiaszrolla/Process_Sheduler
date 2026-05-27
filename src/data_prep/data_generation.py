from src.models.processList import ProcessList
from typing import Tuple
from random import randint
from src.models.process import Process
from collections import deque


def randForTuple(tup: Tuple[int, int]) -> int:
    return randint(tup[0], tup[1])

def gererateProcesess(
        process_nr: int, 
        nr_of_IO_break: int, 
        min_max_IO_time: Tuple[int, int], 
        min_max_CPU_time: Tuple[int, int],
        max_arr_time: int) -> ProcessList:
    
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
                    arrival_time=randint(0, max_arr_time),
                    cpu_bursts=cpu_bursts,
                    io_bursts=io_bursts)
        p_list.add_incoming(p)

    return p_list   
    