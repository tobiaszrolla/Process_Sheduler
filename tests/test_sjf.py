from src.data_prep.data_load_incoming import loadIncomingData
from src.models.processList import ProcessState
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.sjf_algorithm import SJFalgorithm
def test_SJF():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(SJFalgorithm(), 50, p_list)
    eng.run()

    assert len(eng.process_list.finish) > 0
    assert all(p.state == ProcessState.FINISHED for p in eng.process_list.finish)


def test_SJF2():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(SJFalgorithm(), 20, p_list)
    eng.run()

    assert len(eng.process_list.finish) == 2
    assert eng.process_list.finish[0].pid == 1
    assert eng.process_list.finish[1].pid == 0

    assert eng.process_list.ready[0].cpu_bursts[0] == 5
    assert eng.process_list.ready[1].cpu_bursts[0] == 5
    assert eng.process_list.ready[2].cpu_bursts[0] == 1
