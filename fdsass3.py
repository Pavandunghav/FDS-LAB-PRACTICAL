#taake a string input from the usr 
#disaplay 1st appearance of substring 
#count occurence of each word 
#palindrome or not 
def app(s):
    
    #l=s.split()
    el=str(input("ENTER THE SUBSTRING :"))
    
    x=s.find(el)
    print(x)
        
    
'''
    for i in range(0,len(s)-1):
        
        if(el[i]==s[i]):
            print(f"THE FIRST OCCURANCE OF THE SUBSTRING IS AT INDEX :{i}")
            break
            
        else:
            print("THE SUBSTRING YOU ENTERED IS NOT THE PART OF THE STRING ")'''
    
def oc(s):
    l=s.split()
    
    for i in l:
      count=s.count(i) 
      
      print(f"THE COUNT OF {i}   IS :{count}")
      
      
    
    
def pal(s):
    
    for i in range(0,int(len(s)/2+1)):
        j=len(s)-1
        
        if(s[j]==s[i]):
            v="THIS STRING IS PALINDROME "
            break
            
        else:
            v="THIS STRING IS NOT PALINDROME "
            j=j-1
            break
             
    print(v)
        
    
    
    
    
def main():
    s=str(input("ENTER THE STRING :"))
    
    print("1]1ST APPEARANCE OF THE SUBSTRING ")
    print("2]COUNT OCCURANCE OF THE EACH WORD  ")
    print("3] PALINDROME OR NOT  ")
    
    ch=int(input("ENTER YOUR CHOICE "))
    
    if(ch==1):
        app(s)
    elif(ch==2):
        oc(s)
        
    elif(ch==3):
        pal(s)
        
    else:
        print("ENTER THE VALID CHOICE ")
        main()
        
main()
    
    
    
    