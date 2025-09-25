        #-------------------------------------keyless---------------------------

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