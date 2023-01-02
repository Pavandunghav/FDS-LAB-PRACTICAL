# take the string from the user and do the operations 

#1]display the word withe the logest length 
#2]find the frequency of the particular letter 
#3]palindrome or not 

def long(s):
    l=s.split()
    
    longest=0
    for i in l:
      if(longest<len(i)):
          longest=len(i)
          ln=i
      
      else:
          continue
      
    print(f"THE LONGEST WORD IN THE STRING:{ln}")
    print(f"THE LENGTH OF THE LONGEST WORD IN THE STRING IS :{longest} ")
    
   # print(s)
    
    
def fr(s):
    el=str(input("ENTER THE CHARACTER :"))
    
    fr=0
    
    for i in s:
        if(i==el):
            fr=fr+1
    print(f"THE FREQUENCY OF THE CHARACTER IS :{fr}")
     
     
            
    
    
    
def pal(s):
    
    
    for i in range(0,int(len(s)/2+1)):
        
        j=len(s)-1
           
        if(s[i]==s[j]):
            v="THE STRING IS PALINDROME "
            break;
            
        else:
            j=j-1
            v="THE STRING IS NOT THE PALINDROME "
       
    
    print(v)

        
    
    
def main():
    
    
    s=str(input("ENTER THE STRING :"))
    
    print("1]DISPLAY THE WORD WITH THE LONGEST LENGTH ")
    print("2]FREQUENCY OF THE PARTICULAR LETTER  ")
    print("3]PALINDROME OR NOT  ")
    
    ch=int(input("ENTER YOUR CHOICE :"))
    
    if(ch==1):
        long(s)
        
    elif(ch==2):
        fr(s)
    elif(ch==3):
        pal(s)
        
    else:
        print("ENTER THE VALIND CHOICE :")
        main()


main()

    
    
    
    
    