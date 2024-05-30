# A function that returns the sum of two numbers.
print("Let's add some numbers!")
print("What is the first number?")
number1 = 4 #input()
print(number1)
print("What is the second number?")
number2 = 6 #input()
print(number2)

sum = int(number1) + int(number2)
print(f'{number1} + {number2} = {sum}')

print()
# A function that takes a list of srings, and returns a string that is all those strings concatenated together.
# Can do this two ways:  easy way
my_list = ['all', 'good', 'boys', 'do', 'fine']
join_my_list = "".join(my_list)
print(join_my_list)
#pr
join2_my_list = "*".join(my_list)
print(join2_my_list)
# The longer way
join3_my_list = ""
for string in my_list:
    join3_my_list += string
    #to add a hyphen
    if string != my_list[-1]:
        join3_my_list += "-"
print(join3_my_list)

print()
# A function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element.
original_list = [1, 4, 7, 2, 5]
new_list = ""
for num in original_list:
    new_list = original_list[::2]
print(new_list)

print()
# A function that determines the index of the 3rd occurrence of a given character in a string. 
def find_char_nth(string, char, n):
    times = string.find(char)
    while times >= 0 and n > 1:
        times = string.find(char, times + 1)
        if times == -1:
            return None
        n -= 1
    return times
my_string = 'axbxcdxex'
char_string = 'x'
char_string2 = 'b'
third_occurrence = find_char_nth(my_string, char_string, 3)
third_occurrence2 = find_char_nth(my_string, char_string2, 3)
print(f"The index of the third {char_string} is: {third_occurrence}")
print(f"The index of the third {char_string2} is: {third_occurrence2}")

def find_nth(haystack: str, needle: str, n: int) -> int:
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    if start == -1:
        return None
    return start

result = find_nth("foofoofoofoo", "bee", 2)
result2 = find_nth("foofoofoofoo", "foo", 2)
print(result)
print(result2)

print()
# A function that takes two lists of numbers and returns the result of merging the lists.

from itertools import chain, zip_longest

def merge_lists_even_odd(x, y):
    return list(filter(lambda elem: elem != '', chain.from_iterable(zip_longest(x, y, fillvalue='-'))))

x = [1, 2, 3]
y = [4, 5, 6, 7, 9]
result = merge_lists_even_odd(x, y)
print(result)