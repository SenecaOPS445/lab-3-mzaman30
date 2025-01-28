#!/usr/bin/env python3

# Create the global list called "my_list"
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all items in my_list unchanged
    return my_list

def give_first_item():
    # Returns the first item in my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list that includes the first and last items in my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list that includes the second and third items in my_list
    return [my_list[1], my_list[2]]

if __name__ == '__main__':   # This section is the "main block"
    print(give_list())                 # Prints the entire list
    print(give_first_item())           # Prints the first item
    print(give_first_and_last_item())  # Prints the first and last items as a list
    print(give_second_and_third_item())  # Prints the second and third items as a list
