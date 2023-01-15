import math
from collections import Counter

letterFrequency = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 
                    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 
                    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 
                    'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def ceaser(text,p):
    textReturn = ""
    for i in text:
        if i.isalpha():
            textReturn += chr(((ord(i) - p - 65) % 26 + 65))
        else:
            textReturn += i
    return textReturn

def calculate(text):
    total = 0
    c = Counter(text)
    for i in text:
        if not i  == " ":
            total += abs(c.get(i, 0) / len(text) * 100 - letterFrequency[i])
    return total

def funkcja(text):
    (min_roznica, odnaleziony_klucz, returnText) = math.inf, 0, ""
    for i in range(1, 26):
        encrypted = ceaser(text, i)
        total = calculate(encrypted)
        if total < min_roznica:
            min_roznica = total
            odnaleziony_klucz = i
            returnText = encrypted
        print(encrypted, total)
    return min_roznica, odnaleziony_klucz, returnText 

print(funkcja(input("Text: ")))
