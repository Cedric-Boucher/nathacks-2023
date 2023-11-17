import argparse
import time
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from muse import Muse, Data


ANIMATION_FRAMETIME = 100 # ms


def animated_plot(i, muse: Muse, main_subplot: plt.Axes, fft_subplot: plt.Axes):
    data = muse.sampleData(samplingTime=ANIMATION_FRAMETIME/1000).data
    main_subplot.clear()
    import random
    main_subplot.plot([0, 1], [0, random.randint(1, 5)])
    #main_subplot.plot(data[6], data[1])
    #main_subplot.plot(data[6], data[2])
    #main_subplot.plot(data[6], data[3])
    #main_subplot.plot(data[6], data[4])
    #main_subplot.legend(muse.EEG_NAMES)
    fft_subplot.clear()
    fft_subplot.plot([0, 1], [1, 0])
    #fft_subplot.plot(data[6], data[1])
    #fft_subplot.plot(data[6], data[2])
    #fft_subplot.plot(data[6], data[3])
    #fft_subplot.plot(data[6], data[4])
    fft_subplot.legend([i+" fft" for i in muse.EEG_NAMES])


def main():
    main_fig = plt.figure()
    main_subplot = plt.subplot(1,1,1)
    fft_subplot = plt.subplot(2,1,1)
    #frequency = np.arange(-np.fft.fft(data[1]).shape[0]/2, np.fft.fft(data[1]).shape[0]/2) / timeDelta
    #plt.plot(frequency, np.fft.fft(data[1]))
    #plt.plot(frequency, np.fft.fft(data[2]))
    #plt.plot(frequency, np.fft.fft(data[3]))
    #plt.plot(frequency, np.fft.fft(data[4]))
    muse = Muse("00:55:da:b5:c9:df".upper())
    ani = animation.FuncAnimation(main_fig, animated_plot, fargs = (muse, main_subplot, fft_subplot), interval = ANIMATION_FRAMETIME)
    plt.show()


if __name__ == "__main__":
    main()
