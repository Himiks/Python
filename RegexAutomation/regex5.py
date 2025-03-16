import re
pattern = re.compile(r'^\d{1,3}(?:,\d{3})*$')


test_numbers = [
    '42',
    '1,234',
    '6,368,745',
    '12,34,567',
    '1234'
]


for number in test_numbers:
    if pattern.match(number):
        print(f"Matched: {number}")
    else:
        print(f"Did not match: {number}")