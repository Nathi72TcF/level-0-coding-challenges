vowels = []

def count_vowels(words):
    for letter in words:
        if letter in 'aeiou':
            vowels.append(letter.lower())
            print(set(vowels))
        if letter in 'AEIOU':
            vowels.append(letter.lower())
            print(set(vowels))

count_vowels("BOOT camp")
# count_vowels("Umuzi")
