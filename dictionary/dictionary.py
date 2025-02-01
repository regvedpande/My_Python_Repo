dic = {
    24 : "Regved",
    22 : "Ayush",
    29 : "Delia",
    28 : "Yogita",
    26 : "Gunjan",
    25 : "Jitu",
    21 : "Sarvesh",
    20 : "Sagar"
}

print(dic[29])

her = {'age' : 29, 'name' : 'Delia', 'city' : 'Bucharest'}
print(her['city'])

for key in her:
    print(her[key])
    
for key, value in her.items():
    print(value)
    
    