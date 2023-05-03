file= open('images.jpeg','rb')
file1=open('demo.jpeg','wb')
bytes=file.read()

file1.write(bytes)