

class Parser:

	def __init__(self, file_name='input.txt'):
		self.lines = []
		self.data = {}
		self.read_file(file_name)
		self.process_lines()

	def read_file(self, file_name):
		with open(file_name) as f:
			self.lines = f.readlines()

	def process_lines(self):
		try:
			for line in self.lines:
				user, values = line.split('=')
				days = {}
				for value in values.split(','):
					day = value[0:2]
					days[day] = value[2:].strip().replace(':', '').split('-')
				self.data[user] = days
		except Exception as e:
			print('Incorrect File Format')
		

	def get_data(self):
		return self.data


