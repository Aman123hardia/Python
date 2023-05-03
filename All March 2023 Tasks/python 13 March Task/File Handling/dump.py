import pickle5 as pickle

def write():
    file = open("binary.dat",'wb')
    x = [1,2,3,4,5]    #data we wrote in file
    print( pickle.dump(x,file))
    file.close()
 
write()

def read():
   file = open("binary.dat",'rb')
   data= pickle.load(file)
   print(data)
   file.close()

read()