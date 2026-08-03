word = input("Enter the word: ").lower()
vowels = 0

for char in word:
    if char in "aeiou":
        vowels += 1
print(f"Vowels count: {vowels}")