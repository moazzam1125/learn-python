''' prompt/user input '''

input("sample input, press enter")

# Another example

example_input = input("another example (y/n):")
while example_input != 'n':
    print("Conditional user-input")
    break

# Store input in variable

store_input = input("store in variable:\n>>> ")
print(store_input)