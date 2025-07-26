from datetime import date, datetime
from datetime import timedelta


# Get today's date
today = date.today()
print("Today's date:", today)

# Create a specific date
specific_date = date(1990, 3, 10)
print("Specific date:", specific_date)


print("---------------")
# Get the current date and time
now = datetime.now()
print("Current date and time:", now)

# Create a specific datetime
specific_datetime = datetime(1990, 3, 10, 15, 30)
print("Specific datetime:", specific_datetime)

print("-----------------")
# Calculate the difference between two dates
birth_date = date(2004, 9, 17)
today = date.today()
age_days = (today - birth_date).days
print("Days since birth:", age_days)

# Calculate the difference between two datetimes
birth_datetime = datetime(2004, 9, 17, 23, 30)
now = datetime.now()
age_seconds = (now - birth_datetime).total_seconds()
print("Seconds since birth:", age_seconds)

print("------------------")
# Create a timedelta of 10 days
delta = timedelta(days=10)
print("Timedelta of 10 days:", delta)

# Create a timedelta of 2 hours and 30 minutes
delta = timedelta(hours=2, minutes=30)
print("Timedelta of 2 hours and 30 minutes:", delta)

