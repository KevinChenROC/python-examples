import re

test_string = 'python-engineer.com'
pattern = re.compile(r'\.')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\d')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\s')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\w')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\bhey')
matches = pattern.finditer('heyho hohey')  # ho-hey, ho\nhey are matches!
for match in matches:
    print(match)

print()
pattern = re.compile(r'\Ahello')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'123_\Z')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
