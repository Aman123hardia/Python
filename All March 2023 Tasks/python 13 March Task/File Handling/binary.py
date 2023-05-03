
byte_arr = [65,66,67,68]
some_bytes = bytearray(byte_arr)
# bytearray() the method returns a byte array object which is an array of given bytes.

print(some_bytes)
immutable_bytes = bytes(some_bytes)
# byte() the method returns immutable bytes object initialized with the given size and data.

with open("my_file.txt", "wb") as binaryFile:  # this method give flexiblity dont need to close file
	binaryFile.write(immutable_bytes)

with open("my_file.txt", "rb") as binaryFile:  # this method give flexiblity dont need to close file
	print(binaryFile.read())