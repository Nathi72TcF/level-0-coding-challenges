vowels = []

def count_vowels(words):
    for letter in words:
        if letter in 'aeiou':
            vowels.append(letter.lower())
            vowel_string = vowels
            print(*vowel_string, sep= '')
        if letter in 'AEIOU':
            vowels.append(letter.lower())
            vowel_string = vowels
            print(*vowel_string, sep='')

count_vowels("BOOT camp")
# count_vowels("Umuzi")
