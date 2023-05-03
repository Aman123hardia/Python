file=open('studentData.txt','r')
temp=open('temp.txt','w')

d=int(input("Enter how many data you want to insert.."))

while(d):
    rollNo=input("Enter roll number")
    name=input("Enter your name")
    Class = input("Enter your class")
    totalMarks=input("Enter your total marks")
    temp.write(rollNo+" "+name+" "+Class+" "+totalMarks+" \n")
  
temp.close()
file.close()
