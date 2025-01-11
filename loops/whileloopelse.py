num = int(input("Enter a number: "))
i = 0
while i < num:
    print(i)
    i += 1

else:
    print("Loop completed successfully!")
    
    # Python emulation of do-while loop
    i = 0
    while True:
        print(i)
        i += 1
        if i >= num:
            break