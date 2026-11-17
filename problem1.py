def count_vowels_and_consonants(text: str) -> dict:

    counter = {'unli' : 0, 'undosh' : 0}

    VOWELS = 'aeuioAEUIO'

    for letter in text:
       if letter.isalpha():
           if letter in VOWELS:
               counter['unli'] += 1
           else:
               counter['undosh'] += 1
           

    return counter

text = input("Matn kiriting: ")
print(count_vowels_and_consonants(text))
