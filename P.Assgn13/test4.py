
#3


words = input("Input words: ")

words_list = words.split(",")
words_list.sort()
print(((', ').join(words_list))[::-1])


