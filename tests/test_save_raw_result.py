from src.data_prep.data_load_incoming import loadIncomingData
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.sjf_algorithm import SJFalgorithm
from src.results.save_raw_result import saveRawResult
from src.results.save_raw_metrics import saveRawMetrics
import os
def test_Save_raw():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(SJFalgorithm(), 20, p_list)
    eng.run()

    assert len(eng.process_list.finish) == 2
    assert eng.process_list.finish[0].pid == 1
    assert eng.process_list.finish[1].pid == 0

    saveRawResult(eng.process_list, "./tests/save_test.json")
    saveRawMetrics(eng.metrics, "./tests/save_test_metrics.json")

    assert eng.process_list.ready[0].cpu_bursts[0] == 5
    assert eng.process_list.ready[1].cpu_bursts[0] == 5
    assert eng.process_list.ready[2].cpu_bursts[0] == 1
    #os.remove("./tests/save_test.json")
