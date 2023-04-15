''' Dictionary Nesting '''

# Dictionary in string

dict_str = {
    'sector': 'dictionary in string',
    'variable': 'dictionary',
}
str_nest = dict_str
print(str_nest)

# Dictionary in list

dict_list = {
    'sector': 'dictionary in list',
    'variable': 'dictionary',
}
list_nest = [dict_list]
print(list_nest)

# Dictionary in dictionary

dict0 = {
    'sector': 'Dictionary in Dictionary',
}
dict1 = {
    'variable': 'dictionary',
}
dict_nest = {
    dict1['variable']: dict0['sector']
}
print(dict_nest)