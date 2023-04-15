''' A list is a collection of item in a particular order '''

sample_list = ['item1', 'item2', 'item3']
print(sample_list)

# Length of List

print(len(sample_list))

# Add item in list

append_list = ['item1', 'item2']
append_list.append('item3 appended')     # Adds to end of list
print(append_list)

# Insert item in list

insert_list = ['item1', 'item3']
insert_list.insert(1, 'item2 inserted')    # insert by index
print(insert_list)

# Modify item in list

modify_list = ['item0']
modify_list[0] = 'item1 modified'
print(modify_list)
# prevent modify, [:] makes a copy of the list