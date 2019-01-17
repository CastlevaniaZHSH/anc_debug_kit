# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import pyaudio
import matplotlib
matplotlib.use('WXAgg')

from ANC_Debug_Kit_TFCalculator import TFCalculator
import wx
from ANC_Debug_Kit_Monitor import Monitor
import matplotlib.pyplot as plt
import threading
import matplotlib.animation as animation
import matplotlib.lines as line
import numpy as np
from numpy import arange, sin, pi
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import os
import time

main_frame = 1000
real_time_weigting = 1001
dpp_panel = 1002
recompilePanel = 1003

main_frame_width = 1024
main_frame_height = 768


###########################################################################
##
## Real time monitor varibles
##
###########################################################################

weighting_index = 0
sampling_index = 5
sample_point_choicesChoices = [1024, 2048, 4096, 8192, 16384, 32768]

realTime_x_upper = 0.1
realTime_x_lower = 0
realTime_y_upper = 0.5
realTime_y_lower = -0.5

fft_x_type_index = 0
fft_x_upper = 2000
fft_x_lower = 20
fft_y_upper = 100
fft_y_lower = 0.001

datadist = {}
is_anc_on = False
anc_info = " 100dBA with maximum "

###########################################################################
##
## Real time monitor varibles
##
###########################################################################

sigCal_workingPath = os.getcwd()
sigCal_info = "Current sec-path TF order is 300 and Learning rate is 0.001"
sigCal_learningRate = 0.001
sigCal_TFOrder = 300
sigCal_samplingIndex = 0
conStepSize     = 0.001
conRefSigAMp     = 0.1
conAntiDivFactor = 0.01
conFreq1Mic1W    = 1
conFreq1Mic2W    = 1
conFreq1Mic3W    = 1
conFreq1Mic4W    = 1
conFreq2Mic1W    = 1
conFreq2Mic2W    = 1
conFreq2Mic3W    = 1
conFreq2Mic4W    = 1

###########################################################################
## Class frameMain
###########################################################################

class frameMain(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=main_frame, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(main_frame_width, main_frame_height), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(117, 117, 117))

        mainBoxSizer = wx.BoxSizer(wx.VERTICAL)

        self.textSignature = wx.StaticText(self, wx.ID_ANY, u"2h5h", wx.DefaultPosition, wx.DefaultSize, 0)
        self.textSignature.Wrap(-1)
        self.textSignature.SetForegroundColour(wx.Colour(117, 117, 117))

        mainBoxSizer.Add(self.textSignature, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.notebookMain = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panelRealtime = wx.Panel(self.notebookMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        boxSizerRealtime = wx.BoxSizer(wx.HORIZONTAL)

        self.panelRealtime2 = wx.Panel(self.panelRealtime, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        boxSizerRealtime2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap3 = wx.StaticBitmap(self.panelRealtime2, wx.ID_ANY, wx.Bitmap(u"logo33.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        boxSizerRealtime2.Add(self.m_bitmap3, 0, wx.ALIGN_BOTTOM | wx.BOTTOM, 20)

        self.panelMonitor = wx.Panel(self.panelRealtime2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        self.panelMonitor.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.testPanel = MonitorPanel(self.panelMonitor, widthPixel=main_frame_width, heightPixel=main_frame_height,
                                      rt_xlower = realTime_x_lower, rt_xupper = realTime_x_upper,rt_ylower = realTime_y_lower, rt_yupper = realTime_y_upper,
                                      fft_xlower = fft_x_lower, fft_xupper = fft_x_upper,fft_ylower = fft_y_lower, fft_yupper = fft_y_upper, fftxAxis = 'log')

        boxSizerRealtime2.Add(self.panelMonitor, 16, wx.ALL | wx.EXPAND, 25)

        self.m_notebook7 = wx.Notebook(self.panelRealtime2, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.NB_LEFT)
        self.m_panel34 = wx.Panel(self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerMonitor1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel36 = wx.Panel(self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerMonitor1.Add(self.m_panel36, 1, wx.EXPAND | wx.ALL, 5)

        self.m_monitor_controller1 = wx.Panel(self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.TAB_TRAVERSAL)
        self.m_monitor_controller1.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer51 = wx.StaticBoxSizer(
            wx.StaticBox(self.m_monitor_controller1, wx.ID_ANY, u"Realtime Contol Parameters"), wx.VERTICAL)

        bSizer131 = wx.BoxSizer(wx.VERTICAL)

        sbSizer381 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller1, wx.ID_ANY, u"General Parameters"),
                                       wx.VERTICAL)

        bSizer711 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText53 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Step Size:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText53.Wrap(-1)
        bSizer711.Add(self.m_staticText53, 0, wx.ALL, 2)

        self.conStepSIze = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conStepSize), wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer711.Add(self.conStepSIze, 1, wx.ALL, 0)

        self.m_staticText54 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Ref Sig Amp:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        bSizer711.Add(self.m_staticText54, 0, wx.ALL, 2)

        self.conRefSigAmp = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conRefSigAMp), wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer711.Add(self.conRefSigAmp, 1, wx.ALL, 0)

        self.m_staticText55 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Anti-diverge Factor:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText55.Wrap(-1)
        bSizer711.Add(self.m_staticText55, 0, wx.ALL, 2)

        self.conAntiDivFactor = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conAntiDivFactor), wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer711.Add(self.conAntiDivFactor, 1, wx.ALL, 0)

        sbSizer381.Add(bSizer711, 1, wx.EXPAND, 5)

        bSizer131.Add(sbSizer381, 0, wx.EXPAND, 0)

        self.m_staticline21 = wx.StaticLine(self.m_monitor_controller1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer131.Add(self.m_staticline21, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer391 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller1, wx.ID_ANY, u"Frequency one settings"),
                                       wx.VERTICAL)

        sbSizer621 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller1, wx.ID_ANY, u"Weights"), wx.VERTICAL)

        bSizer2421 = wx.BoxSizer(wx.VERTICAL)

        bSizer1721 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1331 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic1 Weight:",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1331.Wrap(-1)
        bSizer1721.Add(self.m_staticText1331, 0, wx.ALL, 2)

        self.freq1Mic1Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq1Mic1W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer1721.Add(self.freq1Mic1Weight, 1, wx.ALL, 0)

        self.m_staticText13121 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic3 Weight:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13121.Wrap(-1)
        bSizer1721.Add(self.m_staticText13121, 0, wx.ALL, 2)

        self.freq1Mic3Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq1Mic3W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer1721.Add(self.freq1Mic3Weight, 1, wx.ALL, 0)

        bSizer2421.Add(bSizer1721, 0, wx.EXPAND, 0)

        sbSizer621.Add(bSizer2421, 0, wx.EXPAND, 0)

        bSizer2431 = wx.BoxSizer(wx.VERTICAL)

        bSizer1731 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1341 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic2 Weight:",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1341.Wrap(-1)
        bSizer1731.Add(self.m_staticText1341, 0, wx.ALL, 2)

        self.freq1Mic2Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq1Mic2W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer1731.Add(self.freq1Mic2Weight, 1, wx.ALL, 0)

        self.m_staticText13131 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic4 Weight:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13131.Wrap(-1)
        bSizer1731.Add(self.m_staticText13131, 0, wx.ALL, 2)

        self.freq1Mic4Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq1Mic4W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer1731.Add(self.freq1Mic4Weight, 1, wx.ALL, 0)

        bSizer2431.Add(bSizer1731, 0, wx.EXPAND, 0)

        sbSizer621.Add(bSizer2431, 0, wx.EXPAND, 0)

        sbSizer391.Add(sbSizer621, 1, wx.EXPAND, 5)

        bSizer131.Add(sbSizer391, 0, wx.EXPAND, 0)

        self.m_staticline211 = wx.StaticLine(self.m_monitor_controller1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        bSizer131.Add(self.m_staticline211, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer3911 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller1, wx.ID_ANY, u"Frequency two settings"),
                                        wx.VERTICAL)

        sbSizer6211 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller1, wx.ID_ANY, u"Weights"), wx.VERTICAL)

        bSizer24211 = wx.BoxSizer(wx.VERTICAL)

        bSizer17211 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13311 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic1 Weight:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13311.Wrap(-1)
        bSizer17211.Add(self.m_staticText13311, 0, wx.ALL, 2)

        self.freq2Mic1Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq2Mic1W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer17211.Add(self.freq2Mic1Weight, 1, wx.ALL, 0)

        self.m_staticText131211 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic3 Weight:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText131211.Wrap(-1)
        bSizer17211.Add(self.m_staticText131211, 0, wx.ALL, 2)

        self.freq2Mic3Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq2Mic3W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer17211.Add(self.freq2Mic3Weight, 1, wx.ALL, 0)

        bSizer24211.Add(bSizer17211, 0, wx.EXPAND, 0)

        sbSizer6211.Add(bSizer24211, 0, wx.EXPAND, 0)

        bSizer24311 = wx.BoxSizer(wx.VERTICAL)

        bSizer17311 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13411 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic2 Weight:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13411.Wrap(-1)
        bSizer17311.Add(self.m_staticText13411, 0, wx.ALL, 2)

        self.freq2Mic2Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq2Mic2W), wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer17311.Add(self.freq2Mic2Weight, 1, wx.ALL, 0)

        self.m_staticText131311 = wx.StaticText(self.m_monitor_controller1, wx.ID_ANY, u"Mic4 Weight:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText131311.Wrap(-1)
        bSizer17311.Add(self.m_staticText131311, 0, wx.ALL, 2)

        self.freq2Mic4Weight = wx.TextCtrl(self.m_monitor_controller1, wx.ID_ANY, str(conFreq2Mic4W), wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer17311.Add(self.freq2Mic4Weight, 1, wx.ALL, 0)

        bSizer24311.Add(bSizer17311, 0, wx.EXPAND, 0)

        sbSizer6211.Add(bSizer24311, 0, wx.EXPAND, 0)

        sbSizer3911.Add(sbSizer6211, 1, wx.EXPAND, 5)

        bSizer131.Add(sbSizer3911, 1, wx.EXPAND, 5)

        sbSizer51.Add(bSizer131, 0, wx.EXPAND, 5)

        self.m_monitor_controller1.SetSizer(sbSizer51)
        self.m_monitor_controller1.Layout()
        sbSizer51.Fit(self.m_monitor_controller1)
        bSizerMonitor1.Add(self.m_monitor_controller1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel181 = wx.Panel(self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel181.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer221 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel181, wx.ID_ANY, u"Contol Panel"), wx.VERTICAL)

        bSizer541 = wx.BoxSizer(wx.HORIZONTAL)

        anc_status_radio_group1Choices = [u"ON", u"OFF"]
        self.anc_status_radio_group1 = wx.RadioBox(self.m_panel181, wx.ID_ANY, u"ANC Status", wx.DefaultPosition,
                                                   wx.DefaultSize, anc_status_radio_group1Choices, 1,
                                                   wx.RA_SPECIFY_ROWS)
        self.anc_status_radio_group1.SetSelection(1)
        bSizer541.Add(self.anc_status_radio_group1, 0, wx.ALL, 5)

        sbSizer331 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel181, wx.ID_ANY, u"Info"), wx.HORIZONTAL)

        self.conCurrentInfo = wx.TextCtrl(self.m_panel181, wx.ID_ANY, u"dB(a) 90dB ", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        sbSizer331.Add(self.conCurrentInfo, 1, wx.ALL | wx.EXPAND, 0)

        bSizer541.Add(sbSizer331, 1, wx.EXPAND, 0)

        sbSizer221.Add(bSizer541, 1, wx.EXPAND, 5)

        self.anc_toggle_botton1 = wx.ToggleButton(self.m_panel181, wx.ID_ANY, u"Toggle Active Noise Cannelling",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.anc_toggle_botton1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        sbSizer221.Add(self.anc_toggle_botton1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel181.SetSizer(sbSizer221)
        self.m_panel181.Layout()
        sbSizer221.Fit(self.m_panel181)
        bSizerMonitor1.Add(self.m_panel181, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel37 = wx.Panel(self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerMonitor1.Add(self.m_panel37, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel34.SetSizer(bSizerMonitor1)
        self.m_panel34.Layout()
        bSizerMonitor1.Fit(self.m_panel34)
        self.m_notebook7.AddPage(self.m_panel34, u"ENC Control Settings", True)
        self.m_panel33 = wx.Panel(self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerMonitor = wx.BoxSizer(wx.VERTICAL)

        self.m_panel38 = wx.Panel(self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerMonitor.Add(self.m_panel38, 1, wx.EXPAND | wx.ALL, 5)

        self.m_monitor_controller = wx.Panel(self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        self.m_monitor_controller.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"Generic Settings"),
                                     wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        weighting_Radio_groupsChoices = [u"A-Weight", u"B-Weight", u"C-Weight"]
        self.weighting_Radio_groups = wx.RadioBox(self.m_monitor_controller, real_time_weigting, u"Weighting method",
                                                  wx.DefaultPosition, wx.DefaultSize, weighting_Radio_groupsChoices, 1,
                                                  wx.RA_SPECIFY_ROWS)
        self.weighting_Radio_groups.SetSelection(0)
        bSizer13.Add(self.weighting_Radio_groups, 0, wx.ALL, 0)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Sample points:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer14.Add(self.m_staticText10, 0, wx.ALL, 6)

        sample_point_choicesChoices = [u"1024", u"2048", u"4096", u"8192", u"16384", u"32768"]
        self.sample_point_choices = wx.Choice(self.m_monitor_controller, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              sample_point_choicesChoices, 0)
        self.sample_point_choices.SetSelection(sampling_index)
        self.sample_point_choices.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.sample_point_choices.SetBackgroundColour(wx.Colour(255, 170, 82))

        bSizer14.Add(self.sample_point_choices, 0, wx.ALL, 5)

        bSizer13.Add(bSizer14, 0, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self.m_monitor_controller, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer13.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer38 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"Realtime Settings"),
                                      wx.VERTICAL)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"X Axis"), wx.VERTICAL)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer17.Add(self.m_staticText13, 0, wx.ALL, 2)

        self.rtAx_upper_limit = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(realTime_x_upper), wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer17.Add(self.rtAx_upper_limit, 1, wx.ALL, 0)

        self.m_staticText131 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText131.Wrap(-1)
        bSizer17.Add(self.m_staticText131, 0, wx.ALL, 2)

        self.rtAx_lower_limit = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(realTime_x_lower), wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer17.Add(self.rtAx_lower_limit, 1, wx.ALL, 0)

        bSizer24.Add(bSizer17, 0, wx.EXPAND, 0)

        sbSizer6.Add(bSizer24, 0, wx.EXPAND, 0)

        sbSizer38.Add(sbSizer6, 0, wx.EXPAND, 0)

        sbSizer61 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"Y Axis"), wx.VERTICAL)

        bSizer241 = wx.BoxSizer(wx.VERTICAL)

        bSizer171 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText132 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText132.Wrap(-1)
        bSizer171.Add(self.m_staticText132, 0, wx.ALL, 2)

        self.rtAy_upper_limit = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(realTime_y_upper), wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer171.Add(self.rtAy_upper_limit, 1, wx.ALL, 0)

        self.m_staticText1311 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1311.Wrap(-1)
        bSizer171.Add(self.m_staticText1311, 0, wx.ALL, 2)

        self.rtAy_lower_limit = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(realTime_y_lower), wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer171.Add(self.rtAy_lower_limit, 1, wx.ALL, 0)

        bSizer241.Add(bSizer171, 0, wx.EXPAND, 0)

        sbSizer61.Add(bSizer241, 0, wx.EXPAND, 0)

        sbSizer38.Add(sbSizer61, 0, wx.EXPAND, 5)

        bSizer13.Add(sbSizer38, 1, wx.EXPAND, 0)

        self.m_staticline2 = wx.StaticLine(self.m_monitor_controller, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer13.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer39 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"FFT Settings"), wx.VERTICAL)

        sbSizer62 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"X Axis"), wx.VERTICAL)

        bSizer242 = wx.BoxSizer(wx.VERTICAL)

        fft_Ax_log_radio_groupChoices = [u"Linear", u"Log"]
        self.fft_Ax_log_radio_group = wx.RadioBox(self.m_monitor_controller, wx.ID_ANY, wx.EmptyString,
                                                  wx.DefaultPosition, wx.DefaultSize, fft_Ax_log_radio_groupChoices, 1,
                                                  wx.RA_SPECIFY_ROWS)
        self.fft_Ax_log_radio_group.SetSelection(1)
        bSizer242.Add(self.fft_Ax_log_radio_group, 0, wx.BOTTOM | wx.TOP, 5)

        bSizer172 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText133 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText133.Wrap(-1)
        bSizer172.Add(self.m_staticText133, 0, wx.ALL, 2)

        self.fftAx_upper = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(fft_x_upper), wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_PROCESS_ENTER)
        bSizer172.Add(self.fftAx_upper, 1, wx.ALL, 0)

        self.m_staticText1312 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1312.Wrap(-1)
        bSizer172.Add(self.m_staticText1312, 0, wx.ALL, 2)

        self.fftAx_lower = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(fft_x_lower), wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_PROCESS_ENTER)
        bSizer172.Add(self.fftAx_lower, 1, wx.ALL, 0)

        bSizer242.Add(bSizer172, 0, wx.EXPAND, 0)

        sbSizer62.Add(bSizer242, 0, wx.EXPAND, 0)

        sbSizer39.Add(sbSizer62, 1, wx.EXPAND, 5)

        sbSizer63 = wx.StaticBoxSizer(wx.StaticBox(self.m_monitor_controller, wx.ID_ANY, u"Y Axis"), wx.VERTICAL)

        bSizer243 = wx.BoxSizer(wx.VERTICAL)

        bSizer173 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText134 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText134.Wrap(-1)
        bSizer173.Add(self.m_staticText134, 0, wx.ALL, 2)

        self.fftAy_upper = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(fft_y_upper), wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_PROCESS_ENTER)
        bSizer173.Add(self.fftAy_upper, 1, wx.ALL, 0)

        self.m_staticText1313 = wx.StaticText(self.m_monitor_controller, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1313.Wrap(-1)
        bSizer173.Add(self.m_staticText1313, 0, wx.ALL, 2)

        self.fftAy_lower = wx.TextCtrl(self.m_monitor_controller, wx.ID_ANY, str(fft_y_lower), wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer173.Add(self.fftAy_lower, 1, wx.ALL, 0)

        bSizer243.Add(bSizer173, 0, wx.EXPAND, 0)

        sbSizer63.Add(bSizer243, 0, wx.EXPAND, 0)

        sbSizer39.Add(sbSizer63, 0, wx.EXPAND, 5)

        bSizer13.Add(sbSizer39, 0, wx.EXPAND, 0)

        sbSizer5.Add(bSizer13, 0, wx.EXPAND, 5)

        self.m_monitor_controller.SetSizer(sbSizer5)
        self.m_monitor_controller.Layout()
        sbSizer5.Fit(self.m_monitor_controller)
        bSizerMonitor.Add(self.m_monitor_controller, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel39 = wx.Panel(self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerMonitor.Add(self.m_panel39, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel33.SetSizer(bSizerMonitor)
        self.m_panel33.Layout()
        bSizerMonitor.Fit(self.m_panel33)
        self.m_notebook7.AddPage(self.m_panel33, u"Monitor Settings", False)

        boxSizerRealtime2.Add(self.m_notebook7, 9, wx.ALL | wx.EXPAND, 5)

        self.panelRealtime2.SetSizer(boxSizerRealtime2)
        self.panelRealtime2.Layout()
        boxSizerRealtime2.Fit(self.panelRealtime2)
        boxSizerRealtime.Add(self.panelRealtime2, 1, wx.EXPAND | wx.ALL, 0)

        self.panelRealtime.SetSizer(boxSizerRealtime)
        self.panelRealtime.Layout()
        boxSizerRealtime.Fit(self.panelRealtime)
        self.notebookMain.AddPage(self.panelRealtime, u"RealTime Monitor", False)
        self.DataProcessingPanel = wx.Panel(self.notebookMain, dpp_panel, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel20 = wx.Panel(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel20, wx.ID_ANY, u"Working DIR"), wx.VERTICAL)

        self.sig_dialog_picker = wx.DirPickerCtrl(self.m_panel20, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        self.sig_dialog_picker.SetForegroundColour(wx.Colour(197, 73, 0))

        sbSizer2.Add(self.sig_dialog_picker, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel20.SetSizer(sbSizer2)
        self.m_panel20.Layout()
        sbSizer2.Fit(self.m_panel20)
        bSizer9.Add(self.m_panel20, 0, wx.EXPAND | wx.ALL, 10)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap2 = wx.StaticBitmap(self.DataProcessingPanel, wx.ID_ANY,
                                         wx.Bitmap(u"logo33.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_LEFT, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.DataProcessingPanel, wx.ID_ANY, u"Signals"), wx.VERTICAL)

        sig_list_boxChoices = []
        self.sig_list_box = wx.ListBox(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, -1),
                                       sig_list_boxChoices, 0)
        self.sig_list_box.SetForegroundColour(wx.Colour(207, 73, 0))

        sbSizer3.Add(self.sig_list_box, 1, 0, 10)

        bSizer10.Add(sbSizer3, 1, wx.EXPAND, 0)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel23 = wx.Panel(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        self.m_panel23.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer25 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel23, wx.ID_ANY, u"Calcuation options"), wx.VERTICAL)

        sbSizer26 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel23, wx.ID_ANY, u"Current parameters"), wx.VERTICAL)

        self.sig_para_info = wx.TextCtrl(self.m_panel23, wx.ID_ANY,
                                         sigCal_info,
                                         wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        sbSizer26.Add(self.sig_para_info, 1, wx.ALL | wx.EXPAND, 0)

        sbSizer25.Add(sbSizer26, 1, wx.EXPAND, 5)

        sbSizer261 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel23, wx.ID_ANY, u"define new parameters"), wx.VERTICAL)

        bSizer1732 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1332 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"TF order:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1332.Wrap(-1)
        bSizer1732.Add(self.m_staticText1332, 0, wx.ALL, 2)

        self.sig_tf_order = wx.TextCtrl(self.m_panel23, wx.ID_ANY, str(sigCal_TFOrder), wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PROCESS_ENTER)
        bSizer1732.Add(self.sig_tf_order, 0, wx.RIGHT, 20)

        self.m_staticText13321 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"Sampling Rate:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText13321.Wrap(-1)
        bSizer1732.Add(self.m_staticText13321, 0, wx.ALL, 2)

        sig_sampling_rateChoices = [u"44.1K", u"48K", u"96K", u"8K", u"2K"]
        self.sig_sampling_rate = wx.Choice(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           sig_sampling_rateChoices, 0)
        self.sig_sampling_rate.SetSelection(sigCal_samplingIndex)
        bSizer1732.Add(self.sig_sampling_rate, 0, wx.RIGHT, 20)

        self.m_staticText133211 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"Learning Rate:", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText133211.Wrap(-1)
        bSizer1732.Add(self.m_staticText133211, 0, wx.ALL, 2)

        self.sig_learning_rate = wx.TextCtrl(self.m_panel23, wx.ID_ANY, str(sigCal_learningRate), wx.DefaultPosition, wx.DefaultSize,
                                             wx.TE_PROCESS_ENTER)
        bSizer1732.Add(self.sig_learning_rate, 0, wx.ALL, 0)

        sbSizer261.Add(bSizer1732, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sbSizer25.Add(sbSizer261, 1, wx.EXPAND, 5)

        bSizer58 = wx.BoxSizer(wx.HORIZONTAL)

        self.sig_cal_new_tf = wx.Button(self.m_panel23, wx.ID_ANY, u"Calculate new sec-path TF", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer58.Add(self.sig_cal_new_tf, 0, wx.RIGHT, 50)

        self.sig_gen_new_c = wx.Button(self.m_panel23, wx.ID_ANY, u"Generate new .c file", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer58.Add(self.sig_gen_new_c, 0, wx.ALL, 0)

        sbSizer25.Add(bSizer58, 0, wx.ALL | wx.EXPAND, 10)

        self.m_panel23.SetSizer(sbSizer25)
        self.m_panel23.Layout()
        sbSizer25.Fit(self.m_panel23)
        bSizer11.Add(self.m_panel23, 0, wx.EXPAND | wx.ALL, 20)

        self.m_panel22 = wx.Panel(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer23 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel22, wx.ID_ANY, u"Sec-Path related "), wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_notebook2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.speaker_1 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker_1.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        self.speaker1 = wx.Notebook(self.speaker_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_LEFT)
        self.speaker1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.speaker1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.speaker1mic1 = wx.Panel(self.speaker1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker1mic1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker1mic1 = TFPanel(self.speaker1mic1, [], widPixel=main_frame_width,heightPixel=main_frame_height)
        self.speaker1.AddPage(self.speaker1mic1, u"Mic1", False)

        self.speaker1mic2 = wx.Panel(self.speaker1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker1mic2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker1mic2 = TFPanel(self.speaker1mic2, [], widPixel=main_frame_width,heightPixel=main_frame_height)
        self.speaker1.AddPage(self.speaker1mic2, u"Mic2", False)

        self.speaker1mic3 = wx.Panel(self.speaker1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker1mic3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker1mic3 = TFPanel(self.speaker1mic3, [], widPixel=main_frame_width,heightPixel=main_frame_height)
        self.speaker1.AddPage(self.speaker1mic3, u"Mic3", False)

        self.speaker1mic4 = wx.Panel(self.speaker1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker1mic4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker1mic4 = TFPanel(self.speaker1mic4, [], widPixel=main_frame_width,heightPixel=main_frame_height)
        self.speaker1.AddPage(self.speaker1mic4, u"Mic4", False)

        bSizer25.Add(self.speaker1, 1, wx.ALL | wx.EXPAND, 5)

        self.speaker_1.SetSizer(bSizer25)
        self.speaker_1.Layout()
        bSizer25.Fit(self.speaker_1)
        self.m_notebook2.AddPage(self.speaker_1, u"Speaker 1", False)
        self.speaker_2 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer26 = wx.BoxSizer(wx.VERTICAL)

        self.speaker2 = wx.Notebook(self.speaker_2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_LEFT)
        self.speaker2mic1 = wx.Panel(self.speaker2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker2mic1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker2mic1 = TFPanel(self.speaker2mic1, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker2.AddPage(self.speaker2mic1, u"Mic1", False)

        self.speaker2mic2 = wx.Panel(self.speaker2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker2mic2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker2mic2 = TFPanel(self.speaker2mic2, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker2.AddPage(self.speaker2mic2, u"Mic2", False)
        self.speaker2mic3 = wx.Panel(self.speaker2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker2mic3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker2mic3 = TFPanel(self.speaker2mic3, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker2.AddPage(self.speaker2mic3, u"Mic3", False)
        self.speaker2mic4 = wx.Panel(self.speaker2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker2mic4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker2mic4 = TFPanel(self.speaker2mic4, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker2.AddPage(self.speaker2mic4, u"Mic4", False)

        bSizer26.Add(self.speaker2, 1, wx.EXPAND | wx.ALL, 5)

        self.speaker_2.SetSizer(bSizer26)
        self.speaker_2.Layout()
        bSizer26.Fit(self.speaker_2)
        self.m_notebook2.AddPage(self.speaker_2, u"Speaker 2", False)
        self.speaker_3 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer27 = wx.BoxSizer(wx.VERTICAL)

        self.speaker3 = wx.Notebook(self.speaker_3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_LEFT)
        self.speaker3mic1 = wx.Panel(self.speaker3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker3mic1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker3mic1 = TFPanel(self.speaker3mic1, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker3.AddPage(self.speaker3mic1, u"Mic1", False)
        self.speaker3mic2 = wx.Panel(self.speaker3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker3mic2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker3mic2 = TFPanel(self.speaker3mic2, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker3.AddPage(self.speaker3mic2, u"Mic2", False)
        self.speaker3mic3 = wx.Panel(self.speaker3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker3mic3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker3mic3 = TFPanel(self.speaker3mic3, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker3.AddPage(self.speaker3mic3, u"Mic3", False)
        self.speaker3mic4 = wx.Panel(self.speaker3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker3mic4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker3mic4 = TFPanel(self.speaker3mic4, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker3.AddPage(self.speaker3mic4, u"Mic4", False)

        bSizer27.Add(self.speaker3, 1, wx.EXPAND | wx.ALL, 5)

        self.speaker_3.SetSizer(bSizer27)
        self.speaker_3.Layout()
        bSizer27.Fit(self.speaker_3)
        self.m_notebook2.AddPage(self.speaker_3, u"Speaker 3", False)
        self.speaker_4 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.speaker4 = wx.Notebook(self.speaker_4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_LEFT)
        self.speaker4mic1 = wx.Panel(self.speaker4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker4mic1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker4mic1 = TFPanel(self.speaker4mic1, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker4.AddPage(self.speaker4mic1, u"Mic1", False)
        self.speaker4mic2 = wx.Panel(self.speaker4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker4mic2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker4mic2 = TFPanel(self.speaker4mic2, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker4.AddPage(self.speaker4mic2, u"Mic2", False)
        self.speaker4mic3 = wx.Panel(self.speaker4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker4mic3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker4mic3 = TFPanel(self.speaker4mic3, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker4.AddPage(self.speaker4mic3, u"Mic3", False)
        self.speaker4mic4 = wx.Panel(self.speaker4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.speaker4mic4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.tfpicspeaker4mic4 = TFPanel(self.speaker4mic4, [], widPixel=main_frame_width,
                                         heightPixel=main_frame_height)
        self.speaker4.AddPage(self.speaker4mic4, u"Mic4", False)

        bSizer28.Add(self.speaker4, 1, wx.EXPAND | wx.ALL, 5)

        self.speaker_4.SetSizer(bSizer28)
        self.speaker_4.Layout()
        bSizer28.Fit(self.speaker_4)
        self.m_notebook2.AddPage(self.speaker_4, u"Speaker 4", False)

        sbSizer23.Add(self.m_notebook2, 1, wx.ALL | wx.EXPAND, 0)

        self.m_panel22.SetSizer(sbSizer23)
        self.m_panel22.Layout()
        sbSizer23.Fit(self.m_panel22)
        bSizer11.Add(self.m_panel22, 1, wx.ALL | wx.EXPAND, 5)

        bSizer10.Add(bSizer11, 3, wx.EXPAND, 10)

        bSizer9.Add(bSizer10, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT, 10)

        self.DataProcessingPanel.SetSizer(bSizer9)
        self.DataProcessingPanel.Layout()
        bSizer9.Fit(self.DataProcessingPanel)
        self.notebookMain.AddPage(self.DataProcessingPanel, u"Data Post Processing", False)
        self.RecompilePanel = wx.Panel(self.notebookMain, recompilePanel, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        self.RecompilePanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel11 = wx.Panel(self.RecompilePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel11.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer71 = wx.BoxSizer(wx.VERTICAL)

        self.proj_status = wx.StaticText(self.m_panel11, wx.ID_ANY, u"Your Project is up to date", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.proj_status.Wrap(-1)
        self.proj_status.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.proj_status.SetForegroundColour(wx.Colour(197, 73, 0))

        bSizer71.Add(self.proj_status, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        bSizer59 = wx.BoxSizer(wx.HORIZONTAL)

        self.proj_recopile = wx.Button(self.m_panel11, wx.ID_ANY, u"Recompile", wx.DefaultPosition, wx.DefaultSize, 0)
        self.proj_recopile.SetDefault()
        bSizer59.Add(self.proj_recopile, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.proj_burn = wx.Button(self.m_panel11, wx.ID_ANY, u"Burn to target", wx.DefaultPosition, wx.DefaultSize, 0)
        self.proj_burn.SetDefault()
        bSizer59.Add(self.proj_burn, 0, wx.ALL, 5)

        bSizer71.Add(bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel131 = wx.Panel(self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel131.SetBackgroundColour(wx.Colour(255, 170, 82))

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap1 = wx.StaticBitmap(self.m_panel131, wx.ID_ANY, wx.Bitmap(u"logo55.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_bitmap1, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 20)

        sbSizer31 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel131, wx.ID_ANY, u"Complie Output:"), wx.VERTICAL)

        proj_build_infoChoices = []
        self.proj_build_info = wx.ListBox(self.m_panel131, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          proj_build_infoChoices, 0)
        self.proj_build_info.Hide()

        sbSizer31.Add(self.proj_build_info, 1, wx.ALL | wx.EXPAND, 50)

        bSizer81.Add(sbSizer31, 1, wx.ALL | wx.EXPAND, 20)

        self.m_panel131.SetSizer(bSizer81)
        self.m_panel131.Layout()
        bSizer81.Fit(self.m_panel131)
        bSizer71.Add(self.m_panel131, 1, wx.EXPAND | wx.ALL, 0)

        self.m_panel11.SetSizer(bSizer71)
        self.m_panel11.Layout()
        bSizer71.Fit(self.m_panel11)
        bSizer8.Add(self.m_panel11, 6, wx.ALIGN_BOTTOM | wx.ALL | wx.EXPAND, 50)

        self.RecompilePanel.SetSizer(bSizer8)
        self.RecompilePanel.Layout()
        bSizer8.Fit(self.RecompilePanel)
        self.notebookMain.AddPage(self.RecompilePanel, u"Recompile LDR", False)

        mainBoxSizer.Add(self.notebookMain, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Powered By Intelligent Acoustic Power\nAll Right Reseved",
                                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(9, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainBoxSizer.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(mainBoxSizer)
        self.Layout()
        self.status_bar_content = self.CreateStatusBar(1, 0, wx.ID_ANY)
        self.status_bar_content.SetForegroundColour(wx.Colour(255, 170, 82))
        self.status_bar_content.SetBackgroundColour(wx.Colour(164, 164, 164))

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.fressh)
        self.conStepSIze.Bind(wx.EVT_TEXT_ENTER, self.onStepSizeChange)
        self.conRefSigAmp.Bind(wx.EVT_TEXT_ENTER, self.onRefSigAmpChange)
        self.conAntiDivFactor.Bind(wx.EVT_TEXT_ENTER, self.onAntiDiFChange)
        self.freq1Mic1Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq1Mic1WChange)
        self.freq1Mic3Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq1Mic3WChange)
        self.freq1Mic2Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq1Mic2WChange)
        self.freq1Mic4Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq1Mic4WChange)
        self.freq2Mic1Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq2Mic1WChange)
        self.freq2Mic3Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq2Mic3WChange)
        self.freq2Mic2Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq2Mic2WChange)
        self.freq2Mic4Weight.Bind(wx.EVT_TEXT_ENTER, self.onFreq2Mic4WChange)
        self.anc_status_radio_group1.Bind(wx.EVT_RADIOBOX, self.onANCStatusChange)
        self.anc_toggle_botton1.Bind(wx.EVT_TOGGLEBUTTON, self.onANCToggle)
        self.weighting_Radio_groups.Bind(wx.EVT_RADIOBOX, self.OnWeightingChange)
        self.sample_point_choices.Bind(wx.EVT_CHOICE, self.onSamplingPointChange)
        self.rtAx_upper_limit.Bind(wx.EVT_TEXT_ENTER, self.onRTXupperChange)
        self.rtAx_lower_limit.Bind(wx.EVT_TEXT_ENTER, self.onRTXlowerChange)
        self.rtAy_upper_limit.Bind(wx.EVT_TEXT_ENTER, self.onRTYupperChange)
        self.rtAy_lower_limit.Bind(wx.EVT_TEXT_ENTER, self.onRTYlowerChange)
        self.fft_Ax_log_radio_group.Bind(wx.EVT_RADIOBOX, self.onFFTXtypeChange)
        self.fftAx_upper.Bind(wx.EVT_TEXT_ENTER, self.onFFTXupperChange)
        self.fftAx_lower.Bind(wx.EVT_TEXT_ENTER, self.onFFTXlowerChange)
        self.fftAy_upper.Bind(wx.EVT_TEXT_ENTER, self.onFFTYupperChange)
        self.fftAy_lower.Bind(wx.EVT_TEXT_ENTER, self.onFFTYlowerChange)
        self.sig_dialog_picker.Bind(wx.EVT_DIRPICKER_CHANGED, self.onSigFolderSelected)
        self.sig_tf_order.Bind(wx.EVT_TEXT_ENTER, self.onTForderChange)
        self.sig_sampling_rate.Bind(wx.EVT_CHOICE, self.onTFSRChange)
        self.sig_learning_rate.Bind(wx.EVT_TEXT_ENTER, self.onLearningRateChange)
        self.sig_cal_new_tf.Bind(wx.EVT_BUTTON, self.onCalculateNewTF)
        self.sig_gen_new_c.Bind(wx.EVT_BUTTON, self.onGenerateNewC)

    def update_testPanel(self):
        self.testPanel.ani._stop()
        self.testPanel.Destroy()
        time.sleep(1)
        self.testPanel = MonitorPanel(self.panelMonitor,samplingPoints=sample_point_choicesChoices[sampling_index],
                                      widthPixel=main_frame_width, heightPixel=main_frame_height,
                                      rt_xlower=realTime_x_lower, rt_xupper=realTime_x_upper,
                                      rt_ylower=realTime_y_lower, rt_yupper=realTime_y_upper,
                                      fft_xlower=fft_x_lower, fft_xupper=fft_x_upper,
                                      fft_ylower=fft_y_lower, fft_yupper=fft_y_upper, fftxAxis='log')


    def fressh(self, event):
        global main_frame_width
        global main_frame_height
        main_frame_width,main_frame_height = self.GetSize()
        self.update_testPanel()
        if datadist!={}:
            self.updateTFplots()
        event.Skip()

    def getANCIndex(self,anc_on_off):
            return (0 if (anc_on_off) else 1)

    def getFiles(self,dirPath):
        Paths = os.listdir(dirPath)
        filePaths = []
        for p in Paths:
            if os.path.isfile(os.path.join(dirPath,p)):
                filePaths.append(p)
        return filePaths

    def is_digit(self,s):
        if s.count('.') == 1:
            sl = s.split('.')
            left = sl[0]
            right = sl[1]
            if left.startswith('-') and left.count('-') == 1 and right.isdigit():
                lleft = left.split('-')[1]
                if lleft.isdigit():
                    return True
            elif left.isdigit() and right.isdigit():
                return True
        elif (s.isdigit()):
            return True
        else:
            return False

    def printStatus(self,text):
        self.status_bar_content.SetStatusText(text,0)

    # Virtual event handlers, overide them in your derived class

    def onStepSizeChange(self, event):
        temp = self.conStepSIze.GetValue()
        global conStepSize
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp)<=1):
                conStepSize = temp
        self.conStepSIze.SetValue(str(conStepSize))
        self.printStatus("step size->" + str(conStepSize))
        event.Skip()

    def onRefSigAmpChange(self, event):
        temp = self.conRefSigAmp.GetValue()
        global conRefSigAMp
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conRefSigAMp = temp
        self.conRefSigAmp.SetValue(str(conRefSigAMp))
        self.printStatus("Reference Signal Amplitude->" + str(conRefSigAMp))
        event.Skip()

    def onAntiDiFChange(self, event):
        temp = self.conAntiDivFactor.GetValue()
        global conAntiDivFactor
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conAntiDivFactor = temp
        self.conAntiDivFactor.SetValue(str(conAntiDivFactor))
        self.printStatus("Anti diverge factor->" + str(conAntiDivFactor))
        event.Skip()

    def onFreq1Mic1WChange(self, event):
        temp = self.freq1Mic1Weight.GetValue()
        global conFreq1Mic1W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq1Mic1W = temp
        self.freq1Mic1Weight.SetValue(str(conFreq1Mic1W))
        self.printStatus("Frequency one mic 1 weight->" + str(conFreq1Mic1W))
        event.Skip()

    def onFreq1Mic3WChange(self, event):
        temp = self.freq1Mic3Weight.GetValue()
        global conFreq1Mic3W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq1Mic3W = temp
        self.freq1Mic3Weight.SetValue(str(conFreq1Mic3W))
        self.printStatus("Frequency one mic 3 weight->" + str(conFreq1Mic3W))
        event.Skip()

    def onFreq1Mic2WChange(self, event):
        temp = self.freq1Mic2Weight.GetValue()
        global conFreq1Mic2W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq1Mic2W = temp
        self.freq1Mic2Weight.SetValue(str(conFreq1Mic2W))
        self.printStatus("Frequency one mic 2 weight->" + str(conFreq1Mic2W))
        event.Skip()

    def onFreq1Mic4WChange(self, event):
        temp = self.freq1Mic4Weight.GetValue()
        global conFreq1Mic1W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                freq1Mic4Weight = temp
        self.freq1Mic4Weight.SetValue(str(freq1Mic4Weight))
        self.printStatus("Frequency one mic 4 weight->" + str(freq1Mic4Weight))
        event.Skip()

    def onFreq2Mic1WChange(self, event):
        temp = self.freq2Mic1Weight.GetValue()
        global conFreq2Mic1W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq2Mic1W = temp
        self.freq2Mic1Weight.SetValue(str(conFreq2Mic1W))
        self.printStatus("Frequency two mic 1 weight->" + str(conFreq2Mic1W))
        event.Skip()

    def onFreq2Mic3WChange(self, event):
        temp = self.freq2Mic3Weight.GetValue()
        global conFreq2Mic3W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq2Mic3W = temp
        self.freq2Mic3Weight.SetValue(str(conFreq2Mic3W))
        self.printStatus("Frequency two mic 3 weight->" + str(conFreq2Mic3W))
        event.Skip()


    def onFreq2Mic2WChange(self, event):
        temp = self.freq2Mic2Weight.GetValue()
        global conFreq2Mic2W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq2Mic2W = temp
        self.freq2Mic2Weight.SetValue(str(conFreq2Mic2W))
        self.printStatus("Frequency two mic 2 weight->" + str(conFreq2Mic2W))
        event.Skip()

    def onFreq2Mic4WChange(self, event):
        temp = self.freq2Mic4Weight.GetValue()
        global conFreq2Mic4W
        if (self.is_digit(temp)):
            if (float(temp) > 0 and float(temp) <= 1):
                conFreq2Mic4W = temp
        self.freq2Mic4Weight.SetValue(str(conFreq2Mic4W))
        self.printStatus("Frequency two mic 4 weight->" + str(conFreq2Mic4W))
        event.Skip()

    def OnWeightingChange(self, event):
        weighting_index = self.weighting_Radio_groups.GetSelection()
        self.printStatus("weighting index->"+str(weighting_index))
        event.Skip()

    def onSamplingPointChange(self, event):
        global sampling_index
        sampling_index = self.sample_point_choices.GetSelection()
        self.printStatus("sampling_index->"+str(sampling_index))
        self.update_testPanel()
        event.Skip()

    def onRTXupperChange(self, event):
        temp = self.rtAx_upper_limit.GetValue()
        global realTime_x_upper
        if(self.is_digit(temp)):
            if(float(temp) > realTime_x_lower):
                realTime_x_upper = temp
        self.rtAx_upper_limit.SetValue(str(realTime_x_upper))
        realTime_x_upper= float(temp)
        self.printStatus("realTime_x_upper->"+str(realTime_x_upper))
        self.update_testPanel()
        event.Skip()

    def onRTXlowerChange(self, event):
        temp = self.rtAx_lower_limit.GetValue()
        global realTime_x_lower
        if (self.is_digit(temp)):
            if (float(temp) < realTime_x_upper):
                realTime_x_lower = temp
        self.rtAx_lower_limit.SetValue(str(realTime_x_lower))
        realTime_x_lower = float(temp)
        self.printStatus("realTime_x_lower->" + str(realTime_x_lower))
        self.update_testPanel()
        event.Skip()

    def onRTYupperChange(self, event):
        temp = self.rtAy_upper_limit.GetValue()
        global realTime_y_upper
        if (self.is_digit(temp)):
            if (float(temp) > realTime_y_lower):
                realTime_y_upper = temp
        self.rtAy_upper_limit.SetValue(str(realTime_y_upper))
        realTime_y_upper = float(temp)
        self.printStatus("realTime_y_upper->" + str(realTime_y_upper))
        self.update_testPanel()
        event.Skip()

    def onRTYlowerChange(self, event):
        temp = self.rtAy_lower_limit.GetValue()
        global realTime_y_lower
        if (self.is_digit(temp)):
            if (float(temp) < realTime_y_upper):
                realTime_y_lower = temp
        self.rtAy_lower_limit.SetValue(str(realTime_y_lower))
        realTime_y_lower = float(temp)
        self.printStatus("realTime_y_lower->" + str(realTime_y_lower))
        self.update_testPanel()
        event.Skip()

    def onFFTXtypeChange(self, event):
        fft_x_type_index = self.fft_Ax_log_radio_group.GetSelection()
        self.printStatus("fft_x_type_index->" + str(fft_x_type_index))
        self.update_testPanel()
        event.Skip()

    def onFFTXupperChange(self, event):
        temp = self.fftAx_upper.GetValue()
        global fft_x_upper
        if (self.is_digit(temp)):
            if (float(temp) > fft_x_lower):
                fft_x_upper = temp
        self.fftAx_upper.SetValue(str(fft_x_upper))
        self.printStatus("fft_x_upper->" + str(fft_x_upper))
        fft_x_upper = int(temp)
        self.update_testPanel()
        event.Skip()

    def onFFTXlowerChange(self, event):
        temp = self.fftAx_lower.GetValue()
        global fft_x_lower
        if (self.is_digit(temp)):
            if (float(temp) < fft_x_upper):
                fft_x_lower = temp
        self.fftAx_lower.SetValue(str(fft_x_lower))
        self.printStatus("fft_x_lower->" + str(fft_x_lower))
        fft_x_lower = int(temp)
        self.update_testPanel()
        event.Skip()

    def onFFTYupperChange(self, event):
        temp = self.fftAy_upper.GetValue()
        global fft_y_upper
        if (self.is_digit(temp)):
            if (float(temp) > fft_y_lower):
                fft_y_upper = temp
        self.fftAy_upper.SetValue(str(fft_y_upper))
        self.printStatus("fft_y_upper->" + str(fft_y_upper))
        fft_y_upper = float(temp)
        self.update_testPanel()
        event.Skip()

    def onFFTYlowerChange(self, event):
        temp = self.fftAy_lower.GetValue()
        global fft_y_lower
        if (self.is_digit(temp)):
            if (float(temp) < fft_y_upper):
                fft_y_lower = temp
        self.fftAy_lower.SetValue(str(fft_y_lower))
        self.printStatus("fft_y_lower->" + str(fft_y_lower))
        fft_y_lower = float(temp)
        self.update_testPanel()
        event.Skip()

    def onANCStatusChange(self, event):
        event.Skip()

    def onANCToggle(self, event):
        is_anc_on = self.anc_toggle_botton.GetValue()
        self.printStatus("is_anc_on->" + str(is_anc_on))
        self.anc_status_radio_group.SetSelection(self.getANCIndex(is_anc_on))
        print(self.panelMonitor.GetSize())
        event.Skip()

    def onSigFolderSelected(self, event):
        global sigCal_workingPath
        sigCal_workingPath = self.sig_dialog_picker.GetPath()
        self.sig_list_box.Clear()
        self.printStatus("sigCal_workingPath->" + str(sigCal_workingPath))
        filePaths = self.getFiles(sigCal_workingPath)
        fileLength = len(filePaths)
        if (fileLength !=0):
            for i in range(fileLength):
                print(filePaths[i])
                self.sig_list_box.Append(filePaths[i])
        self.start_matlabcal()
        event.Skip()


    def onTForderChange(self, event):
        global sigCal_TFOrder
        sigCal_TFOrder = 300
        temp = self.sig_tf_order.GetValue()
        if(self.is_digit(temp)):
            if(int(temp)>20 and int(temp)<600):
                sigCal_TFOrder = int(temp)
        self.printStatus("sigCal_TFOrder->" + str(sigCal_TFOrder))
        event.Skip()

    def onTFSRChange(self, event):
        sigCal_samplingIndex = self.sig_sampling_rate.GetSelection()
        self.printStatus("sigCal_samplingIndex->" + str(sigCal_samplingIndex))
        event.Skip()

    def onLearningRateChange(self, event):
        global sigCal_learningRate
        sigCal_learningRate = 0.001
        temp = self.sig_learning_rate.GetValue()
        if(self.is_digit(temp)):
            if(float(temp)<1 and float(temp)>0):
                    sigCal_learningRate = float(temp)
        self.printStatus("sigCal_learningRate->" + str(sigCal_learningRate))
        event.Skip()

    def onCalculateNewTF(self, event):
        self.printStatus("Calculating transfer functions")
        self.start_matlabcal()
        self.updateTFplots()
        event.Skip()

    def onGenerateNewC(self, event):
        event.Skip()


    def updateTFplots(self):
        self.printStatus("Updating transfer functions" )
        self.tfpicspeaker1mic1.Destroy()
        self.tfpicspeaker1mic1 = TFPanel(self.speaker1mic1,datadist['tf_spk1_mic1_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker1mic2.Destroy()
        self.tfpicspeaker1mic2 = TFPanel(self.speaker1mic2,datadist['tf_spk1_mic2_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker1mic3.Destroy()
        self.tfpicspeaker1mic3 = TFPanel(self.speaker1mic3,datadist['tf_spk1_mic3_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker1mic4.Destroy()
        self.tfpicspeaker1mic4 = TFPanel(self.speaker1mic4,datadist['tf_spk1_mic4_output'],widPixel=main_frame_width,heightPixel=main_frame_height)



        self.tfpicspeaker2mic1.Destroy()
        self.tfpicspeaker2mic1 = TFPanel(self.speaker2mic1,datadist['tf_spk2_mic1_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker2mic2.Destroy()
        self.tfpicspeaker2mic2 = TFPanel(self.speaker2mic2,datadist['tf_spk2_mic2_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker2mic3.Destroy()
        self.tfpicspeaker2mic3 = TFPanel(self.speaker2mic3,datadist['tf_spk2_mic3_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker2mic4.Destroy()
        self.tfpicspeaker2mic4 = TFPanel(self.speaker2mic4,datadist['tf_spk2_mic4_output'],widPixel=main_frame_width,heightPixel=main_frame_height)



        self.tfpicspeaker3mic1.Destroy()
        self.tfpicspeaker3mic1 = TFPanel(self.speaker3mic1,datadist['tf_spk3_mic1_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker3mic2.Destroy()
        self.tfpicspeaker3mic2 = TFPanel(self.speaker3mic2,datadist['tf_spk3_mic2_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker3mic3.Destroy()
        self.tfpicspeaker3mic3 = TFPanel(self.speaker3mic3,datadist['tf_spk3_mic3_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker3mic4.Destroy()
        self.tfpicspeaker3mic4 = TFPanel(self.speaker3mic4,datadist['tf_spk3_mic4_output'],widPixel=main_frame_width,heightPixel=main_frame_height)




        self.tfpicspeaker4mic1.Destroy()
        self.tfpicspeaker4mic1 = TFPanel(self.speaker4mic1,datadist['tf_spk4_mic1_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker4mic2.Destroy()
        self.tfpicspeaker4mic2 = TFPanel(self.speaker4mic2,datadist['tf_spk4_mic2_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker4mic3.Destroy()
        self.tfpicspeaker4mic3 = TFPanel(self.speaker4mic3,datadist['tf_spk4_mic3_output'],widPixel=main_frame_width,heightPixel=main_frame_height)

        self.tfpicspeaker4mic4.Destroy()
        self.tfpicspeaker4mic4 = TFPanel(self.speaker4mic4,datadist['tf_spk4_mic4_output'],widPixel=main_frame_width,heightPixel=main_frame_height)
        self.printStatus("Transfer functions updated.")


    def matlabTFcal(self,path,order,miu):
        plotter = TFCalculator(path,order,miu)
        global datadist
        datadist = plotter.getResult()
        self.updateTFplots()

    def start_matlabcal(self):
        self.sig_para_info.SetValue("Current sec-path TF order is {order} and Learning rate is {rate}".format(
            order=sigCal_TFOrder, rate=sigCal_learningRate))
        t = threading.Thread(target=self.matlabTFcal, args=(str(sigCal_workingPath), sigCal_TFOrder,sigCal_learningRate))
        t.start()
        # t.setDaemon(True)







class TFPanel(wx.Panel):
    def __init__(self,parent,data,
                 widPixel=1024,
                 heightPixel=768):
        self.data = data if(data!=[]) else [1,2,3,2,1,2,3,4,1,2]
        wx.Panel.__init__(self,parent)
        self.widPixel  = widPixel
        self.heightPixel = heightPixel
        self.figure = Figure(figsize=(self.widPixel/180, self.heightPixel/300))
        self.axes = self.figure.add_subplot(111)
        x = np.arange(0,len(self.data))
        y = np.array(self.data)
        self.axes.plot(x, y,color='#C54900')
        self.axes.grid(True, which='both')
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.ALL | wx.CENTER| wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()


class MonitorPanel(wx.Panel):

    def __init__(self,parent,
                 widthPixel=1024,heightPixel=768,
                 samplingPoints=32768,
                 rt_xlower = 0.0, rt_xupper = 0.5,
                 rt_ylower = -0.5, rt_yupper = 0.5,
                 fft_xlower = 10 ,fft_xupper = 20000,
                 fft_ylower = 0.0001 ,fft_yupper = 100,
                 fftxAxis = 'log' ):

        wx.Panel.__init__(self, parent)
        self.monitor = Monitor (44100, pyaudio.paInt16, 1, samplingPoints)
        self.CHUNK = samplingPoints
        self.figure = Figure(figsize=(widthPixel/200, heightPixel/140))
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.ALL | wx.CENTER)
        self.SetSizer(self.sizer)
        self.Fit()

        rt_ax = self.figure.add_subplot(211,
                                        xlim=(rt_xlower, rt_xupper),
                                        ylim=(rt_ylower, rt_yupper),
                                        ylabel = 'Amplitude(V)',
                                        frame_on= True)

        rt_ax.grid(True, which='both')

        fft_ax = self.figure.add_subplot(212,
                                         xlim=(fft_xlower, fft_xupper),
                                         ylim=(fft_ylower, fft_yupper),
                                         yscale='log',
                                         xscale=fftxAxis,
                                         ylabel='Sound Pressure(Pa)',
                                         xlabel='Frequency(Hz)'
                                         )
        fft_ax.grid(True, which='both')

        rt_line = line.Line2D([], [], color='#C54900')
        fft_line = line.Line2D([], [], color='#C54900')

        rt_x_data = np.arange(0, float(self.CHUNK) / 44100, 1.0 / 44100)
        fft_x_data = np.arange(0, float(self.CHUNK / 2 + 1) / (self.CHUNK) * 44100, (1.0) / (self.CHUNK) * 44100)

        def plot_init():
            rt_ax.add_line(rt_line)
            fft_ax.add_line(fft_line)
            return fft_line, rt_line

        def plot_update(i):
            rt_line.set_xdata(rt_x_data)
            rt_line.set_ydata(self.monitor.realTimeData)

            fft_line.set_xdata(fft_x_data)
            fft_line.set_ydata(self.monitor.fftData)
            return fft_line, rt_line

        self.ani = animation.FuncAnimation(self.figure, plot_update, init_func=plot_init, repeat=False)
        self.monitor.start()
        self.canvas.draw()

    def __del__(self):
        self.ani._stop()
        del self.monitor





if __name__ == '__main__':
    app = wx.App()
    main_win = frameMain(None)
    main_win.Show()
    app.MainLoop()
