# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
for i in range(6):
    print(i)
else:
    print("Loop completed")
  
# The else block will not be executed if the loop is terminated by a break statement.    
for i in range(6):
    print(i)
    if i == 3:
        break
else:
    print("Loop completed")