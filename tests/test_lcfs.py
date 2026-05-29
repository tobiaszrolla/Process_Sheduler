from src.data_prep.data_load_incoming import loadIncomingData
from src.models.processList import ProcessState
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.lcsf_algorithm import LCSFalgorithm
def test_LCFS():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(LCSFalgorithm(), 50, p_list)
    eng.run()

    assert len(eng.process_list.finish) > 0
    assert all(p.state == ProcessState.FINISHED for p in eng.process_list.finish)

def test_LCFS2():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(LCSFalgorithm(), 20, p_list)
    eng.run()

    assert len(eng.process_list.finish) == 2
    assert eng.process_list.finish[1].pid == 3
    assert eng.process_list.finish[0].pid == 1

    assert len(eng.process_list.waiting) == 1
    assert eng.process_list.waiting[0].pid == 4

    





