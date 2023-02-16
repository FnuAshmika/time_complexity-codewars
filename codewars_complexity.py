# You probably know the "like" system from Facebook and other pages. 
#People can "like" blog posts, pictures or other items. 
#We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. 
#It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

"""
O(1) -> Constant
As per my understanding, the time complexity of this function should be "O(1) constant".
There are no for loops. And the 'if' statements are also not iterating through the whole list.
Which means that it is performing a constant number of operations.
"""
def likes(names):
    length = len(names)
    if length == 0:
        return f'no one likes this'
    elif length == 1:
        return f'{names[0]} likes this'
    elif length == 2:
        return f'{names[0]} and {names[1]} like this'
    elif length == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        n = length - 2
        return f'{names[0]}, {names[1]} and {n} others like this'

    
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-35)
# Note: The function accepts an integer and returns an integer.
"""
O(n) -> Linear
The time complexity of this function has to be "O(n) linear".
There is one 'for' loop ,which means an iteration is happening here.
So, here the time will increase by the size of input.
"""
def square_digits(num):
    num_str = str(num)
    result=''
    for n in num_str:
        square = int(n)**2
        result += str(square)
    return int(result)


# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
#  The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
"""
O(n) -> Linear
The time complexity of this function is "O(n) linear".
Althought there are 2 'for' loops but they are at the same indentation level.
So, O(n) + O(n) -> O(n+n) -> O(2n)-> O(n) <- simplify out the constant
Also the 2nd 'for loop' is iterating over a dictionary and membership check on dict or set is O(1) 
So, it should be O(n) + O(1) -> O(n)
"""
def duplicate_count(text):
    char_count= {}
    for c in text.lower():
        if c in char_count:
            char_count[c] +=1
        else:
            char_count[c] = 1
    total_count = 0
    for c in char_count:
        if char_count[c] > 1:
            total_count += 1
    return total_count      

# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
# Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns ["arp", "live", "strong"]
# Example 2:
# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns []
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

"""
O(n^2) -> quadratic	
The time complexity of this function will be "O(n^2) quadratic" I think.
Because it has nested 'for' loops and there are 2 iterations going on. 
"""
def in_array(array1, array2):
    result = []
    #O(n)
    for x in array1:
        #O(n)
        for y in array2:
            if x in y and x not in result:
                result.append(x)
    return sorted(result)