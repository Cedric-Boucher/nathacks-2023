import argparse
import time

from pprint import pprint
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


# Initialize BoardShim object to connect to Muse 2 device.
def getBoardShim():
    params = BrainFlowInputParams()
    params.mac_address = "00:55:da:b5:c9:df"
    boardId = BoardIds.MUSE_2_BOARD
    board = BoardShim(boardId, params)
    return board


def main():
    BoardShim.enable_dev_board_logger()

    board = getBoardShim()

    board.prepare_session()
    board.start_stream()
    time.sleep(1)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data(100)  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()

    print(data)
    print(data.shape)


if __name__ == "__main__":
    main()
