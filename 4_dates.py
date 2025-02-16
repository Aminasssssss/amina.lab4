#Write a Python program to calculate two date difference in seconds.
import datetime

date1_str = input("YYYY-MM-DD HH:MM:SS")
date2_str = input("YYYY-MM-DD HH:MM:SS")


date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")


difference = abs(date2 - date1)  
seconds = int(difference.total_seconds())


print(seconds)
