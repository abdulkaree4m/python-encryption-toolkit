        #-------------------------------------keyless---------------------------
from math import ceil
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