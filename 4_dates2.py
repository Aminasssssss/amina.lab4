import datetime

date1 = datetime.datetime(2024, 2, 10, 12, 30, 0)
date2 = datetime.datetime(2024, 2, 15, 14, 45, 0)

difference = date2 - date1
seconds = difference.total_seconds()


print(int(seconds))
