"""
Write a Python program to display the current date and time.

"""
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time : ")
# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))