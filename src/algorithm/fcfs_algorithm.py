from src.algorithm.sheduling_algorithm import ShedulingAlgorithm

class FCFSalgorithm(ShedulingAlgorithm):
    def choose(self, ready_queue):
        if not ready_queue:
            return None
        else:
            return ready_queue[0]
