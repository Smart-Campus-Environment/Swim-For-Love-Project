import time
import os

class Logger:
	'''Parent class for all logging methods.'''

	def __init__(self, loggerName='default', logType=0):
		'''logType: 0 print only, 1 file only, 2 print and file'''
		self._name = loggerName.strip('_')
		self._logType = logType
		self._LEVELS = {0: 'DEBUG', 1: 'INFO', 2: 'WARNING', 3: 'ERROR', 4: 'CRITICAL'}
		self._COLORS = {'DEBUG': '', 'INFO': '\033[36m', 'WARNING': '\033[93m', 'ERROR': '\033[91m', 'CRITICAL': '\u001b[48;5;9m'}
		self._MSG = '{} ({}) {}\033[1m[{}]\033[0m {}'

	def log(self, level, msg, callback=None):
		'''Base method for all levels of logging.'''
		currentTime = time.strftime('%Y-%m-%d %H:%M:%S')
		level = self._LEVELS.get(level, level)
		if level not in self._LEVELS.values():
			self.warning('Unknown log type: [{}], message: {}'.format(level, msg))
			return -1
		print(self._MSG.format(currentTime, self._name, self._COLORS.get(level, ''), level, msg))
		if level == 'CRITICAL':
			if callback in (0, None):
				pass
			elif callback in (1, 'PAUSE'):
				input('A critical error occurred, the program has paused, press enter to continue.')
			elif callback in (2, 'EXIT'):
				exit()

	def debug(self, msg):
		self.log('DEBUG', msg)

	def info(self, msg):
		self.log('INFO', msg)

	def warning(self, msg):
		self.log('WARNING', msg)

	def error(self, msg):
		self.log('ERROR', msg)

	def critical(self, msg, callback=None):
		self.log('CRITICAL', msg, callback)

def open_url(url):
	os.system('osascript -e \'tell application "Safari" to set the URL of the front document to "{}"\''.format(url))
