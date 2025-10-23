def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP_search(text, pattern):
    text = text.lower()
    pattern = pattern.lower()
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern
    results = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            results.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results

# Main Program
text = "The dog is barking"
pattern = input("Enter a word to search: ")

positions = KMP_search(text, pattern)

if positions:
    print(f'"{pattern}" word exists!')
    for pos in positions:
        print(f'"{pattern}" word is in index {pos} and ends at {pos + len(pattern) - 1}')
else:
    print(f'"{pattern}" word does NOT exist in the text.')