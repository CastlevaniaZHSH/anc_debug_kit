#!/usr/bin/env python

############################################################################
# Update history.
# 2017.09.30: Created and test by ShengZhng.
############################################################################
import serial
import time
import copy
from serial import STOPBITS_ONE,PARITY_NONE

OFFS_START 			   	=	0
OFFS_4IN1 				=	1
OFFS_AMP_MSB			=	2
OFFS_AMP_LSB			=	5
OFFS_PHASE_MSB			=	6
OFFS_PHASE_LSB			=	9
OFFS_FREQ_FROM_MSB 		=	10
OFFS_FREQ_FROM_LSB 		=	11
OFFS_FREQ_TO_MSB		=	12
OFFS_FREQ_TO_LSB		=	13
OFFS_2IN1				=	14
OFF_END					=	15

BYTE_START				=	0xFF
BYTE_IND				=	0x00
BYTE_COM				=	0x20
BYTE_CON				=	0x40
BYTE_FIN				=	0x80
BYTE_UNDEFINED			=	0xFF
BYTE_END				=	0x8C

COMMAND_FORMAT			=[	0xFF,			# COMMAND start Byte
							0x00,			# COMMAND indicator,control
							0x00,			# COMMAND MSB
							0x00,			#
							0x00,			#
							0x00,			# COMMAND LSB
							0x00,			# AMPLITUDE MSB
							0x00,			#
							0x00,			#
							0x00,			# AMLITUDE	LSB
							0x00,			# FREQ FROm MSB
							0x64,			# FREQ FROM	LSB
							0x00,			# FREQ IN MSB
							0x64,			# FREQ IN LSB
							0x00,			# 4IN1
							0x8C]			# COMMAND END

class Diplomat():
	def __init__(self, __CommPortName, __BaudRateDefine, __Parity,__StopBits):
		self.ser = None
		self.CommPortName 	= __CommPortName
		self.BaudRate 		= __BaudRateDefine
		self.Parity			=	__Parity
		self.StopBits		=	__StopBits

	def sendPara(self,commandIndex,commandValue):
		CON_DATA = COMMAND_FORMAT
		CON_DATA[OFFS_4IN1]		= BYTE_IND
		CON_DATA[OFFS_AMP_LSB] 	= commandIndex & 0x00FF
		CON_DATA[OFFS_PHASE_LSB-1] 	= (commandValue & 0xFF00)>>8
		CON_DATA[OFFS_PHASE_LSB] 	= commandValue & 0x00FF
		Feedback = self.command(CON_DATA)
		print(Feedback)
		tf = False
		if(Feedback!=[] and Feedback[OFFS_4IN1]== BYTE_COM):
			CON_DATA[OFFS_4IN1] = BYTE_CON
			Feedback = self.command(CON_DATA)
			print(Feedback)
			if(Feedback!=[] and Feedback[OFFS_4IN1]== BYTE_FIN):
				print("send successfully")
				tf = True
		return tf

	def command(self, __inputCommand):

		received = []
		try:
			self.ser = serial.Serial(
				port = self.CommPortName,
				baudrate = self.BaudRate,
				parity = self.Parity,
				stopbits = self.StopBits,
				bytesize = serial.EIGHTBITS,
				timeout = 2)
			self.ser.write(__inputCommand)
			temp = self.ser.read()
			while temp!='':
				received.append(ord(temp))
				temp = self.ser.read()
			self.ser.close()
		except KeyboardInterrupt:
			self.ser.close()
		except:
			self.ser.close()
			raw_input('\n Exception, Press Enter to continue ... ')
		return received

if __name__ == "__main__":
	bs =  Diplomat('COM1',9600,PARITY_NONE,STOPBITS_ONE)
	tf  = bs.sendPara(1,int(6553))
	if tf:
		print("send successfully.")
	else:
		print("send faild")

