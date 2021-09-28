def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_string = []
    lower_case_string = string.lower()
    for i in lower_case_string:
        if i in vowels:
            vowels_string.append(i)
    duplicates = list(set(vowels_string))
    print(f"Vowels: {', '.join(letter for letter in duplicates[::-1])}") 

count_vowels("BOOT camp")
# count_vowels("Umuzi")
