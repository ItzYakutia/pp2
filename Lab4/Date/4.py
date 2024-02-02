import datetime, math
now = datetime.datetime.now()
nowwithoutM = (datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, 0))

laterwithoutM = (datetime.datetime(2024, 2, 5, 21, 14, 23, 0))

diff = (laterwithoutM - nowwithoutM)
sec = diff.total_seconds()
print(math.fabs(sec))
    