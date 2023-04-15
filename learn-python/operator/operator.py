# Operators OR Whitespace
''' whitespace refers to any nonprinting characters '''


## BASIC Operators

# Newline
'''\n'''

print("Newline\nNewline")

# Tabs
'''\t'''

print("Tab\tTab")

# Alarm
'''\a'''

print("Alarm\a")


# Strip OR Remove extra whitespace
'''strip()'''

strip_str = " STRIP "

print(strip_str.strip()) #Striped
print(strip_str.rstrip()) #Right Strip
print(strip_str.lstrip()) #Left Strip