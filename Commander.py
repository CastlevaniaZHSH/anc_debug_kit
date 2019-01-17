#!/usr/bin/env python

############################################################################
# Update history.
# 2017.09.30: Created and test by David Kang.
############################################################################
import re
import serial
import Queue
import threading
import actrl as ac					#import for print out special color and others.
import ctypes
import time

class Commander():
	def __init__(self, __CommPortName, __BaudRateDefine, __LogTime):
		try:
			self.logBuffer = ""
			self.ser = None
			self.CommPortName = __CommPortName
			self.BaudRate = __BaudRateDefine
			self.isPassed = False
			timeOfLog = __LogTime
			self.LogTestFileName = time.strftime("qfct_test_%Y%m%d_%H%M%S.log", timeOfLog)
			self.LogErrorFileName = time.strftime("qfct_error_%Y%m%d_%H%M%S.log", timeOfLog)
		except:
			pass

	def updateLog(self, resultStrings):
		with open(self.LogTestFileName,"a") as LogFile:
			LogFile.write(self.timeLog + "\nTest item:" + self.testName)
			LogFile.write('\nStatus: '+'PASS' if self.isPassed else 'FAIL')
			LogFile.write('\nCommand sent:  ' + self.commandLog + '\nResult get:\n\t')
			if len(resultStrings) > 0: 
				for each in resultStrings:
					LogFile.write(each + "\n\t")
			else:
				LogFile.write("<<Time out, No result>>")
			LogFile.write("\n\n" + ac.Seprator)

		if not self.isPassed:
			with open(self.LogErrorFileName,"a") as LogFile2:
				LogFile2.write(self.timeLog + "\nTest item:" + self.testName)
				LogFile2.write('\nCommand sent:  ' + self.commandLog + '\nResult get:\n\t')
				if len(resultStrings) > 0: 
					for each in resultStrings:
						LogFile2.write(each + "\n\t")
				else:
					LogFile2.write("<<Time out, No result>>")
				LogFile2.write("\n\n" + ac.Seprator)

				
	def checkResult(self, inputData, checkString, printOut = False):
		if len(inputData) == 0:
			print ac.FAIL, ac.blinking(ac.bold(ac.color(',no return timeout.',ac.CFAIL)))
			return False
		if checkString == "":
			print ac.OK, "No checking result."
			if printOut:
				for each in inputData:
					print each.replace("\n","")
			return True
		match = False
		pattern = re.compile(checkString, re.I|re.M|re.S)
		for eachInput in inputData:
			match = pattern.search(eachInput)
			if (match):
				break
		if match:
			print ac.OK
			if printOut:
				for each in inputData:
					print each.replace("\n","")
		else:
			print ac.FAIL
			for each in inputData:
				print " ".rjust(ac.RJ) + "  ", ac.blinking(ac.bold(ac.color(each.replace("\n",""),ac.CFAIL)))
		return match

	def command(self, __testName, __inputCommand, __checkStrings = "", __printOut = False):
		try:
			self.timeLog = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
			self.commandLog = __inputCommand
			self.testName = __testName
			self.ser = serial.Serial(
				port = self.CommPortName,
				baudrate = self.BaudRate,
				parity = serial.PARITY_NONE,
				stopbits = serial.STOPBITS_ONE,
				bytesize = serial.EIGHTBITS,
				timeout = 2)
			self.ser.write(__inputCommand + "\n")
			print __testName.rjust(ac.RJ) + "  ",
			self.isPassed = False
			outPutStrings = []

			while True:
				received = self.ser.readline()
				if received == "":
					self.ser.close()
					break
				else:
					outPutStrings.append(received.replace("\n",""))

			#Get it all before check result.
			self.isPassed = self.checkResult(outPutStrings, __checkStrings, __printOut)
			self.updateLog(outPutStrings)
			return self.isPassed
		except KeyboardInterrupt:
			self.ser.close()
			raw_input('\nInterrupt by keyboard, press Enter to continue ... ')
			import sys
			sys.exit()
		except:
			self.ser.close()
			raw_input('\n Exception, Press Enter to continue ... ')

	def printResult(self, errTest, pause = True):
		if len(errTest) == 0:
			print ac.bold(ac.color('*** Overall Test Results Pass! ***',ac.COK))
			retVal = True
		else:
			outputString = '*** Overall Test Results Fail! %s'%errTest[0]
			for each in errTest[1:]:
				outputString += ",%s"%each

			print ac.bold(ac.color(outputString +  ' ***',ac.CFAIL))
			retVal = False

		if pause:
			raw_input('\nPress Enter to continue ... ')
		return retVal

if __name__ == "__main__":
	bs = Commander('COM4', 115200, time.localtime())
	bs.command("this is a test afsdsdfaf", "> ft:ok")
	bs.command("TestName1", "quit1", '> ft:ok')
	bs.command("TestName2", "quitsdfsd", '', True)
	bs.command("Quit Test", "quit", '> syscfg:ok.*')

