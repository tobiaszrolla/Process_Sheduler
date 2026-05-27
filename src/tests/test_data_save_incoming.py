import os
import json
from src.data_prep.data_save_incoming import saveDataIncoming
from src.data_prep.data_generation import gererateProcesess

def test_dataSefeincoming():
    path = "./test_save.json"
    p = gererateProcesess(10, 3, [1,3], [1,3], 8)
    saveDataIncoming(p, path)

    assert os.path.exists(path)

    with open(path) as f:
        data = json.load(f)
    assert len(data) == len(p.incoming)

    os.remove(path)