# Truthiness

print(True)
print(False)

print()

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string

print(make_longer("abc", True))
print(make_longer("xyz", False))

print()

def is_digit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False
    
print(is_digit("5"))
print(is_digit("a"))

print()

value = True

if value is True:
    print("It's true!")
elif value is False:
    print("It's false!")
else:
    print("It's not true or false!")

print()

num = 5

if num < 10:
    print("small number")
else:
    print("large number")

print()

def is_small(number):
    return number < 10   # evaluates to False if >x 10

num = 15   

if is_small(num):
    print("small number")   # True
else:
    print("large number")   # False

print()

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()
num = 5
print(num < 10 and num > 3)
print(num < 10 and num < 6)
print(num > 10 and num < 6)
print((num > 10) and (num < 3)) # prevents confustion

print()

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()
num = 5
print(num < 10 or num > 3)
print((num < 10) or (num > 6))
print((num > 10) or (num < 6))
print((num > 10) or (num < 3))

print()

print(not True)
print(not False)
print()
value = 3
is_even = (value % 2 == 0)

print(is_even)
print(not is_even)

print()

print(False and len(None))

print()

name = "JOE"
if name != None and name.isupper():
    print(f"Hi, {name}.")
else:
    print("Hello whoever you are.")

print()

num = 5 
if num:
    print("valid number")  # this is truthy any non-zero number
else:
    print("error!")

num = 0
if num:
    print("valid number")
else:
    print("error!")        # this is falsy

print(num == True)

name = input("What is your name?  ")
if name:
    print(f"Hi {name}.")
else:
    print("you must enter your name!")

print()   # code above is strongly discouraged by most style guides
# use below code instead

name = input("What is your name? ")
if name == "":
    print("You must enter your name!")
else:
    print(f"Hi {name}!")
    