def list_operations():
    # Create a list
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)

    # Append an element to the list
    my_list.append(6)
    print("List after appending 6:", my_list)

    # Insert an element at a specific position
    my_list.insert(2, 10)
    print("List after inserting 10 at index 2:", my_list)

    # Remove an element from the list
    my_list.remove(3)
    print("List after removing 3:", my_list)

    # Pop an element from the list
    popped_element = my_list.pop()
    print("Popped element:", popped_element)
    print("List after popping an element:", my_list)

    # Reverse the list
    my_list.reverse()
    print("List after reversing:", my_list)

    # Sort the list
    my_list.sort()
    print("List after sorting:", my_list)

# Call the function to perform list operations
list_operations()
