import serial

OK = 'OK\r\n'
FAIL = 'FAIL\r\n'

class HC05:
	def __init__(self, port, baudrate):
		self.serial = serial.Serial(port, baudrate)

	def writeline(self, string):
		self.serial.write(string + '\r\n')

	def readline(self):
		return self.serial.readline()

	def test(self):
		self.writeline('AT')
		ret = self.readline()

		if ret == OK:
			return True
		return False

	def reset(self):
		self.writeline('AT+RESET')
		ret = self.readline()

		if ret == OK:
			return True
		return False

	def version(self):
		self.writeline('AT+VERSION?')
		ret = self.readline()

		if not (self.readline() == OK):
			return None
		return ret[9:-2]

	def orgl(self):
		self.writeline('AT+ORGL')

		if self.readline() == OK:
			return True
		return False

	def addr(self):
		self.writeline('AT+ADDR?')
		ret = self.readline()

		if not (self.readline() == OK):
			return None
		return ret[5:-2]

	def getname(self):
		self.writeline('AT+NAME?')
		ret = self.readline()

		if ret == FAIL:
			return None

		if not (self.readline() == OK):
			return None
		return ret[6:-2]

	def setname(self, name):
		self.writeline('AT+NAME=' + name)

		if self.readline() == OK:
			return True
		return False

	def rname(self, address):
		self.writeline('AT+RNAME?' + address)
		ret = self.readline()

		if ret == FAIL:
			return None

		if self.readline() == OK:
			return ret[7:-2]
		return None

	def getrole(self):
		self.writeline('AT+ROLE?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[6:-2]
		return None

	def setrole(self, role):
		self.writeline('AT+ROLE=' + str(role))

		if self.readline() == OK:
			return True
		return False

	def getclass(self):
		self.writeline('AT+CLASS?')
		ret = self.readline()

		if ret == FAIL:
			return None

		if self.readline() == OK:
			return ret[7:-2]
		return None

	def setclass(self, clss):
		self.writeline('AT+CLASS=' + str(clss))

		if self.readline() == OK:
			return True
		return False

	def getiac(self):
		self.writeline('AT+IAC?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[5:-2]
		return None

	def setiac(self, iac):
		self.writeline('AT+IAC=' + str(iac))

		if self.readline() == OK:
			return True
		return False

	def getinqm(self):
		self.writeline('AT+INQM?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[6:-2]
		return None

	def setinqm(self, params):
		self.writeline('AT+INQM=' + str(params[0]) + ',' + str(params[1]) + ',' + str(params[2]))

		if self.readline() == OK:
			return True
		return False

	def getpswd(self):
		self.writeline('AT+PSWD?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[6:-2]
		return None

	def setpswd(self, pswd):
		self.writeline('AT+PSWD=' + str(pswd))

		if self.readline() == OK:
			return True
		return False

	def getuart(self):
		self.writeline('AT+UART?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[6:-2]
		return None

	def setuartparams(self, params):
		self.writeline('AT+UART=' + str(params[0]) + ',' + str(params[1]) + ',' + str(params[2]))

		if self.readline() == OK:
			return True
		return False

	def getcmode(self):
		self.writeline('AT+CMODE?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[7:-2]
		return None

	def setcmode(self, mode):
		self.writeline('AT+CMODE=' + str(mode))

		if self.readline() == OK:
			return True
		return False

	def getbind(self, address):
		self.writeline('AT+BIND?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[6:-2]
		return None

	def setbind(self, address):
		self.writeline('AT+BIND=' + str(address))

		if self.readline() == OK:
			return True
		return False

	def getpolar(self):
		self.writeline('AT+POLAR?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[7:-2]
		return None

	def setpolar(self, params):
		self.writeline('AT+POLAR=' + str(params[0]) + ',' + str(params[1]))

		if self.readline() == OK:
			return True
		return False

	def setsinglepio(self, params):
		self.writeline('AT+PIO=' + str(params[0]) + ',' + str(params[1]))

		if self.readline() == OK:
			return True
		return False

	def setmultiplepio(self, mask):
		self.writeline('AT+MPIO=' + str(mask))

		if self.readline() == OK:
			return True
		return False

	def getmultiplepio(self):
		self.writeline('AT+MPIO?')
		ret = self.readline()

		if self.readline() == OK:
			return ret[6:-2]
		return None
