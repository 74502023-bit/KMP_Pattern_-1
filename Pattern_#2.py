text = """On a quiet night, Sarah walked through the garden, gazing at the endless sky.
The wind felt Soft as it brushed against her face, whispering Tales of distant galaxies.
Along the path, a lantern flickered, reminding her of childhood Adventures spent wishing upon the glowing moon.
In the stillness, she realized that among all the chaos of life, there will always be a Reason to look up — 
a shining reminder that hope never fades."""

letters_to_find = ['S', 'T', 'A', 'R']
results = {}

for letter in letters_to_find:
    indexes = [i for i, char in enumerate(text) if char == letter]
    results[letter] = indexes

for letter, positions in results.items():
    if positions:
        print(f"'{letter}' found at indexes: {positions}")
    else:
        print(f"'{letter}' not found in text.")