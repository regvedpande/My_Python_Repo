fav = ["regved", 25, "delia", 28, "ayush", 20]
print(fav[1:-1])
#Jump Index
print(fav[1:-1:2])

#list comprehension
i = [3, 5, 8 , 9]
print([i for i in range(10)])
print([i*i for i in range(10) if i%2==0])