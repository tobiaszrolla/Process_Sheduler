class ProcessList:
    '''
        Class where state of processes is stored
    '''
    def __init__(self):
        self.ready = []
        self.waiting = []
        self.finish = []

    def add_ready(self, p):
        self.ready.append(p)

    def move(self, p, src, dst):
        src.remove(p)
        dst.append(p)
