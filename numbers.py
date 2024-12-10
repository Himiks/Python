import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('My number is: 415-555-4242. And another number: 234-567-899-6789')
for m in mo:
    print('Founded phone number is: ' + m)
