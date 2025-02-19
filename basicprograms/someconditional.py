import random

num = random.randint(1, 100)

if num % 2 == 0:
    print(f"{num} is even.")
    if num > 50:
        print("It's greater than 50.")
    else:
        print("It's 50 or less.")
else:
    print(f"{num} is odd.")
    if num < 25:
        print("It's less than 25.")
    elif num > 75:
        print("It's greater than 75.")
    else:
        print("It's between 25 and 75.")

color = random.choice(["red", "blue", "green"])

if color == "red":
    print("The color is red.")
elif color == "blue":
    print("The color is blue.")
else:
    print("The color is green.")