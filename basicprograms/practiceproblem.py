import time
t = time.strftime("%H:%M:%S")
gethrs = int(time.strftime("%H"))
if gethrs > 0 and gethrs < 12:
    print("Good Morning")
elif gethrs >= 12 and gethrs < 16:
    print("Good Afternoon")
elif gethrs >= 16 and gethrs < 20:
    print("Good Evening")
else:
    print("Good Night")