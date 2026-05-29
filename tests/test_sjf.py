from src.data_prep.data_load_incoming import loadIncomingData
from src.models.processList import ProcessState
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.sjf_algorithm import SJFalgorithm
def test_FIFO():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(SJFalgorithm(), 50, p_list)
    eng.run()

    assert len(eng.process_list.finish) > 0
    assert all(p.state == ProcessState.FINISHED for p in eng.process_list.finish)