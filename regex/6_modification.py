import re


#===============Basic usage of sub and split==================
my_string = 'abc123ABCDEF123abc'
pattern = re.compile(r'123')  # no escape for the . here in the set
matches = pattern.split(my_string)
print(matches)

my_string = "hello world, you are the best world"
pattern = re.compile(r'world')
subbed_string = pattern.sub(r'planet', my_string)
print(subbed_string)


#===============Advanced Example==================
rls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern = re.compile(r'https?://(www\.)?(\w|-)+\.\w+')
pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    #print(match)
    print(match.group())  # 0
    #print(match.group(1))
    #print(match.group(2))
    print(match.group(3))

# substitute using back references to replace url + domain name
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
