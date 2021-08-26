import re

my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""
pattern = re.compile(r'Mr\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print("\nUsing conditions ")
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)


print()
emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
pattern = re.compile('[a-zA-Z1-9-]+@[a-zA-Z-]+\.[a-zA-Z]+')
pattern = re.compile('[a-zA-Z1-9-]+@[a-zA-Z-]+\.(com|de)')
pattern = re.compile('([a-zA-Z1-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
