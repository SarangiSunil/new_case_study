def count_vowels_consonants(word):
    vowels = 0
    consonants = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
    return (vowels, consonants)
word = input("Enter a word: ")
vowels, consonants = count_vowels_consonants(word)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
