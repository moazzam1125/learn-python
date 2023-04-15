''' Remove items/elements from list OR whole list '''

# Pop item

pop_list = ['item1', 'item2']
last_popped_item = pop_list.pop()      # pop last item
print(last_popped_item)

index_pop_list = ['item1', 'item2', 'item3']
index_popped_item = index_pop_list.pop(1)      # pop specific item by index
print(index_popped_item)

# Remove list items
'''remove by value'''

tmp_remove = ['No data', 'tmp remove']
print(tmp_remove)

tmp_remove.remove('No data')
print(tmp_remove)

# Delete list OR list item
'''del by index'''

tmp_delete = ['tmp list', 'No data']
print(tmp_delete)

del tmp_delete[1]     # deleting item
print(tmp_delete)
#print(tmp_delete[1])    # traceback

del tmp_delete
#print(tmp_delete)    # traceback