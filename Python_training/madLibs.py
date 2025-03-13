

with open('madlibs.txt', 'r') as file:
    content = file.read()
    
placeholders = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

for placeholder in placeholders:
    while placeholder in content:
        replacement = input(f"Enter a {placeholder.lower()}: ")
        content = content.replace(placeholder, replacement, 1)
        
with open('madlibs_done.txt', 'w') as file:
    file.write(content)
