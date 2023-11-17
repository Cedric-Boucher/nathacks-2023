import argparse
import time

from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from muse import Muse, Data


def main():
    BoardShim.enable_dev_board_logger()

    muse = Muse("00:55:da:b5:c9:df")
    eegData = muse.sampleData(samplingTime=5)

    print(eegData.getAllData())
    plotData(eegData)
    

if __name__ == "__main__":
    main()
