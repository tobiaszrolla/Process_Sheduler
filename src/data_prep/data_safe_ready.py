from src.models.processList import ProcessList
import json
def safeDataReady(process_lis: ProcessList, path: str):
    data = []
    for process in process_lis.ready:
        data.append({
            "pid": process.pid,
            "arrival_time": process.arrival_time,
            "cpu_bursts": list(process.cpu_bursts),
            "io_bursts": list(process.io_bursts)
        })
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
        
