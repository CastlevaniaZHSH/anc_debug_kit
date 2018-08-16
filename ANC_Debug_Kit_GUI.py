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

from anc_debug_kit_monitor import Monitor
import wx
import anc_debug_kit_monitor
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as line
import numpy as np
from numpy import arange, sin, pi
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

main_frame = 1000
note_book_main = 1001
reat_time_pannel = 1002
real_time_plt = 1003
real_time_ctl = 1004
real_time_weigting = 1005
dpp_panel = 1006
recompilePanel = 1007
int_for_recomplie = 1008
statusbar_main = 1009


###########################################################################
## Class FrameMain
###########################################################################

class FrameMain(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=main_frame, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1275, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(117, 117, 117))

        SizerMain = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"2h5h", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetForegroundColour(wx.Colour(117, 117, 117))

        SizerMain.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.NoteBookMain = wx.Notebook(self, note_book_main, wx.DefaultPosition, wx.DefaultSize, 0)
        self.RealTimePanel = wx.Panel(self.NoteBookMain, reat_time_pannel, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel141 = wx.Panel(self.RealTimePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        # here
        self.m_panel16 = wx.Panel(self.m_panel141, real_time_plt, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel16.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.testPanel = MonitorPanel(self.m_panel16)

        bSizer12.Add(self.m_panel16, 2, wx.EXPAND | wx.ALL, 25)

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel17 = wx.Panel(self.m_panel141, real_time_ctl, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel17.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"Generic Settings"), wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        m_radioBox31Choices = [u"A-Weight", u"B-Weight", u"C-Weight"]
        self.m_radioBox31 = wx.RadioBox(self.m_panel17, real_time_weigting, u"Weighting method", wx.DefaultPosition,
                                        wx.DefaultSize, m_radioBox31Choices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox31.SetSelection(0)
        bSizer13.Add(self.m_radioBox31, 0, wx.ALL, 0)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Sample points:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer14.Add(self.m_staticText10, 0, wx.ALL, 6)

        m_choice1Choices = [u"1024", u"2048", u"4096", u"8192"]
        self.m_choice1 = wx.Choice(self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(1)
        self.m_choice1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.m_choice1.SetBackgroundColour(wx.Colour(255, 170, 82))

        bSizer14.Add(self.m_choice1, 0, wx.ALL, 5)

        bSizer13.Add(bSizer14, 0, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer13.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer38 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"Realtime Settings"), wx.VERTICAL)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"X Axis"), wx.VERTICAL)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText13 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer17.Add(self.m_staticText13, 0, wx.ALL, 2)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_textCtrl1, 1, wx.ALL, 0)

        self.m_staticText131 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText131.Wrap(-1)
        bSizer17.Add(self.m_staticText131, 0, wx.ALL, 2)

        self.m_textCtrl11 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_textCtrl11, 1, wx.ALL, 0)

        bSizer24.Add(bSizer17, 0, wx.EXPAND, 0)

        sbSizer6.Add(bSizer24, 0, wx.EXPAND, 0)

        sbSizer38.Add(sbSizer6, 0, wx.EXPAND, 0)

        sbSizer61 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"Y Axis"), wx.VERTICAL)

        bSizer241 = wx.BoxSizer(wx.VERTICAL)

        m_radioBox51Choices = [u"Linear", u"Log"]
        self.m_radioBox51 = wx.RadioBox(self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        m_radioBox51Choices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox51.SetSelection(0)
        bSizer241.Add(self.m_radioBox51, 0, wx.BOTTOM, 5)

        bSizer171 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText132 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText132.Wrap(-1)
        bSizer171.Add(self.m_staticText132, 0, wx.ALL, 2)

        self.m_textCtrl12 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer171.Add(self.m_textCtrl12, 1, wx.ALL, 0)

        self.m_staticText1311 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1311.Wrap(-1)
        bSizer171.Add(self.m_staticText1311, 0, wx.ALL, 2)

        self.m_textCtrl111 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer171.Add(self.m_textCtrl111, 1, wx.ALL, 0)

        bSizer241.Add(bSizer171, 0, wx.EXPAND, 0)

        sbSizer61.Add(bSizer241, 0, wx.EXPAND, 0)

        sbSizer38.Add(sbSizer61, 0, wx.EXPAND, 5)

        bSizer13.Add(sbSizer38, 1, wx.EXPAND, 0)

        self.m_staticline2 = wx.StaticLine(self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer13.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer39 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"FFT Settings"), wx.VERTICAL)

        sbSizer62 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"X Axis"), wx.VERTICAL)

        bSizer242 = wx.BoxSizer(wx.VERTICAL)

        m_radioBox52Choices = [u"Linear", u"Log"]
        self.m_radioBox52 = wx.RadioBox(self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        m_radioBox52Choices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox52.SetSelection(0)
        bSizer242.Add(self.m_radioBox52, 0, wx.BOTTOM | wx.TOP, 5)

        bSizer172 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText133 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText133.Wrap(-1)
        bSizer172.Add(self.m_staticText133, 0, wx.ALL, 2)

        self.m_textCtrl13 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer172.Add(self.m_textCtrl13, 1, wx.ALL, 0)

        self.m_staticText1312 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1312.Wrap(-1)
        bSizer172.Add(self.m_staticText1312, 0, wx.ALL, 2)

        self.m_textCtrl112 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer172.Add(self.m_textCtrl112, 1, wx.ALL, 0)

        bSizer242.Add(bSizer172, 0, wx.EXPAND, 0)

        sbSizer62.Add(bSizer242, 0, wx.EXPAND, 0)

        sbSizer39.Add(sbSizer62, 1, wx.EXPAND, 5)

        sbSizer63 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel17, wx.ID_ANY, u"Y Axis"), wx.VERTICAL)

        bSizer243 = wx.BoxSizer(wx.VERTICAL)

        bSizer173 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText134 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Upper Limit:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText134.Wrap(-1)
        bSizer173.Add(self.m_staticText134, 0, wx.ALL, 2)

        self.m_textCtrl14 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer173.Add(self.m_textCtrl14, 1, wx.ALL, 0)

        self.m_staticText1313 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Lower Limit:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1313.Wrap(-1)
        bSizer173.Add(self.m_staticText1313, 0, wx.ALL, 2)

        self.m_textCtrl113 = wx.TextCtrl(self.m_panel17, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer173.Add(self.m_textCtrl113, 1, wx.ALL, 0)

        bSizer243.Add(bSizer173, 0, wx.EXPAND, 0)

        sbSizer63.Add(bSizer243, 0, wx.EXPAND, 0)

        sbSizer39.Add(sbSizer63, 0, wx.EXPAND, 5)

        bSizer13.Add(sbSizer39, 0, wx.EXPAND, 0)

        sbSizer5.Add(bSizer13, 0, wx.EXPAND, 5)

        self.m_panel17.SetSizer(sbSizer5)
        self.m_panel17.Layout()
        sbSizer5.Fit(self.m_panel17)
        bSizer47.Add(self.m_panel17, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel18 = wx.Panel(self.m_panel141, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel18.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer22 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel18, wx.ID_ANY, u"Contol Panel"), wx.VERTICAL)

        bSizer54 = wx.BoxSizer(wx.HORIZONTAL)

        m_radioBox3Choices = [u"ON", u"OFF"]
        self.m_radioBox3 = wx.RadioBox(self.m_panel18, wx.ID_ANY, u"ANC Status", wx.DefaultPosition, wx.DefaultSize,
                                       m_radioBox3Choices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox3.SetSelection(1)
        bSizer54.Add(self.m_radioBox3, 0, wx.ALL, 5)

        sbSizer33 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel18, wx.ID_ANY, u"Extremum"), wx.HORIZONTAL)

        self.m_staticText54 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"96dB@1000Hz", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        sbSizer33.Add(self.m_staticText54, 0, wx.ALL, 0)

        bSizer54.Add(sbSizer33, 1, wx.EXPAND, 0)

        sbSizer22.Add(bSizer54, 1, wx.EXPAND, 5)

        self.m_toggleBtn1 = wx.ToggleButton(self.m_panel18, wx.ID_ANY, u"Toggle Active Noise Cannelling",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_toggleBtn1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        sbSizer22.Add(self.m_toggleBtn1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel18.SetSizer(sbSizer22)
        self.m_panel18.Layout()
        sbSizer22.Fit(self.m_panel18)
        bSizer47.Add(self.m_panel18, 1, wx.EXPAND | wx.ALL, 5)

        bSizer12.Add(bSizer47, 1, wx.EXPAND, 5)

        self.m_panel141.SetSizer(bSizer12)
        self.m_panel141.Layout()
        bSizer12.Fit(self.m_panel141)
        bSizer4.Add(self.m_panel141, 1, wx.EXPAND | wx.ALL, 5)

        self.RealTimePanel.SetSizer(bSizer4)
        self.RealTimePanel.Layout()
        bSizer4.Fit(self.RealTimePanel)
        self.NoteBookMain.AddPage(self.RealTimePanel, u"RealTime Monitor", False)
        self.DataProcessingPanel = wx.Panel(self.NoteBookMain, dpp_panel, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel20 = wx.Panel(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel20, wx.ID_ANY, u"Working DIR"), wx.VERTICAL)

        self.m_dirPicker1 = wx.DirPickerCtrl(self.m_panel20, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                             wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        self.m_dirPicker1.SetForegroundColour(wx.Colour(197, 73, 0))

        sbSizer2.Add(self.m_dirPicker1, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel20.SetSizer(sbSizer2)
        self.m_panel20.Layout()
        sbSizer2.Fit(self.m_panel20)
        bSizer9.Add(self.m_panel20, 0, wx.EXPAND | wx.ALL, 10)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.DataProcessingPanel, wx.ID_ANY, u"Signals"), wx.VERTICAL)

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     m_listBox2Choices, 0)
        self.m_listBox2.SetForegroundColour(wx.Colour(207, 73, 0))

        sbSizer3.Add(self.m_listBox2, 1, wx.EXPAND, 10)

        bSizer10.Add(sbSizer3, 1, wx.EXPAND, 0)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel23 = wx.Panel(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        self.m_panel23.SetBackgroundColour(wx.Colour(255, 170, 82))

        sbSizer25 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel23, wx.ID_ANY, u"Calcuation options"), wx.VERTICAL)

        sbSizer26 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel23, wx.ID_ANY, u"Current parameters"), wx.VERTICAL)

        self.m_staticText44 = wx.StaticText(self.m_panel23, wx.ID_ANY,
                                            u"Current sec-path TF order is 300 and Learning rate is 0.5.",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)
        sbSizer26.Add(self.m_staticText44, 0, wx.ALL, 5)

        sbSizer25.Add(sbSizer26, 1, wx.EXPAND, 5)

        sbSizer261 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel23, wx.ID_ANY, u"define new parameters"), wx.VERTICAL)

        bSizer1732 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1332 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"TF order:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText1332.Wrap(-1)
        bSizer1732.Add(self.m_staticText1332, 0, wx.ALL, 2)

        self.m_textCtrl132 = wx.TextCtrl(self.m_panel23, wx.ID_ANY, u"123", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1732.Add(self.m_textCtrl132, 0, wx.RIGHT, 40)

        self.m_staticText13321 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"Sampling Rate:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticText13321.Wrap(-1)
        bSizer1732.Add(self.m_staticText13321, 0, wx.ALL, 2)

        m_choice2Choices = [u"44.1K", u"48K", u"96K", u"8K", u"2K"]
        self.m_choice2 = wx.Choice(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(4)
        bSizer1732.Add(self.m_choice2, 0, wx.RIGHT, 40)

        self.m_staticText133211 = wx.StaticText(self.m_panel23, wx.ID_ANY, u"Learning Rate:", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText133211.Wrap(-1)
        bSizer1732.Add(self.m_staticText133211, 0, wx.ALL, 2)

        self.m_textCtrl13211 = wx.TextCtrl(self.m_panel23, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1732.Add(self.m_textCtrl13211, 0, wx.ALL, 0)

        sbSizer261.Add(bSizer1732, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sbSizer25.Add(sbSizer261, 1, wx.EXPAND, 5)

        bSizer58 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button2 = wx.Button(self.m_panel23, wx.ID_ANY, u"Calculate new sec-path TF", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizer58.Add(self.m_button2, 0, wx.RIGHT, 50)

        self.m_button21 = wx.Button(self.m_panel23, wx.ID_ANY, u"Generate new .c file", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer58.Add(self.m_button21, 0, wx.ALL, 0)

        sbSizer25.Add(bSizer58, 0, wx.ALL | wx.EXPAND, 10)

        self.m_panel23.SetSizer(sbSizer25)
        self.m_panel23.Layout()
        sbSizer25.Fit(self.m_panel23)
        bSizer11.Add(self.m_panel23, 0, wx.EXPAND | wx.ALL, 20)

        self.m_panel22 = wx.Panel(self.DataProcessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        sbSizer23 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel22, wx.ID_ANY, u"Sec-Path related "), wx.VERTICAL)

        self.m_panel19 = wx.Panel(self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel19.SetBackgroundColour(wx.Colour(255, 255, 255))

        sbSizer23.Add(self.m_panel19, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel22.SetSizer(sbSizer23)
        self.m_panel22.Layout()
        sbSizer23.Fit(self.m_panel22)
        bSizer11.Add(self.m_panel22, 1, wx.ALL | wx.EXPAND, 5)

        bSizer10.Add(bSizer11, 3, wx.EXPAND, 10)

        bSizer9.Add(bSizer10, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT, 10)

        self.DataProcessingPanel.SetSizer(bSizer9)
        self.DataProcessingPanel.Layout()
        bSizer9.Fit(self.DataProcessingPanel)
        self.NoteBookMain.AddPage(self.DataProcessingPanel, u"Data Post Processing", False)
        self.RecompilePanel = wx.Panel(self.NoteBookMain, recompilePanel, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        self.RecompilePanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel11 = wx.Panel(self.RecompilePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel11.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer71 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText8 = wx.StaticText(self.m_panel11, int_for_recomplie, u"Your Project is up to date",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.m_staticText8.SetForegroundColour(wx.Colour(197, 73, 0))

        bSizer71.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        bSizer59 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button3 = wx.Button(self.m_panel11, wx.ID_ANY, u"Recompile", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetDefault()
        bSizer59.Add(self.m_button3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_button31 = wx.Button(self.m_panel11, wx.ID_ANY, u"Burn to target", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button31.SetDefault()
        bSizer59.Add(self.m_button31, 0, wx.ALL, 5)

        bSizer71.Add(bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel131 = wx.Panel(self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel131.SetBackgroundColour(wx.Colour(255, 170, 82))

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap1 = wx.StaticBitmap(self.m_panel131, wx.ID_ANY, wx.Bitmap(u"WechatIMG77.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_bitmap1, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 20)

        sbSizer31 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel131, wx.ID_ANY, u"Complie Output:"), wx.VERTICAL)

        m_listBox3Choices = []
        self.m_listBox3 = wx.ListBox(self.m_panel131, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices,
                                     0)
        sbSizer31.Add(self.m_listBox3, 1, wx.ALL | wx.EXPAND, 50)

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
        self.NoteBookMain.AddPage(self.RecompilePanel, u"Recompile LDR", False)

        SizerMain.Add(self.NoteBookMain, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Powered By Intelligent Acoustic Power\nAll Right Reseved",
                                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(9, 70, 90, 90, False, wx.EmptyString))
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        SizerMain.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(SizerMain)
        self.Layout()
        self.StatusBarMain = self.CreateStatusBar(1, 0, statusbar_main)
        self.StatusBarMain.SetBackgroundColour(wx.Colour(164, 164, 164))

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class TestPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas,1,wx.EXPAND | wx.ALL,)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0,3.0,0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)

class MonitorPanel(wx.Panel):

    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.monitor = Monitor(44100,pyaudio.paInt16,1,32768)
        self.CHUNK = 32768
        self.figure = Figure(figsize=(8,6))
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas,1,wx.EXPAND | wx.ALL,)
        self.SetSizer(self.sizer)
        self.Fit()



        rt_ax = self.figure.add_subplot(211,
                                        xlim=(0, self.CHUNK/44100),
                                        ylim=(-0.01, 0.01),
                                        ylabel = 'Amplitude(V)',
                                        frame_on = True,
                                        autoscale_on = True)

        rt_ax.grid(True,which='both')

        fft_ax = self.figure.add_subplot(212,
                                         xlim = (10, 20000),
                                         ylim = (0.00001, 100),
                                         yscale = 'log',
                                         xscale = 'log',
                                         ylabel = 'Sound Pressure(Pa)',
                                         xlabel = 'Frequency(Hz)'
                                         )
        fft_ax.grid(True,which='both')

        rt_line = line.Line2D([], [],color='#C54900')
        fft_line = line.Line2D([], [],color='#C54900')

        rt_x_data = np.arange(0, self.CHUNK / 44100, 1 / 44100)
        fft_x_data = np.arange(0, (self.CHUNK / 2 + 1) / (self.CHUNK) * 44100, (1) / (self.CHUNK) * 44100)


        def plot_init():
            rt_ax.add_line(rt_line)
            fft_ax.add_line(fft_line)
            return fft_line, rt_line,

        def plot_update(i):
            rt_line.set_xdata(rt_x_data)
            rt_line.set_ydata(self.monitor.realTimeData)

            fft_line.set_xdata(fft_x_data)
            fft_line.set_ydata(self.monitor.fftData)
            return fft_line, rt_line,

        ani = animation.FuncAnimation(self.figure, plot_update,init_func=plot_init,blit=True)
        self.monitor.start()
        self.canvas.draw()


if __name__ == '__main__':
    app = wx.App()
    main_win = FrameMain(None)
    main_win.Show()
    app.MainLoop()
