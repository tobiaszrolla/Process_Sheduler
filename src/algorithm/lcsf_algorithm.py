from src.algorithm.sheduling_algorithm import ShedulingAlgorithm

class LCSFalgorithm(ShedulingAlgorithm):
    def __init__(self):
            self.current_process = None
    def choose(self, ready_queue):
        if not ready_queue:
            return None
        if self.current_process in ready_queue:
           return self.current_process  
        else:
            self.current_process = ready_queue[-1]
            return self.current_process