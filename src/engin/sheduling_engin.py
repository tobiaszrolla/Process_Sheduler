from src.algorithm.sheduling_algorithm import ShedulingAlgorithm
from src.models.processList import ProcessList
from src.models.process import ProcessState
class ShedulingEngin():
    def __init__(self ,algoritm: ShedulingAlgorithm, max_time: int, process_list: ProcessList):
        self.time = 0
        self.algoritm = algoritm
        self.max_time = max_time
        self.process_list = process_list
    
    def moveIncomingToReady(self):
        new_incoming = []
        for p in self.process_list.incoming:
            if p.arrival_time <= self.time:
                p.state = ProcessState.READY
                self.process_list.ready.append(p)
            else:
                new_incoming.append(p)
        self.process_list.incoming = new_incoming
        


                
