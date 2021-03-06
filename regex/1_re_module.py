# from enum import Flag
import re

my_string = '123ABC123abc\n123abc\n'
# # mutiple line matching, starting from the last line.
match = re.search(r"abc$", my_string, re.M)

# # Single string matching
# match = re.search(r"abc$", my_string),
print(match)
print()

# # finditer()
my_string = 'abc123ABC123abc'
pattern = re.compile(r'123')  # r"123" is a raw string
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group())  # returns the string


print()
# findall()
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print(match)

print()

# match
match = pattern.match(my_string)
print(match)  # return None, because match looks at the beginning of the string

pattern = re.compile(r'abc')
match = pattern.match(my_string)
print(match)


print()
# search
pattern = re.compile(r'123')
match = pattern.search(my_string)
print(match)
