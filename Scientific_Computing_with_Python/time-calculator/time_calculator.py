def add_time(start, duration, day_week=''):
  start_lst = start[:-3].split(':')
  duration_lst = duration.split(':')
  all_time = [int(i) + int(j) for i, j in zip(start_lst, duration_lst)]
  days = 0
  period = start[-2:]
  if all_time[1] >= 60:
    extra = all_time[1]//60
    all_time[1] = all_time[1]%60
    all_time[0] += extra
    if all_time[0] == 12:
      if 'AM' in period:
        period = 'PM'
    elif 'PM' in period:
      period = 'AM'
      days += 1
  while all_time[0] > 12:
    if 'AM' in period:
      period = 'PM'
    elif 'PM' in period:
      period = 'AM'
      days += 1
    all_time[0] = all_time[0] - 12 
  all_time = [str(i) for i in all_time]
  if int(all_time[1]) < 10:
    all_time[1] = '0' + all_time[1]
  extra_text = ''
  if days == 1:
    extra_text = '(next day)'
  elif days > 1:
    extra_text = '({} days later)'.format(days)
  if day_week != '':
    text_day = ''
    days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    number_of_day = days_week.index(day_week.capitalize()) + days
    text_day = days_week[number_of_day%7] 
    new_time = ':'.join(all_time) + ' {}, {} {}'.format(period, text_day, extra_text)
  else:
      new_time = ':'.join(all_time) +  ' {} {}'.format(period, extra_text)
  return new_time.rstrip()
