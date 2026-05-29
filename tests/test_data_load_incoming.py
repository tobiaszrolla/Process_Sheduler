import os
import json
from src.data_prep.data_save_incoming import saveDataIncoming
from src.data_prep.data_generation import gererateProcesess
from src.data_prep.data_load_incoming import loadIncomingData

def test_dataLoadincoming():
    path = "./test2_save.json"
    p = gererateProcesess(10, 3, [1,3], [1,3], 8)
    saveDataIncoming(p, path)

    p2 = loadIncomingData(path)

    assert p.incoming == p2.incoming
    os.remove(path)