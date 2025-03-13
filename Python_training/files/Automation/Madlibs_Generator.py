with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"
for i, char in enumerate(story): #gives position and element
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1] # slice operation
        words.add(word)
        start_of_word = -1



answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])


print(story)