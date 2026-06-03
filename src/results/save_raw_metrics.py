from src.models.processList import ProcessList
from src.engin.calculate_metrics import CalculateMetrics
import json

def saveRawMetrics(metrics: CalculateMetrics, path: str):
    data = []
    data.append({
            "avr_turnaround_time": metrics.avr_turnaround_time,
            "avr_response_time": metrics.avr_response_time,
            "avr_waiting_time": metrics.avr_waiting_time,
            "throughput": metrics.throughput,
            "fairnes": metrics.fairnes

        })
    with open(path, "w") as f:
        json.dump(data, f, indent=5)
    