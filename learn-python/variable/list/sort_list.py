''' Sorting a list '''

# Reverse order

rev_list = ['reverse', 'list']
rev_list.reverse()
print(rev_list)

# Permanently Sort a list

perm_sort_list = ['permanently', 'organize']
perm_sort_list.sort()
print(perm_sort_list)
perm_sort_list.sort(reverse=True)   # reverse sort
print(perm_sort_list)

# Temporarily sort

tmp_sort_list = ['temporarily', 'organize']
print(sorted(tmp_sort_list))