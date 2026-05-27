import os
import json
from src.data_prep.data_save_ready import saveDataReady
from src.data_prep.data_generation import gererateProcesess
from src.models.processList import ProcessList
from src.models.process import Process

def test_dataSefeReady():
    path = "./test_save.json"
    p = gererateProcesess(10, 3, [1,3], [1,3], 8)
    saveDataReady(p, path)

    assert os.path.exists(path)

    with open(path) as f:
        data = json.load(f)
    assert len(data) == len(p.ready)

    os.remove(path)