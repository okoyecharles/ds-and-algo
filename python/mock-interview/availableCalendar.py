# Sample input:
p1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b1 = ['9:00', '20:00']
p2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
b2 = ['10:00', '18:30']
time = 30
# Sample output: ['11:30'. '12:00'], ['15:00'. '16:00], ['18:00'. '18:30'] ... Available Times

# helper functions
def getTimeInMinutes (time):
	h, m = time.split(':')
	time = int(h) * 60 + int(m)
	return time

def compareTimes (time1, time2):
	time1 = getTimeInMinutes(time1) 
	time2 = getTimeInMinutes(time2) 
	
	if time1 < time2: return -1
	elif time1 == time2: return 0
	else: return 1

def isValidTime(start, end, time):
	diff = getTimeInMinutes(end) - getTimeInMinutes(start)
	return diff >= time

# main function
# Time Complexity O (n + m)
# Space Complexity O (n + m)

def availableCalendar (
    schedule1: list[list[str]],
    schedule2: list[list[str]],
    bound1: list[str],
    bound2: list[str],
    time: int
):
	i = 0
	j = 0
	schedule = [] # O(n + m)

	# merge lists (sorted)
	while i < len(schedule1) or j < len(schedule2): # O(n + m)
		s1 = getTimeInMinutes(schedule1[i][0]) if i < len(schedule1) else float('inf')
		s2 = getTimeInMinutes(schedule2[j][0]) if j < len(schedule2) else float('inf')

		if s1 <= s2: 
			schedule.append(schedule1[i])
			i = i + 1
		else:
			schedule.append(schedule2[j])
			j = j + 1


	# combine time bounds
	bound = [None] * 2
	bound[0] = bound1[0] if getTimeInMinutes(bound1[0]) >= getTimeInMinutes(bound2[0]) else bound2[0]				
	bound[1] = bound1[1] if getTimeInMinutes(bound1[1]) <= getTimeInMinutes(bound2[1]) else bound2[1]				

	# combine merged lists
	i = 0

	while i < len(schedule) - 1: # O(n + m)
		s1 = getTimeInMinutes(schedule[i][0])
		e1 = getTimeInMinutes(schedule[i][1])
		s2 = getTimeInMinutes(schedule[i + 1][0])
		e2 = getTimeInMinutes(schedule[i + 1][1])

		if s1 < s2:
			if e1 < s2:
				i = i + 1
			if e1 >= s2 and e1 <= e2:
				schedule[i + 1][0] = schedule[i][0]
				schedule[i] = None
				i = i + 1
			if e1 > e2:
				schedule[i + 1][0] = schedule[i][0]
				schedule[i + 1][1] = schedule[i][1]
				schedule[i] = None
				i = i + 1
		elif s1 >= s2 and s1 <= e2:
			if e1 <= e2:
				schedule[i] = None
				i = i + 1
			if e1 > e2:
				schedule[i + 1][1] = schedule[i][1]
				schedule[i] = None
				i = i + 1
		
	# append bound times to the start and end of the list
	schedule = [[bound[0], bound[0]]] + schedule + [[bound[1], bound[1]]] # Time & Space: O(n + m)			
				
	# generate free times
	availability = [] # O (n + m)
	i = 0
	j = 0

	while i < len(schedule): # O (n + m)
		while i < len(schedule) and schedule[i] == None:
			i = i + 1
		j = i + 1
		while j < len(schedule) and schedule[j] == None:
			j = j + 1
		if i == len(schedule) - 1: break

		start = schedule[i][1]
		end = schedule[j][0]
		if isValidTime(start, end, time):
			availability.append([start, end])
		i = j
	
	print(availability)
	print('done')
			
		
availableCalendar(p1, p2, b1, b2, time)
# 3 hours
