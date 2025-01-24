performance = {234: 78, 345: 89, 456: 90, 888: 78}
anotherperformance = {233: 78, 349: 89, 459: 90, 889: 78}

# update() method is used to update the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.
performance.update(anotherperformance)
print(performance)

# clear() method is used to remove all the elements from the dictionary.
performance.clear()
print(performance)

# pop() method is used to remove the element with the specified key from the dictionary.
performance.pop(345)
print(performance)

# popitem() method is used to remove the last inserted item from the dictionary.
performance.popitem()
print(performance)

# del keyword is used to delete the dictionary object.
# del performance
# del performance[234]

# copy() method is used to return a shallow copy of the dictionary.
performance = {234: 78, 345: 89, 456: 90, 888: 78}
anotherperformance = performance.copy()
print(anotherperformance)

