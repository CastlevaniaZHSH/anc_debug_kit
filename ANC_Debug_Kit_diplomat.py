#!/usr/bin/env python

############################################################################
# Update history.
# 2017.09.30: Created and test by ShengZhng.
############################################################################
import serial
import time

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
BYTE_UNDEFINED			=	0xFF
BYTE_END				=	0x8C

COMMAND_FORMAT			=[	0xFF,			# COMMAND start Byte
							0x00,			# COMMAND indicator,control
							0x00,			# COMMAND MSB
							0x00,			#
							0x00,			# COMMAND LSB
							0x00,			#
							0x00,			# AMPLITUDE MSB
							0x00,			#
							0x00,			# AMLITUDE	LSB
							0x00,			#
							0xFF,			# FEEQ FR0M MSB
							0xFF,			# FREQ FROM	LSB
							0xFF,			# FREQ IN MSB
							0xFF,			# FREQ IN LSB
							0xFF,			# 4IN1
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
		CON_DATA[OFFS_AMP_LSB-1] = hex(commandIndex)
		CON_DATA[OFFS_AMP_LSB] 	= hex(commandValue	&	0xFF00)
		CON_DATA[OFFS_AMP_LSB+1] = hex(commandValue & 	0x00FF)
		Feedback = self.command(CON_DATA)



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
				received.append(temp)
				temp = self.ser.write(__inputCommand)
			self.ser.close()
		except KeyboardInterrupt:
			self.ser.close()
			raw_input('\nInterrupt by keyboard, press Enter to continue ... ')
			import sys
			sys.exit()
		except:
			self.ser.close()
			raw_input('\n Exception, Press Enter to continue ... ')
		return received

if __name__ == "__main__":
	bs = Diplomat('COM4', 115200, time.localtime())
	bs.command("this is a test afsdsdfaf", "> ft:ok")

