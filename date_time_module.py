import datetime
import pytz
import maya


today = datetime.date.today()
print(today)
birthday = datetime.date(1983, 4, 30)
# return an object
print(birthday)
# days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)
# adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today+tdelta)

print(today.month)
# monday = 0, sunday = 6
print(today.weekday())

print(datetime.time(7, 2, 20, 15))
# datetime.date (y,m,d)
# .time (h, m, s, ms)
# .datetime (Y, M, D, h, m, s, ms)

# add 10 hrs to current day
hour_delta = datetime.timedelta(hours=10)

print(datetime.datetime.now()+hour_delta)
#
datetime_tday = datetime.datetime.now(tz=pytz.utc)
datetime_pacific = datetime_tday.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)
# for tz in pytz.all_timezones:
#     print(tz)

# string formatting with dates
# 2019-03-09 -> March 3, 2019
# strftime - f as in formatting
print(datetime_pacific.strftime(' %B %d, %Y'))
# March 3, 2019 -> 2019-03-09
# strptime - p as in parsing
date_time_thing = datetime.datetime.strptime('March 09, 2019', '%B %d, %Y')
print(date_time_thing)

# use Maya - https://github.com/timofurrer/maya

event_start = maya.now()
print(event_start)
event_end = event_start.add(hours=1)
print(event_end)
