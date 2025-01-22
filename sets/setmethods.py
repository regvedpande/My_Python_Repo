# Creating two sets with some common and unique elements
set1 = {"Apple", "Banana", "Cherry", 1, 2, 3}
set2 = {"Apple", "Dragon fruit", "Cherry", 3, 4, 5}
print("Set 1:", set1)
print("Set 2:", set2)

# Union methods
print("\n# Union Operations")
print("union():", set1.union(set2))  # Returns new set with all elements
set1.update(set2)  # Updates set1 with elements from set2
print("after update():", set1)

# Reset set1 for next operations
set1 = {"Apple", "Banana", "Cherry", 1, 2, 3}

# Intersection methods
print("\n# Intersection Operations")
print("intersection():", set1.intersection(set2))  # Returns common elements
set1.intersection_update(set2)  # Updates set1 keeping only common elements
print("after intersection_update():", set1)

# Reset set1 for next operations
set1 = {"Apple", "Banana", "Cherry", 1, 2, 3}

# Difference methods
print("\n# Difference Operations")
print("difference():", set1.difference(set2))  # Returns elements only in set1
set1.difference_update(set2)  # Removes elements found in set2 from set1
print("after difference_update():", set1)

# Reset set1 for next operations
set1 = {"Apple", "Banana", "Cherry", 1, 2, 3}

# Symmetric difference methods
print("\n# Symmetric Difference Operations")
print("symmetric_difference():", set1.symmetric_difference(set2))  # Returns elements in either set but not both
set1.symmetric_difference_update(set2)  # Updates set1 with elements in either set but not both
print("after symmetric_difference_update():", set1)

# Additional set methods
print("\n# Other Set Operations")
# Create new sets for testing
set3 = {1, 2, 3}
set4 = {1, 2, 3, 4, 5}

print("isdisjoint():", set3.isdisjoint(set4))  # Returns True if sets have no common elements
print("issubset():", set3.issubset(set4))      # Returns True if set3 is subset of set4
print("issuperset():", set4.issuperset(set3))  # Returns True if set4 is superset of set3

# Other useful methods
test_set = {"Apple", "Banana", "Cherry"}
print("\n# Additional Methods")
print("add():", test_set.add("Date"))          # Adds an element
print("remove():", test_set.remove("Apple"))   # Removes an element (raises error if not found)
print("discard():", test_set.discard("Fig"))   # Removes an element (no error if not found)
print("pop():", test_set.pop())                # Removes and returns an arbitrary element
print("clear():", test_set.clear())            # Removes all elements
