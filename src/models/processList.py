from random import shuffle
class ProcessList:
    '''
        Class where state of processes is stored
    '''
    def __init__(self):
        self.ready = []
        self.waiting = []
        self.finish = []
        self.incoming = []

    def add_incoming(self, p):
        self.incoming.append(p)

    def move(self, p, src, dst):
        src.remove(p)
        dst.append(p)

    def merge_with_new_pid(self, other):

        merged = ProcessList()

        merged.ready = self.ready.copy()

        offset = len(self.ready)

        for process in other.ready:
            process.pid += offset
            merged.ready.append(process)

        
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
    