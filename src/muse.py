
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


class Data:
    def __init__(self, data, packageNums, timestamps):
        self.data = data
        self.packageNums = packageNums
        self.timestamps = timestamps

    @staticmethod
    def fromEEG(data):
        return Data([data[1], data[2], data[3], data[4]], data[0], data[6])

    def getAllData(self):
        return [self.timestamps, self.packageNums] + self.data


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

    
        

