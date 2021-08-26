import re

my_string = "Hello World"
# pattern = re.compile(r'world', re.IGNORECASE)  # No match without I flag
pattern = re.compile(r'((?i)world)')  # No match without I flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
    print(match.groups())

print()
my_string = '''
hello
cool
Hello
'''
# line starts with ...
pattern = re.compile(r'^[a-z]', re.MULTILINE)  # No match without M flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
