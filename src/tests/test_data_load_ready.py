import os
import json
from src.data_prep.data_save_ready import saveDataReady
from src.data_prep.data_generation import gererateProcesess
from src.data_prep.data_load_ready import loadReadyData

def test_dataLoadReady():
    path = "./test2_save.json"
    p = gererateProcesess(10, 3, [1,3], [1,3], 8)
    saveDataReady(p, path)

    p2 = loadReadyData(path)

    assert p.ready == p2.ready
    os.remove(path)