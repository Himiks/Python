import re
pattern = re.compile(r'(?i)^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$')
test_sentences = [
    'Alice eats apples.',
    'Bob pets cats.',
    'Carol throws baseballs.',
    'Alice throws Apples.',
    'BOB EATS CATS.',
    'RoboCop eats apples.',
    'ALICE THROWS FOOTBALLS.',
    'Carol eats 7 cats.'
]
for sentence in test_sentences:
    if pattern.match(sentence):
        print(f"Matched: {sentence}")
    else:
        print(f"Did not match: {sentence}")