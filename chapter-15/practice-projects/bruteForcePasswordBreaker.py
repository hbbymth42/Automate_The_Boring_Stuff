#! python3
# bruteForcePasswordBreaker.py - Breaks password encryption for PDF Files (Brute-Force Method)

import PyPDF2
from pathlib import Path

dictionaryFile = open(Path.cwd() / 'dictionary.txt')

wordList = dictionaryFile.readlines()

for word in wordList:
    noNewLineWord = word.rstrip('\n')
    pdfReader = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))
    if pdfReader.decrypt(noNewLineWord.upper()) == 0:
        pdfReader = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))
        if pdfReader.decrypt(noNewLineWord.lower()) == 0:
            continue
        else:
            print(f'Password found!: {noNewLineWord.lower()}')
            break
    else:
        print(f'Password found!: {noNewLineWord.upper()}')
        break