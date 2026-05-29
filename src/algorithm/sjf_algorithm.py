from src.algorithm.sheduling_algorithm import ShedulingAlgorithm
from src.models.process import Process
class SJFalgorithm(ShedulingAlgorithm):
    def choose(self, ready_queue):
        if not ready_queue:
            return None
        else:
            shortest_process = ready_queue[0]
            for process in ready_queue:
                if process.cpu_bursts[0] < shortest_process.cpu_bursts[0]:
                    shortest_process = process
            return shortest_process
