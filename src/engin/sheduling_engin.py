from src.algorithm.sheduling_algorithm import ShedulingAlgorithm
from src.models.processList import ProcessList
from src.models.process import ProcessState, Process
from src.simulation.io import execute_io_step
from src.simulation.cpu import execute_cpu_step
class ShedulingEngin():
    def __init__(self ,algoritm: ShedulingAlgorithm, max_time: int, process_list: ProcessList, start_time=0, quantum=10):
        self.algoritm = algoritm
        self.max_time = max_time
        self.process_list = process_list
        self.time = start_time
        self.time = quantum
        
    
    def moveIncomingToReady(self):
        '''
            Check if we can add process to Ready
            list(...) helps with keeping correct iteration
        '''
        for p in list(self.process_list.incoming):
            if p.arrival_time <= self.time:
                self.process_list.move_to_ready(
                    p, 
                    self.process_list.incoming
                )

    def wait(self):
        '''
            execute wait for every process in ready list
        '''
        for p in list(self.process_list.waiting):
            execute_io_step(p)
            if p.state == ProcessState.READY:
                self.process_list.move_to_ready(
                    p, 
                    self.process_list.waiting
                )

            elif p.state == ProcessState.FINISHED:
                self.process_list.move_to_finish(
                    p, 
                    self.process_list.waiting
                )


    def cpuStep(self, p: Process):

        execute_cpu_step(p, self.time)

        if p.state == ProcessState.WAITING:
            self.process_list.move_to_wait(
                p,
                self.process_list.ready
            )

        elif p.state == ProcessState.FINISHED:
            self.process_list.move_to_finish(
                p,
                self.process_list.ready
            )
            
    def run(self):
        for i in range(self.max_time):
            a =1

        


    



        


                
