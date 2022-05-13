
class Processor:

	def process_data(self, data):

		result = {}
		# User list to know the ones pending check
		user_list = list(data.keys())

		for user, days in data.items():
			# Remove the user to not check with yourself
			user_list.remove(user)
			# Check with the rest of the users
			for user_to_compare in user_list:
				days_to_compare = data[user_to_compare]

				# Check for each day
				for day, hours in days.items():
					if days_to_compare.get(day):
						if self.compare_times(hours, days_to_compare.get(day)):
							result[user + '-' + user_to_compare] = 1 + result.get(user + '-' + user_to_compare, 0)

		return result


	def compare_times(self, start_time, end_time):
		from1 = int(start_time[0])
		to1 = int(start_time[1])
		from2 = int(end_time[0])
		to2 = int(end_time[1])
		return (from1 < to2) and (to1 > from2)


