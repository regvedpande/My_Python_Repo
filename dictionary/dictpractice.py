import random

def random_dictionary_operation():
    """Performs a random operation on a Python dictionary."""

    my_dict = {"apple": 1, "banana": 2, "cherry": 3}
    operations = ["add", "remove", "update", "get"]
    chosen_operation = random.choice(operations)

    if chosen_operation == "add":
        new_key = random.choice(["grape", "orange", "kiwi"])
        new_value = random.randint(4, 10)
        my_dict[new_key] = new_value
        print(f"Added {new_key}: {new_value} to the dictionary.")

    elif chosen_operation == "remove":
        if my_dict: #check if dictionary is not empty.
            removed_key = random.choice(list(my_dict.keys()))
            del my_dict[removed_key]
            print(f"Removed {removed_key} from the dictionary.")
        else:
            print("Dictionary is empty, cannot remove.")

    elif chosen_operation == "update":
        if my_dict: #check if dictionary is not empty.
            updated_key = random.choice(list(my_dict.keys()))
            new_value = random.randint(11, 20)
            my_dict[updated_key] = new_value
            print(f"Updated {updated_key} to {new_value} in the dictionary.")
        else:
            print("Dictionary is empty, cannot update.")

    elif chosen_operation == "get":
        if my_dict: #check if dictionary is not empty.
            get_key = random.choice(list(my_dict.keys()))
            value = my_dict.get(get_key)
            print(f"Value of {get_key} is: {value}")
        else:
            print("Dictionary is empty, cannot get value.")

    print(f"Current dictionary: {my_dict}")

random_dictionary_operation()
