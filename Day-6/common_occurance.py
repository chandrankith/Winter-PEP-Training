'''
Given a string  , whicch is the company name in lowercase letters, your task is to find the top three most common characters in the string.
print the three most common characters along with their occurence count,
sort in descending count is the same, sort the characters in alphabetical order

Input Format:
aabbbccdef

Output Format:
b 3
a 2
c 2
'''

s = input("Enter the string: ")

result = []

for ch in set(s):
    result.append([ch, s.count(ch)])

result.sort(key=lambda x: (-x[1], x[0]))

for i in range(3):
    print(result[i][0], result[i][1])








