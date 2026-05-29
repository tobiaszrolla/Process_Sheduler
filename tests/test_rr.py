from src.data_prep.data_load_incoming import loadIncomingData
from src.models.processList import ProcessState
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.round_robin_algorithm import RoundRobinAlgorithm
def test_RR():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(RoundRobinAlgorithm(), 50, p_list)
    eng.run()

    assert len(eng.process_list.finish) > 0
    assert all(p.state == ProcessState.FINISHED for p in eng.process_list.finish)
    
def test_RR2():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(RoundRobinAlgorithm(2), 5, p_list)
    eng.run()

    #assert p_list.ready[-1].pid == 1
    #assert p_list.ready[-1].cpu_bursts[0] == 3