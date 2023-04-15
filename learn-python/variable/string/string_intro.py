''' A string is simply a series of characters '''

sample_str = "string value"
print(sample_str)

# Length of string

print(len(sample_str))

# Count values in string by value

count_str = "count, count, count values"
print(count_str.count('count'))

# Split value of string
''' seperate string in parts where finds a space '''

spl_value = "Split value of string"
print(spl_value.split())

# Delete a string

tmp_str = "delete string"
print(tmp_str)

del tmp_str
#print(tmp_str)     # traceback

### Apendix

# Quotes

correct0 = "Moazzam's repositry"
print(correct0)
#invalid0 = 'Moazzam's repositry'
#print(invalid0)    # traceback

# int() to str()

correct1 = int(125)
print("correct1 is " + str(correct1))
#print(print("correct1 is " + correct1)     # traceback