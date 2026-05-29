from src.algorithm.sheduling_algorithm import ShedulingAlgorithm

class RoundRobinAlgorithm(ShedulingAlgorithm):

    def __init__(self, quantum=10):
        self.quantum = quantum
        self.counter = 0
        self.index = 0
        self.current = None

    def choose(self, ready_queue):
        if not ready_queue:
            return None
        

        if self.current is None or self.counter >= self.quantum:
            self.current = ready_queue[0]
            self.counter = 0

            #self.current = ready_queue[self.index % len(ready_queue)]
            ready_queue.append(ready_queue[0])
            ready_queue.remove(ready_queue[0])
        self.counter += 1
        return ready_queue[0]