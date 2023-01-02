#selection sort

def sel(l,n):
    
    for i in range(0,n,1):
        
          for j in range(i+1,n,1):
        
              if(l[j]<l[i]):
                  l[i],l[j]=l[j],l[i]
              else:
                  continue
                  
              
              
              
    print("SORTED ARRAY IS :")
    
    
    for i in range(0,n,1):
        
        print(l[i],end=" ")
            
def main():
    
    n=int(input("ENTER NO. OF ELEMENTS "))
    l=[]
    for i in range(n):
      el=int(input("ENTER A ELEMENT "))
      l.append(el)
      
    sel(l,n)
main()  
      