from src.algorithm.sheduling_algorithm import ShedulingAlgorithm
from src.models.processList import ProcessList
from src.models.process import ProcessState, Process
from src.simulation.io import execute_io_step
from src.simulation.cpu import execute_cpu_step
from src.engin.calculate_metrics import CalculateMetrics
class ShedulingEngin():
    def __init__(self ,algoritm: ShedulingAlgorithm, max_time: int, process_list: ProcessList, start_time=0):
        self.algoritm = algoritm
        self.max_time = max_time
        self.process_list = process_list
        self.time = start_time
        self.metrics = CalculateMetrics()
        
    
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


    def move_executed_process(self, p: Process):
        if p == None:
            return
        elif p.state == ProcessState.WAITING:
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
        while self.time <= self.max_time:
            self.moveIncomingToReady()
            p = self.algoritm.choose(self.process_list.ready)
            if p is not None:
                execute_cpu_step(p, self.time)
            self.time += 1
            for waiting in self.process_list.ready:
                if waiting != p:
                    waiting.waiting_time += 1       
            self.wait()
            self.move_executed_process(p)
        self.metrics.calculate(self.process_list, self.max_time)

            

        


    



        


                
