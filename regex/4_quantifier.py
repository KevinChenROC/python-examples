import re
from typing import Pattern

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
