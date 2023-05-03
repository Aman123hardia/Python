import random 
from os import system
from rich import print
from rich.table import Table
import time
from rich.progress import track

score= random.randint(20,100)  

user1=0
user2=0
chance=random.randint(1,2)
table = Table(title="Target to win "+str(score))

while True:
     system('clear')
     table = Table(title="Target to win "+str(score))
     table.add_column("user 1 score is ", justify='center', style="cyan", no_wrap=True)
     table.add_column("user 2 score is ", justify='center', style="cyan", no_wrap=True)
     table.add_row(str(user1),str(user2))
  
     print(table)   
     user = chance
     print("[yellow]       user ",user," [yellow] chance ")
     if user1>=score or user2>=score:
         break
     if user==1: 
        d=input("Throw the dice press D or d = ")  
        if d=='D' or d=='d':      
         user1+= random.randint(1,6)         
         chance=2
        else:
          print("[red] PRESS ONLY D OR d ")
          time.sleep(2)
     elif user==2:
        d=input("Throw the dice press D or d = ")
        if d=='D' or d=='d':
         user2+= random.randint(1,6)
         chance=1      
        else:
          print("Please [red] PRESS ONLY D OR d ")
          time.sleep(2)
system('clear')
 
for i in track(range(10), description="Result will be in Processing..."):
    time.sleep(0.3)
if user1>=user2:
 table.add_row("[yellow] user 1 is winner Hurray!!!!!","[yellow] user 2 is Lost  Try Next Time ....")
elif user1==user2:
 table.add_row("Draw Match scroe is equal ","Draw Match scroe is equal")
else:
 table.add_row("[yellow] user 1 Lost  Try Next Time ....","[yellow] user 2  is winner Hurray!!!!!")
print(table)