class Generator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):         # next method if generator
        if len(self.data) == self.index:
            raise StopIteration
        a= self.data[self.index]
        self.index = self.index + 1
        return a
         
    
rev = Generator('spam')

print(iter(rev))
for char in rev:
  print(char)
