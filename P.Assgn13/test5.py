#4


words = input("Input words: ")

words_list = words.split(" ")
words_list.sort()
for words in words_list:
    print(('  ').join(words_list))
