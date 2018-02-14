"""
Practice with defining functinos
lab1.py
Dylan Durand
1/31/2018

"""

def alarm_clock():
	"""

	calculates and outputs the time when the alarm goes off bases 
	on time current time (in hours) and number of hours to wait for the alarm.
	"""
	current_time_string = input("What is the current time (in hours)? ")
	waiting_time_string = input("How many hours do you have to wait? ")

	current_time_int = int(current_time_string)
	waiting_time_int = int(waiting_time_string)

	hours = current_time_int + waiting_time_int	

	timeofday = hours % 24

	"""
	% devides and returns the remainder

	"""

	print(timeofday)

	print('done') 

