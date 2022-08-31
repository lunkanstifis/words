def replace_word():

    sentence = "Hi guys, I am Stefan, and hi hi hi hi hi hi"
    print(sentence)
    word_to_replace = input("Enter word to replace: ")
    word_replacement = input("Enter word replacement: ")
    print(sentence.replace(word_to_replace, word_replacement))


replace_word()
