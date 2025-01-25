a = input("Enter a number: ")
print(f"Multiplication table of {a} is:")

try:
   for i in range(1, 11):
    print(f"{int(a)} x {i} = {int(a)*i}") 
except:
    print(f"Error: {e}")