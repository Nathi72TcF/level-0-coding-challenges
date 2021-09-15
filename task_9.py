words = input('Enter your words: ' )

def count_vowels():
    for letter in words:
        if letter in 'aeiou':
            print(letter)

count_vowels()