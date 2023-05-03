from connection import data as connection
from create import * 
from AlterTable import alterTable 
from Delete import delete
from os import system, name


li=['use database','create database','create table','Alter table','update data','drop database or table','delete column or row','insert data','show Database or Tables','select','EXIT']
for count,i in enumerate(li):
    print("press",count," for "+i)


def skipChoice(ch):
 print("\n\nIf you want to exit this choice press @")
 choice=input("press @ or c ")
 if choice=='@':
  return '@'
 else:
   return 'c'

while True:
 choice=int(input("\n\nEnter your choice = "))
 if choice==0:   
  useDatabase()
 elif choice==1:  
  createDatabase()
 elif choice==2:  
   createTable()
 elif choice==3:
  alterTable()
 elif choice==4:
   updateData() 
 elif choice==5:
   drop()
 elif choice==6:
   delete()
 elif choice==7:
   print("This query is not working now...")
 elif choice==8:
    show()
 elif choice==9: 
    select()
 elif choice==10: 
    break   
#  elif choice=='@':
#     continue

      