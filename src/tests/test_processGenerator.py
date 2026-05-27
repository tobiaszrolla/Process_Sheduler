from src.data_prep.data_generation import gererateProcesess
def test_processGenerator():
    p_list = gererateProcesess(10, 3, [1.0, 6.4], [1.0, 10.0], 2)
    assert len(p_list.ready) == 10
    assert len(p_list.ready[0].io_bursts) == 3
    assert len(p_list.ready[0].cpu_bursts) == 4
    
    for i in range(10):
        for j in range(3):
            assert p_list.ready[i].io_bursts[j] <= 6.4 and p_list.ready[i].io_bursts[j] >= 1.0 
        for j in range(4):
            assert p_list.ready[i].cpu_bursts[j] <= 10.0 and p_list.ready[i].cpu_bursts[j] >= 1.0
        assert p_list.ready[i].arrival_time <= 2.0