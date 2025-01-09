import time
current_time = time.localtime().tm_hour
if current_time < 12:
    print("Good Morning!")
elif current_time < 17:
    print("Good Afternoon!")
else:
    print("Good Night!")