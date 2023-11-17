
import time
from dataclasses import dataclass
from pprint import pprint

import numpy.typing as npt
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow.data_filter import DataFilter


@dataclass
class Data:
    data: npt.NDArray[np.float64]
    packageNums: npt.NDArray[np.float64]
    timestamps: npt.NDArray[np.float64]

    @staticmethod
    def fromEEG(museData):
        return Data(np.vstack([museData[1], museData[2], museData[3], museData[4]]),
                    museData[0],
                    museData[6])

    @staticmethod
    def fromFile(filename):
        data = DataFilter.read_file(filename)
        return Data(np.vstack([data[2], data[3], data[4], data[5]]), data[1], data[0])

    def getAllData(self):
        """
        Returns a numpy array with the following Muse data.
        [0] - Timestamps of the samples.
        [1] - Package numbers (?).
        [2] - TP9 samples.
        [3] - Fp1 samples.
        [4] - Fp2 samples.
        [5] - TP10 samples.
        """
        return np.vstack([self.timestamps, self.packageNums, self.data])

    def writeToFile(self, filename):
        DataFilter.write_file(self.getAllData(), filename, "w")


class Muse:
    ID = BoardIds.MUSE_2_BOARD
    EEG_NAMES = ["TP9","Fp1","Fp2","TP10"]

    def __init__(self, macAddress):
        self.initBoard(macAddress)

    def initBoard(self, macAddress):
        params = BrainFlowInputParams()
        params.mac_address = macAddress
        boardId = BoardIds.MUSE_2_BOARD
        self.board = BoardShim(boardId, params)

    def sampleData(self, mode=BrainFlowPresets.DEFAULT_PRESET, samplingTime=1):
        samplingRate = BoardShim.get_sampling_rate(Muse.ID, mode)

        self.board.prepare_session()
        self.board.start_stream()
        time.sleep(samplingTime)
        self.board.stop_stream()
        data = self.board.get_board_data(samplingRate * samplingTime)
        self.board.release_session()

        return Data.fromEEG(data)

