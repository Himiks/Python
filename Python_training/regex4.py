import re
pattern = re.compile(r'(?i)^[A-Z][a-z]+ Nacomoto')


test_sentences = [
    'Alice Nacomoto.',
    'Bob Nacomoto.',
    'Carol NACOMOTO.',
    'Steve Miels',
    'Mr. Nakamoto',
    'satoshi Nakamoto',
    'Nakamoto',
    'Satoshi nakamoto'
]
for sentence in test_sentences:
    if pattern.match(sentence):
        print(f"Matched: {sentence}")
    else:
        print(f"Did not match: {sentence}")