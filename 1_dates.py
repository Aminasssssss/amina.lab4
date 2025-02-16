import datetime 
today = datetime.date.today()
five_days_ago = today - datetime.timedelta(days=5)

print(today)
print(five_days_ago)