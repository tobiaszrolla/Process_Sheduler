from src.data_prep.data_load_incoming import loadIncomingData
from src.models.processList import ProcessState
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.sjf_algorithm import SJFalgorithm

def test_SJF():
    p_list = loadIncomingData("./tests/test_data.json")
    eng = ShedulingEngin(SJFalgorithm(), 20, p_list)
    eng.run()

    assert eng.metrics.avr_turnaround_time == 13
    assert eng.metrics.avr_response_time == 5.25
    assert eng.metrics.avr_waiting_time == 10.4
    assert eng.metrics.throughput == 0.1
    assert eng.metrics.fairnes == 5.535341001239219


