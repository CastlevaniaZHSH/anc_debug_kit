# -*- coding: utf-8 -*-
# Created by 2h5h on 2018/8/3.
# Copyright © 2018 Intelligent Acoustic Power . All rights reserved.
# This python file is used to call matlab core.

import matplotlib.pyplot as plt
import FxLMS
import matplotlib.lines as line
import numpy as np
import os
import logging

signalsInaGroup = 5

class TFCalculator():
    def __init__(self,folderPath,order,miu):
        self.folderPath = folderPath
        self.order      = order
        self.miu        = miu
        self.result_dict = {}
        filesnames = os.listdir(self.folderPath)
        filesnames.sort()
        if len(filesnames)%signalsInaGroup ==0:
            logging.debug("first judgement pass")
            correct_filename = 0
            for filename in filesnames:
                if filename.index > -1:
                    correct_filename +=1
            if correct_filename == len(filesnames):
                logging.debug("correct files")
                data_list_list = []
                for filename in filesnames:
                    with open(os.path.join(self.folderPath,filename)) as datafile:
                        data_withrn = datafile.readlines()
                        data_list=[]
                        for datasring in data_withrn:
                            data_list.append(float(datasring.strip('\r\n')))
                        data_list_list.append(data_list)
                logging.debug("data read finish")
                self.result_dict = self.calculateTF(filesnames,data_list_list)
            else:
                logging.debug("files wrong")


    def calculateTF(self,filenames,datalistlist):
        groups = len(filenames)/signalsInaGroup
        tf_dict = {}
        for i in range(groups):
            for j in range(groups):
                logging.debug(filenames[i*signalsInaGroup])
                logging.debug(filenames[i*signalsInaGroup+j+1])
                tfname = "tf_"+filenames[i*signalsInaGroup+j+1]
                inp = np.array(datalistlist[i*signalsInaGroup])
                outp = np.array(datalistlist[i*signalsInaGroup+j+1])
                fxlms = FxLMS.FxLMS(input_signal=inp,output_signal=outp,order=self.order,learning_rate=self.miu)
                fxlms.solve()
                (weight,error)=fxlms.getResults()
                tf_dict[tfname] = weight.tolist()
        return tf_dict

    def getResult(self):
        return self.result_dict






if __name__ == '__main__':
    path = '/Users/Vicent/Downloads/ANC_2h5h/anc_debug_kit/Signals'
    plotter = TFCalculator(path, 300)
    dict = plotter.getResult()
    print(dict.keys())

    data = []
    for element in dict['tf_spk4_mic4_output']:
        data.append(element)
    plt.plot(data)
    plt.xlabel("Filter Coefficients")
    plt.ylabel("Coefficients")
    plt.show()