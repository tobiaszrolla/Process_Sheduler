from src.models.processList import ProcessList
from src.models.process import Process
from collections import deque
import json

def loadIncomingData(path: str) -> ProcessList:
    with open(path, "r") as f:
        data = json.load(f)

    p_list = ProcessList()

    for item in data:
        p_list.incoming.append(Process(
            pid=item["pid"],
            arrival_time=item["arrival_time"],
            cpu_bursts=deque(item["cpu_bursts"]),
            io_bursts=deque(item["io_bursts"]),
        ))
    return p_list

