#Write a Python program to drop microseconds from datetime.
import datetime
now = datetime.datetime.now()
without_microseconds = now.replace(microsecond=0)

print(now)
print(without_microseconds)