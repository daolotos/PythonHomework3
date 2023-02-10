LetterValues = {}
# English
LetterValues.update(dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1))
LetterValues.update(dict.fromkeys(['D', 'G'], 2))
LetterValues.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
LetterValues.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4))
LetterValues.update(dict.fromkeys(['K'], 5))
LetterValues.update(dict.fromkeys(['J', 'X'], 8))
LetterValues.update(dict.fromkeys(['Q', 'Z'], 10))
# Russian
LetterValues.update(dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1))
LetterValues.update(dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2))
LetterValues.update(dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3))
LetterValues.update(dict.fromkeys(['Й', 'Ы'], 4))
LetterValues.update(dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5))
LetterValues.update(dict.fromkeys(['Ш', 'Э', 'Ю'], 8))
LetterValues.update(dict.fromkeys(['Ф', 'Щ', 'Ъ'], 1))


LetterValues.update(dict.fromkeys(['П', 'Ъ'], 10))

word = input("Type any word: ").upper()


scores = 0
for letter in word:
    scores += LetterValues[letter]

print(f"Scores = {scores}")
