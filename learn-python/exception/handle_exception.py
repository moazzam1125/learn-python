''' Handle exceptions '''


# try-except block

try:
    print(5/0)  # ZeroDevision
except ZeroDivisionError:
    print('try-except handle exception')

# try-except-else block

try:
    ops = "try-except-else handle exception"
except NameError:
    pass
else:
    print(ops)