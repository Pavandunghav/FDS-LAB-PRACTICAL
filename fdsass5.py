#matrix operation 
#1]substraction
#2]multiplication
#3]transpose
def get(r,c,m):
    
    for i in range (r):
         a=[]
         for i in range (c):
             el=int(input("ENTER THE ELEMENT :"))
             
             a.append(el)
             
         m.append(a)
         
        
        
def show(r,c,m):
    for i in range(r):
       
        for j in range(c):
            
            print(m[i][j],end="  ")
        print()
         
             
    
    
def sub(r1,c1,m1,m2):
     sub=[]
     for i in range (r1):
         b=[]
         for j in range (c1):
            b.append(m1[i][j]-m2[i][j])
         sub.append(b)
         
     print("SUBSTRACTION IS :")
     show(r1,c1,sub)
      
            
           
         
def mul(r1,c1,r2,c2,m1,m2):
    m=[]
    for i in range (r1):
         a=[]
         for j in range (c1):
           
            s=0
                 
            for j in range (c2):
           
             s+=m1[i][j]*m2[i][j]
            
            a.append(s)
         m.append(a)
         
    print("MULTIPLICATION IS :")    
    show(r1,c1,m)
    
def transpose (r,c,m):
           
    for i in range (r):
       
         for j in range (c):
            
            print(m[j][i],end="  ")
         print()
         
    
def main():
    
    print("THIS IS FOR THE MATRIX 1:")
    r1=int(input("ENTER THE NO. OF THE ROWS "))
    c1=int(input("ENTER THE NO. OF THE COLUMNS "))
    m1=[]
    get(r1,c1,m1)
    show(r1,c1,m1)
    
    
    
    print("THIS IS FOR THE MATRIX 2:")
    r2=int(input("ENTER THE NO. OF THE ROWS "))
    c2=int(input("ENTER THE NO. OF THE COLUMNS "))
    m2=[]
    get(r2,c2,m2)
    show(r2,c2,m2)
    
    print("1]SUBSTRACTION /n 2]MULTIPLICATION   /n 3] TRANSPOSE ")
    ch=int(input("ENTER YOUR CHOICE :"))
    
    if(ch==1):
        
        if(c1==c2 and r1==r2):
           sub(r1,c1,m1,m2)
        else:
            print("SUBSTRACTION IS NOT POSSIBLE :")
            
        
    if(ch==2):
        mul(r1,c1,r2,c2,m1,m2)
        
    if(ch==3):
        transpose(r1,c1,m1)
        transpose(r2,c2,m2)
        
main()   
    