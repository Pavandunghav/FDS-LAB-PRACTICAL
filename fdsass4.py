# matrix operations , 1] addition  3] multiplication 2] transpose 
def get(r,c,m):
    for i in range(r):
        a=[]
        for j in range(c):
            el=int(input("ENTER THE ELEMENT :"))
            a.append(el)
        m.append(a)
        
    
def show(r,c,m):
    
     for i in range(r):
            
        for j in range(c):
           print(m[i][j],end=" ")
        print()
        
        
def add(r,c,m1,m2):
    res = []
    for i in range(len(m1)):
        a=[]  
        for j in range(len(m1[i])):
           a.append( m1[i][j] +m2[i][j])
        res.append(a)
    print("THE ADDITION OF THE MATRIX IS :")
    show(r,c,res)
        
        
        
def transpose(r,c,m):
    
    
    for i in range(r):
            
        for j in range(c):
           print(m[j][i],end=" ")
        print()
    
        
def main():
    print("THIS IS FOR THE MATRIX 1:")
    r1=int(input("ENTER THE NO. OF ROWS :"))
    c1=int(input("ENTER THE NO. OF COLUMNS :"))
    m1=[]
    
    #TAKING ELEMENTS OF THE MATRIX 
    
    get(r1,c1,m1)
        
    
    #displaying the matrix 
    
    print(f"YOUR MATRIX  1 IS :")
    show(r1,c1,m1)
    
    
    print("\n\nTHIS IS FOR THE MATRIX 2:")
   
    r2=int(input("ENTER THE NO. OF ROWS :"))
    c2=int(input("ENTER THE NO. OF COLUMNS :"))
    
   
    m2=[]
    m3=[]
    
    
    #for second matrix 
    
    get(r2,c2,m2)
    
    
     #displaying the matrix 
     
    
    
    print(f"YOUR MATRIX  2 IS :")
    show(r2,c2,m2)
    
    
    print("1]ADDITION \n 2] TRANSPOSE ")
    ch=int(input("ENTER YOUR CHOICE :"))
    # addition 
    
    if(ch==1):
       if(r1==r2 and c1==c2):
         add(r1,c1,m1,m2)
     
       else:
         print("ADDITION IS NOT POSSIBLE ")
         
         
         
    if(ch==2):
        print("THE TRANSPOSE OF THE MATRIX 1 IS :")
        transpose(r1,c1,m1)
        
        print("THE TRANSPOSE OF THE MATRIX 2 IS :")
        transpose(r2,c2,m2)
        
    
main()
    