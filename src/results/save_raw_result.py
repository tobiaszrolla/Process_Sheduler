from src.models.processList import ProcessList
from src.models.process import Process
import json

def preperRecord(process: Process):
    return {
            "pid": process.pid,
            "arrival_time": process.arrival_time,
            "cpu_bursts": list(process.cpu_bursts),
            "io_bursts": list(process.io_bursts),
            "start_time": process.start_time,
            "completion_time": process.completion_time,
            "response_time": process.response_time,
            "turnaround_time": process.turnaround_time,
            "waiting_time": process.waiting_time,
            "state": process.state.value

        }
def saveRawResult(process_lis: ProcessList, path: str):
    data = []
    for process in process_lis.incoming:
        data.append(preperRecord(process))
    for process in process_lis.ready:
        data.append(preperRecord(process))
    for process in process_lis.waiting:
        data.append(preperRecord(process))
    for process in process_lis.finish:
        data.append(preperRecord(process))
    with open(path, "w") as f:
        json.dump(data, f, indent=10)