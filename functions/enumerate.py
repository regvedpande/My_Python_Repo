a = [23,45,78,92,34]
# index = 0
# for i in a:
#     print(i)
#     if (index == 3):
#         print("You are top of the Class")
#     index += 1

for index, value in enumerate(a):
    print(index, value)
    if (index == 3):
        print("You are top of the Class")