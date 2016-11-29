import calendar
date = map(int, raw_input().split())
n = calendar.weekday(date[2], date[0], date[1])
if n == 0:
    print "MONDAY"
if n == 1:
    print "TUESDAY"
if n == 2:
    print "WEDNESDAY"
if n == 3:
    print "THURSDAY"
if n == 4:
    print "FRIDAY"
if n == 5:
    print "SATURDAY"
if n == 6:
    print "SUNDAY"
