# Sample input:
p1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b1 = ['9:00', '20:00']
p2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
b2 = ['10:00', '18:30']
time = 30
# Sample output: ['11:30'. '12:00'], ['15:00'. '16:00], ['18:00'. '18:30'] ... Available Times

def to_minutes(time):
  (hour, minutes) = time.split(':')
  return int(hour) * 60 + int(minutes)

def to_hour_minutes(time):
  hour = time // 60 
  minutes = time % 60
  return str(hour) + ':' + str(minutes)

def get_free_schedule(schedule, boundary, min_time):
  (b1, b2) = boundary
  schedule.append([b2, b2])
  
  curr = [b1, b1]
  curr_index = -1
  
  free_schedule = []
  
  while curr_index < len(schedule) - 1:
    next = schedule[curr_index + 1]
    curr_end, next_start = to_minutes(curr[1]), to_minutes(next[0])
    
    if curr_end < next_start and next_start - curr_end >= min_time:
      free_schedule.append([curr[1], next[0]])
    
    curr_index += 1
    curr = schedule[curr_index]
  
  return free_schedule

def intersect_schedule(schedule1, schedule2, min_time):
  ptr1, ptr2 = 0, 0
  schedule = []
  
  while ptr1 < len(schedule1) and ptr2 < len(schedule2):
    (s1_start, s1_end) = schedule1[ptr1]
    (s2_start, s2_end) = schedule2[ptr2]
    
    intersection_start = max(to_minutes(s1_start), to_minutes(s2_start))
    intersection_end = min(to_minutes(s1_end), to_minutes(s2_end))
    
    if intersection_start < intersection_end and intersection_end - intersection_start >= min_time:
      schedule.append([to_hour_minutes(intersection_start), to_hour_minutes(intersection_end)])
    
    if to_minutes(s1_end) < to_minutes(s2_end):
      ptr1 += 1
    else:
      ptr2 += 1
      
  return schedule

def available_calendar(p1, b1, p2, b2, min_time):
  # find both free times -> get their intersections ✅
  free_time1 = get_free_schedule(p1, b1, min_time)
  free_time2 = get_free_schedule(p2, b2, min_time)
  
  return intersect_schedule(free_time1, free_time2, min_time)
  # merge busy times -> merge minboundary -> get freetime
  
print(available_calendar(p1, b1, p2, b2, time))