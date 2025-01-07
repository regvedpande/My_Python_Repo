name = "Regved is my Name"
# String Slicing in Python
print(name[0:6])
print(name[7:9])
print(name[:12])  
# where -6 = len(name)-6 
print(name[3:-6]) 
# where -1 = len(name)-1 and -6 = len(name)-6 = 15:6 = which does not make any sense
# so no result
print(name[-1:-6])

# so, we get the output in these
print(name[-6:-1])

print(len(name))

name = "Harry"
print(name[-4:-2])