f = open('data.txt', 'r+')
f.truncate(10)   # truncate is used to delete or clear all data from file at given position 

f = open('data.txt', 'r+')
f.truncate(0) 