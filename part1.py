"""
Adding and removing dots

Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""


def add_dots(string):
    return ".".join(list(string))


def remove_dots(string):
    return string.replace(".", "")


print(remove_dots(add_dots("hello")))











"""
All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""


def all_equal(l):
    result = True
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            result = False

    return result


print(all_equal([1, 1, 1, 1]))
print(all_equal([1, 2, 1, 1]))








"""
Anagrams

Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""


def is_anagram(str1, str2):
    str1 = "".join(sorted(str1))
    str2 = "".join(sorted(str2))
    return str1 == str2


print(is_anagram("python", "nohtyp"))
print(is_anagram("python", "JavaScript"))









"""
Capital indexes

Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""


def capital_indexes(string):
    return [i for i, char in enumerate(string) if char.isupper()]


print(capital_indexes("HeLlO"))









"""
Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""


def consecutive_zeros(string):
    string_list = string.split("1")
    for i in string_list:
        if i == "":
            string_list.remove(i)
    result = 0
    for i in string_list:
        if len(i) > result:
            result = len(i)
    return result


print(consecutive_zeros("1000000"))
print(consecutive_zeros("1001101000110"))









"""
Counting syllables
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
"""


def count(string):
    return len(string.split("-"))


print(count("ho-tel-code"))








"""
Double letters

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise
"""


def double_letters(string):
    result = False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            result = True
    return result


print(double_letters("boom"))
print(double_letters("damn!"))

# shorter solution
# using a list comprehension, zip, and any
""" def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])]) """







"""
Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
"""


def flatten(l):
    result = []
    for i in l:
        if type(i) == list:
            for j in i:
                result.append(j)
        else:
            result.append(i)
    return result


print(flatten([[1, 2], [3, 4], 5, 6, 7]))
print(flatten([[1, 2], [3, 4]]))














"""
Middle letter

Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""
"""


def mid(string):
    stringLen = len(string)
    if stringLen % 2 != 0:
        middle_string_index = stringLen // 2
        result = string[middle_string_index]
        return result
    else:
        return ""


print(mid("abc"))

















"""
Min-maxing

Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""


def largest_difference(l):
    largest_number = 0
    smallest_number = l[0]
    for i in l:
        if i > largest_number:
            largest_number = i
        if i < smallest_number:
            smallest_number = i
    return largest_number - smallest_number


print(largest_difference([22, 33, 11, 23, 3982]))
print(largest_difference([1, 2, 3, 4, 5]))














"""
Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.
"""


def palindrome(string):
    return string == string[::-1]


print(palindrome("bob"))
print(palindrome("black"))

















