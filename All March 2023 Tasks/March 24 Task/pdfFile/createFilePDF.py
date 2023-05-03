import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader('example.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page

for i in range(len(reader.pages)):
 print(reader.pages[i].extract_text())



