import keyword
print(keyword.kwlist)

#Checking whether a word is a keyword
word = input("Enter the word: ")
print(keyword.iskeyword(word))