from src.data_prep.data_load_incoming import loadIncomingData
from src.models.processList import ProcessState
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.fcfs_algorithm import FCFSalgorithm
def test_FIFO():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(FCFSalgorithm(), 50, p_list)
    eng.run()

    assert len(eng.process_list.finish) > 0
    assert all(p.state == ProcessState.FINISHED for p in eng.process_list.finish)

def test_FIFO2():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(FCFSalgorithm(), 20, p_list)
    eng.run()

    assert len(eng.process_list.finish) == 0

    assert eng.process_list.ready[0].pid == 1
    assert eng.process_list.ready[0].cpu_bursts[0] == 1





