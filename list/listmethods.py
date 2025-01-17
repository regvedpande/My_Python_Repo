# Initialize our list with numbers
items = [11, 44, 1, 4, 6, 9, 6, 8]

# append() adds an element to the end of the list
items.append(10)
print("After append:", items)

# sort() arranges elements in ascending order
items.sort()
print("After sorting:", items)

# sort(reverse=True) arranges elements in descending order
items.sort(reverse=True)
print("After reverse sorting:", items)

# index() returns the position of first occurrence of specified value
print("Index of 6:", items.index(6))

# count() returns number of times a value appears in the list
print("Count of 6:", items.count(6))

# insert() adds element at specified position
items.insert(2, 7)
print("After inserting 7 at index 2:", items)

# Additional useful list methods:

# remove() removes first occurrence of specified value
items.remove(6)
print("After removing first 6:", items)

# pop() removes and returns element at specified index (or last element if no index given)
popped_item = items.pop()
print("Popped item:", popped_item)
print("After pop:", items)

# extend() adds elements from another list
items.extend([2, 3])
print("After extending:", items)

# reverse() reverses the list in-place
items.reverse()
print("After reversing:", items)

# clear() removes all elements from the list
items.clear()
print("After clearing:", items)