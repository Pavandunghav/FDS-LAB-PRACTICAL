

# average score of the class
def avg(l,n):
    
  avg=sum(l)/n

  print("average marks of the class is :",avg)

# highest score and lowest score 
def hsls(l,n):
     
 l.sort()


 hs=l[-1]
 ls=l[0]
 print("the highest ecore of the class:",hs)
 print("the lowest score of the class is :",ls)

#count of absent student 
def ab(l,n):
    
 ab=0
 for i in range (n):
    if (l[i]==0) or (l[i]<0):
        ab=ab+1

 print("no. of absent student is :",ab)

# display mark with highest count 

def hc(l,n):
    
 max=1
 re=0
 for i in range (0,n):
   
    freq=l.count(l[i])
    
    if (freq>max):
      max=freq
      re=i
    

 print("highest count in the student list :",max)
 print("element with highest count is :",l[re])



# creating a main function 

global l 

def main():
 flag="yes"
 while(flag=="yes"):
  l=[]
  n=int(input("enter no. of students :"))

  for i in range (n):
    
 
   a=int(input("enter your marks :"))
   l.append(a)
   print(l)


  print("1]avg of marks 2] highest and lowest score 3] count of absent student  4] mark with highest count ")
  ch=int(input("enter your choice :"))

  if(ch==1):
     avg(l,n)
  if(ch==2):
     hsls(l,n)
  if(ch==3):
     ab(l,n)
  if(ch==4):
     hc(l,n)
    
  flag=str(input("do you want to continue (yes/no)?"))

main()