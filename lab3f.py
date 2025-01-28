#!/usr/bin/env python3

# The global list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends a new item that is the last item + 1
    ordered_list.append(ordered_list[-1] + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all items from ordered_list that are found in items_to_remove
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)  # Print original list
    add_item_to_list(my_list)  # Add items
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # Print list after additions
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specified items
    print(my_list)  # Print list after removals
