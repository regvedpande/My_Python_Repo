a = int(input("Enter a number: "))
if a < 0:
    print("Number is a Negative Number")
elif 0 <= a <= 10:
    print("Number is between 0 and 10")
    if 10 <= a <= 20:
        print("Number is between 10 and 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is a Positive Number")