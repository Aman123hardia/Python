import random

def shuffle(*string):
  data=random.shuffle(string)
  return ' '.join(string[0])

uppercase=[]
for i in range(5):
 uppercase.append(chr(random.randint(65,90)))

password = shuffle(uppercase)

print(password)


