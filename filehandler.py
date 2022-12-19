import json


class FileHandler(object):
	def __init__(self, file):
		self.data = []
		self.file = file

	def read(self, file):
		f = open(file, "r")
		self.data = f.read()
		self.data = json.loads(self.data)
		return self.data
