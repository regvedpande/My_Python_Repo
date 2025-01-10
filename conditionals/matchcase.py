num = int(input("Enter a number: "))

match num:
    case 0:
        print("You entered zero.")
    case 1 if num > 0 and num < 2:
        print("You entered one.")
    case 2 if num > 1 and num < 3:
        print("You entered two.")
    case _:
        print("You entered some other number.") 
