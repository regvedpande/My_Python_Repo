num = int(input("Enter a number for the Table: "))
for i in range(10):
    if i > 10:
        continue
    print(num,"x", i + 1, "=", num * (i + 1))
    if(i == 10):
        break
print("Loop completed successfully!")