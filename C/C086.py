def anti_vowel(text):
    vowels = ['a','e','i','o','u','A','I','U','E','O']
    new_text =[]
    for i in text:
        new_text.append(i)
        for j in vowels:
            if i == j:
                new_text.remove(j)
    return ''.join(new_text)

text = input()
print(anti_vowel(text))
