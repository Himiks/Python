def replace_word():

    string = "Hi guys, I am himik, and hi hi hi hi"
    word_to_replace = input("Enter a word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    new_word = string.replace(word_to_replace, word_replacement)
    print(new_word)


replace_word()