import os, re

pattern = input("Enter a regex: ")
compiled = re.compile(pattern)

folder = input("Enter a folder in which to search: ")

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        with open(os.path.join(folder, filename), 'r') as file:
            lines = file.readlines()
            print(lines)
            
        for line_num, line in enumerate(lines, start=1):
            if compiled.search(line):
                print(f"Match found in {filename} (Line {line_num}): {line.strip()}")
            
            