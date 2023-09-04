#! python3
# pdfParanoiaDecrypt.py - Decrypt all Encrypted PDFs in folder

import PyPDF2, os, re

folder = './meetingMinutes'

folder = os.path.abspath(folder)

passwordGuess = ''

for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        pdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName, filename), 'rb'))
        if pdfReader.isEncrypted == False:
            continue
        print('Please enter password for this PDF: ')
        passwordGuess = input()
        if pdfReader.decrypt(passwordGuess) == 0:
            print('Incorrect Password, continuing to next PDF')
            continue
        else:
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            decryptFilename = str(re.findall('[\w\d]+|[\.]', filename)[0]) + '_decrypted.pdf'
            decryptPdf = open(os.path.join(folderName, decryptFilename), 'wb')
            pdfWriter.write(decryptPdf)
            decryptPdf.close()
print('Done.')