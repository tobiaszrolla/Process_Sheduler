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
