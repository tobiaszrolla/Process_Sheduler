from random import shuffle
from src.models.process import ProcessState
class ProcessList:
    '''
        Class where state of processes is stored
    '''
    def __init__(self):
        self.ready = []
        self.waiting = []
        self.finish = []
        self.incoming = []

    '''
        Helpers for moving process in lists
    '''
    def move_to_ready(self, p, src):
        self.move(p, src, self.ready)
    def move_to_finish(self, p, src):
        self.move(p, src, self.finish)
    def move_to_wait(self, p, src):
        self.move(p, src, self.waiting)

    def add_incoming(self, p):
        self.incoming.append(p)

    def move(self, p, src, dst):
        src.remove(p)
        dst.append(p)
        
    def merge(self, other):
        merged = ProcessList()
        merged.incoming = self.incoming.copy()
        offset = len(merged.incoming)

        for process in other.incoming:
            process.pid += offset
            merged.incoming.append(process)

        shuffle(merged.incoming)

        return merged

    def shuffle_incoming(self):
        shuffle(self.incoming)
    