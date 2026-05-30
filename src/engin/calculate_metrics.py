from dataclasses import dataclass, field
from src.models.processList import ProcessList
import statistics

@dataclass
class CalculateMetrics():
    avr_turnaround_time: float = field(default=None)
    avr_response_time: float = field(default=None)
    avr_waiting_time: float = field(default=None)
    throughput: float = field(default=None)
    fairnes: float = field(default=None)

    def avrTurnaroundTime(self, processes: ProcessList):
        finished = processes.finish
        if not finished:
            self.avr_turnaround_time = None
            return
        times = 0
        for p in finished:
            times += p.turnaround_time
        self.avr_turnaround_time = times / len(finished)
        
    def avrResponseTime(self, processes: ProcessList):
        finished = processes.finish
        ready = processes.ready
        waiting = processes.waiting
        started_processes = len(finished) + len(waiting)
        times = 0
        for p in finished:
            times += p.response_time
        for p in waiting:
            times += p.response_time
        for p in ready:
            if p.response_time:
                started_processes += 1
                times += p.response_time
        self.avr_response_time = times / started_processes
    def avrWaitingTime(self, processes: ProcessList):
        finished = processes.finish
        ready = processes.ready
        waiting = processes.waiting
        times = 0
        for p in finished:
            times += p.waiting_time
        for p in waiting:
            times += p.waiting_time
        for p in ready:
            times += p.waiting_time
        self.avr_waiting_time = times / (len(finished) + len(ready) + len(waiting))

    def throughputCalc(self ,processes, total_time):
        finished = len(processes.finish)
        self.throughput = finished / total_time

    def fairnessCalc(self, processes):
        finished = processes.finish
        ready = processes.ready
        waiting = processes.waiting
        times = []

        for p in finished:
            times.append(p.waiting_time)

        for p in waiting:
            times.append(p.waiting_time)

        for p in ready:
            times.append(p.waiting_time)
            self.fairness = statistics.pstdev(times)
    
    def calculate(self, processes: ProcessList, total_time: int):
       self.avrTurnaroundTime(processes)
       self.avrResponseTime(processes)
       self.avrWaitingTime(processes)
       self.throughputCalc(processes, total_time)
       self.fairnessCalc(processes)



    