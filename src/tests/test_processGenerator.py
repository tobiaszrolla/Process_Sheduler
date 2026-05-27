from src.data_prep.data_generation import gererateProcesess
def test_processGenerator():
    p_list = gererateProcesess(10, 3, [1, 6], [1, 10], 2)
    assert len(p_list.incoming) == 10
    assert len(p_list.incoming[0].io_bursts) == 3
    assert len(p_list.incoming[0].cpu_bursts) == 4
    
    for i in range(10):
        for j in range(3):
            assert p_list.incoming[i].io_bursts[j] <= 6 and p_list.incoming[i].io_bursts[j] >= 1
        for j in range(4):
            assert p_list.incoming[i].cpu_bursts[j] <= 10 and p_list.incoming[i].cpu_bursts[j] >= 1
            assert p_list.incoming[i].arrival_time <= 2