import datetime
now = datetime.datetime.now()
print(datetime.datetime(now.year, now.month, now.day, hour=now.hour, minute=now.minute, second=now.second, microsecond=0))
    