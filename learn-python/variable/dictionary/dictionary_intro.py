''' key-value pairs '''

sample_dict0 = {'variable': 'dictionary', 'number': 6}
print(sample_dict0)

sample_dict1 = {
    'variable': 'dictionary',
    'number': 6,
}
print(sample_dict1['variable'])

# Add key-value

add_dict = {'sector': 'Adding key-values'}
add_dict['variable'] = 'dictionary'
print(add_dict)

# Modify key-value

modify_dict = {'sector': 'unknown', 'variable': 'dictionary'}
modify_dict['sector'] = 'Modify key-values'
print(modify_dict)

# Deleting key-value

del_key_dict = {'sector': 'Deleting key-values', 'variable': 'dictionary'}
del del_key_dict['variable']
print(del_key_dict)