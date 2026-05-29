from src.algorithm.sheduling_algorithm import ShedulingAlgorithm
from src.models.process import Process
class SJFalgorithm(ShedulingAlgorithm):
    def __init__(self):
            self.shortest_process = None
    def choose(self, ready_queue):
        if not ready_queue:
            return None
        elif self.shortest_process not in ready_queue:
            self.shortest_process = ready_queue[0]
            for process in ready_queue:
                if process.cpu_bursts[0] < self.shortest_process.cpu_bursts[0]:
                    self.shortest_process = process
        return self.shortest_process
