''' List Nesting '''

# List in string

list_str = ['list in string', 'list']
str_nest = list_str
print(str_nest)

# List in List

list0 = ['list', 'in']
list1 = ['list']

list_nest = [list0, list1]
print(list_nest)

# List in Dictionary

list_dict0 = ['list', 'dictionary']
list_dict1 = ['in']

dict_nest = {
    'sector': list_dict0[0] + " " + list_dict1[0] + " " + list_dict0[1]
}
print(dict_nest)