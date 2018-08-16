# -*- coding: utf-8 -*-
# Created by 2h5h on 2018/8/3.
# Copyright © 2018 Intelligent Acoustic Power . All rights reserved.
# This python file is used to call the audio hardware to monitor sound environment

# imports
import pyaudio
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as line
import threading
import queue
import numpy as np
from scipy import fftpack
from scipy import signal
import argparse

CHUNK = 32768
RECORD_SECONDS = 5
data =[]
FFT_LEN = CHUNK/2
frames=[]
counter=1


class Monitor():


    def __init__(self,pSampleRate,pDataFormat,pChannelNum,pFramesPerBuffer):

        self.__sampleRate = pSampleRate
        self.__dataFormat = pDataFormat
        self.__channelNum = pChannelNum
        self.__framesPerBuffer = pFramesPerBuffer
        self.__pyAudio = pyaudio.PyAudio()
        self.__ad_rdy_ev = threading.Event()


        self.audioQueue = queue.Queue()
        self.window = signal.hamming(CHUNK)
        self.realTimeData= np.arange(0, CHUNK, 1)
        self.fftData=[]


        self.stream = self.__pyAudio.open(format = self.__dataFormat,
                                            channels = self.__channelNum,
                                            rate = self.__sampleRate,
                                            input = True,
                                            frames_per_buffer = self.__framesPerBuffer,
                                            stream_callback = self.default_callback)


    def default_callback(self,in_data,frame_count,time_info,status):
        self.audioQueue.put(in_data)
        self.__ad_rdy_ev.set()
        if counter <= 0:
            return (None, pyaudio.paComplete)
        else:
            return (None, pyaudio.paContinue)


    def start(self):
        self.stream.start_stream()
        t = threading.Thread(target=self.read_audio_thead,args=(self.audioQueue,self.stream,self.__ad_rdy_ev))
        t.daemon = True
        t.start()



    def read_audio_thead(self,q, stream, ad_rdy_ev):
        while stream.is_active():
            ad_rdy_ev.wait(timeout=1000)
            if not q.empty():
                # process audio data here
                data = q.get()
                while not q.empty():
                    q.get()
                self.realTimeData = np.frombuffer(data, np.dtype('<i2'))
                self.realTimeData = self.realTimeData/65536
                self.realTimeData = self.realTimeData * self.window
                fft_temp_data = fftpack.fft(self.realTimeData, self.realTimeData.size, overwrite_x=True)
                self.fftData = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]
            ad_rdy_ev.clear()

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.__pyAudio.terminate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Standalone micphone test")
    parser.add_argument('-f', '--format', help='data format', type=str, default='Int16', required=False)
    parser.add_argument('-c', '--channel', help='channel number', type=int, default=1, required=False)
    parser.add_argument('-r', '--rate', help='sample rate', type=int, default=44100, required=False)
    parser.add_argument('-b', '--frames', help='frame per buffer', type=int, default=CHUNK, required=False)
    args = parser.parse_args()


    if args.format =='Int16':
            mFormat = pyaudio.paInt16
    monitor = Monitor(args.rate,mFormat,args.channel,args.frames)

    # Matplotlib
    fig = plt.figure()
    rt_ax = plt.subplot(212, xlim=(0,CHUNK/args.rate), ylim=(-0.01, 0.01))
    fft_ax = plt.subplot(211)
    fft_ax.set_yscale('log')
    fft_ax.set_xscale('log')
    fft_ax.set_xlim(20,20000)
    fft_ax.set_ylim(0.00001, 100)
    rt_ax.set_title("Real Time")
    fft_ax.set_title("FFT Time")
    rt_line = line.Line2D([], [])
    fft_line = line.Line2D([], [])

    rt_x_data = np.arange(0, CHUNK/args.rate, 1/args.rate)
    fft_x_data = np.arange(0, (CHUNK/2+1)/(CHUNK)*args.rate,(1)/(CHUNK)*args.rate)


    def plot_init():
        rt_ax.add_line(rt_line)
        fft_ax.add_line(fft_line)
        return fft_line, rt_line,


    def plot_update(i):
        rt_line.set_xdata(rt_x_data)
        rt_line.set_ydata(monitor.realTimeData)

        fft_line.set_xdata(fft_x_data)
        fft_line.set_ydata(monitor.fftData)
        return fft_line, rt_line,


    ani = animation.FuncAnimation(fig, plot_update,
                                  init_func=plot_init,
                                  blit=True)

    monitor.start()

    plt.show()












