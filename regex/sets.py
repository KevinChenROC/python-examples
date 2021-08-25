import re

test_string = 'hello 123_'
pattern = re.compile(r'[a-w]')  # match any char from a to w
pattern = re.compile(r'[1-3]')  # match any char from 1 to 3
matches = pattern.finditer(test_string)
for match in matches:
    print(match)


dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

print('all dates with a character in between')
pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

print('only dates with - or . in between')
# no escape for the . here in the set
pattern = re.compile(r'\d\d\d\d[-.]\d\d[-.]\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)

print()
print('only dates with - or . in between in May or June')
pattern = re.compile(r'\d\d\d\d[-.]0[56][-.]\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)

# a dash in a character set specifies a range if it is in between, otherwise the dash itself
print()
print('only dates with - or . in between in May, June, July')
# no escape for the . here in the set
pattern = re.compile(r'\d\d\d\d[-.]0[5-7][-.]\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
