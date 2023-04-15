''' String Nesting '''

# String in string

str0 = ("string")
str_in_str = ("in")

str_nest = str0 + " " + str_in_str + " " + str0
print(str_nest)

# String in List

str_list0 = ('string')
str_list1 = ('list')

list_nest = [str_list0, str_list1]
print(list_nest)

# String in Dictionary

str_dict = ('sector')
str_dict1 = ('string in dicttionary')

dictt_nest = {
    str_dict: str_dict1
}
print(dictt_nest)