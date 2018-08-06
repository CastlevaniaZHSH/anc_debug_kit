# -*- coding: utf-8 -*-
# Created by 2h5h on 2018/8/3.
# Copyright © 2018 Intelligent Acoustic Power . All rights reserved.
# This python file is used to call the audio hardware to monitor sound environment

# imports
import pyaudio
import wave
import queue
import numpy as np
from scipy import fftpack
from scipy import signal
import argparse


class monitor():
    def __init__(self,pSampleRate,pDataFormat,pChannelNum,pFramesPerBuffer,callBack):
        self.__sampleRate = pSampleRate
        self.__dataFormat = pDataFormat
        self.__channelNum = pChannelNum
        self.__framesPerBuffer = pFramesPerBuffer
        self.__pyAudio = pyaudio.PyAudio()
        self.__callBack = callBack


        self.__stream = self.__pyAudio.open(format = self.__dataFormat,
                                            channels = self.__channelNum,
                                            rate = self.__sampleRate,
                                            input = True,
                                            frames_per_buffer = self.__framesPerBuffer,
                                            stream_callback = self.__callBack)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Standalone micphone test")
    parser.add_argument('-f', '--format', help='data format', type=str, default='Int16', required=True)
    parser.add_argument('-c', '--channel', help='channel number', type=int, default=1, required=True)
    parser.add_argument('-r', '--rate', help='sample rate', type=int, default=44100, required=True)
    parser.add_argument('-i', '--input', help='input switch', type=bool, default=True, required=True)
    parser.add_argument('-b', '--frames', help='frame per buffer', type=int, default=1024, required=True)
    args = parser.parse_args()






