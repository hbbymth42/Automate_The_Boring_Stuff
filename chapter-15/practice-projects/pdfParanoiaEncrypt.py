#! python3
# pdfParanoiaEncrypt.py - Encrypt all PDFs in folder

import PyPDF2, os, re

folder = './meetingMinutes'

folder = os.path.abspath(folder)

for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        pdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName, filename), 'rb'))
        if pdfReader.isEncrypted:
            continue
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt('encrypted')
        encryptFilename = str(re.findall('[\w\d]+|[\.]', filename)[0]) + '_encrypted.pdf'
        encryptPdf = open(os.path.join(folderName, encryptFilename) , 'wb')
        pdfWriter.write(encryptPdf)
        encryptPdf.close()
        encryptPdfReader = PyPDF2.PdfFileReader(open(os.path.join(folderName, encryptFilename), 'rb'))
        if encryptPdfReader.isEncrypted:
            os.remove(os.path.join(folderName, filename))
        else:
            print('Not encrypted')