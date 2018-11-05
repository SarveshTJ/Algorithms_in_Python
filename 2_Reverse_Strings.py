'''
Problem Statement
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.
For example,
Given s = "the sky is blue",
return "blue is sky the".
'''


# Method 1 (The Traditional Way)
print "*******Method 1 (The Traditional Way)******** "

in_var = input("What's the string? ")

##index = 0
words = []# Will contain all the words
word = ''

for x in in_var:
    if x != ' ':
        word = word + x
    if (x == ' ') or (in_var.rfind(x) == len(in_var) - 1):
        words.append(word)
        word = ''
        continue
    

for index in range(1, len(words)+1):
    print words[-index],



# Method 2 (More Pythonic)
print '\n'
print "*******Method 2 (More Pythonic)******** "

in_var = input()

words = [x for x in in_var.split()]

for index in range(1, len(words)+1):
    print words[-index],
    
