#f strings are used to format strings in python and is introduced in python 3.6
details = "Hello my name is {1} and i am {0} years old"
name = "John"
age = 23
# print(details.format(name, age))
# # We get the data in reverse here
# print(details.format(age, name))
print(f"Hello my name is {name} and i am {age} years old")
# Cancel it out
print(f"Hello my name is {{name}} and i am {{age}} years old")
price = 40.88888
print(f"The price of the product is {price:.2f}")
print(f"{2**3}")