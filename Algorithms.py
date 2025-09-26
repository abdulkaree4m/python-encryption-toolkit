#-------------------------------------keyless---------------------------
from math import ceil
import unicodedata
def keyless(plaintext,key):
              
                row=0
                d=False  
                
                l=[''] *key   
                                     #* 4
                for i in plaintext:

                    l[row]+=i
                    if row==0 or row== key-1: # 0    -1
                        d=not d    # 1 
                        
                        if d:
                                    row+=1
                        else:
                                    row-=1 

                cip=''.join(l)

                return cip 
#//////////////////////////////////////////////////////
def railway_de(text,key):
        
            c=0
            reslute=""
            col=len(text)/key

            if type(col)is float:
                    col=ceil(col)

            arr=[]
            for i in range(key):
                    row=[]
                    for j in range(col):
                            row.append("")
                    arr.append(row)
            for i in range(key):
                    for j in range(col):
                            if c<len(text):
                                    arr[i][j]=text[c]
                                    c+=1
            for i in range(len(max(arr,key=len))):
                    for row in arr:
                            reslute+=row[i]
            
            return ''.join(reslute)

     #----------------------------------------------------------------

# ---------------- Caesar (Additive) ---------------- #
def Caesar_algorithm(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) + key - shift) % 26 + shift)
        else:
            result += char
    return result

def Caesar_algorithm_De(text, key):
    return Caesar_algorithm(text, -key)


