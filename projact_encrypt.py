from tkinter import *
from tkinter import ttk
import math
import random
import unicodedata


class Encrypt:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x400')  # تعديل الحجم الكلي للنافذة
        self.root.title('برنامج تشفير متعدد')
        self.root.config(background='lightgray')
        self.root.resizable(False, False)
        #---------------------------------------------------------------- 
        
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
        
        from math import ceil

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
        def Caesar_algorithm(Plaint, KEY):

            
            Arabic_encryption = ""
            English_encryption = ""

            for s in range(97, 123):
                English_encryption += chr(s)
            for v in range(1568, 1611):
                Arabic_encryption += chr(v)

            result = ""
            result1 = ""

            for i in Plaint:
                cat = unicodedata.name(i).split()[0]#
                match cat:
                    case "LATIN":
                        n_encryption = (English_encryption.index(i.lower()) + KEY) % len(English_encryption)
                        if i.isupper():
                            result += English_encryption[n_encryption].upper()
                        else:
                            result += English_encryption[n_encryption]
                    case "ARABIC":
                        n_encryption1 = (Arabic_encryption.index(i) + KEY) % len(Arabic_encryption)
                        result1 += Arabic_encryption[n_encryption1]

            return result1 + result
        
        
        def Caesar_algorithm_De(Plaint, KEY):
             
                Arabic_encryption=""
                English_encryption=""

                for s in range(97,123):
                    English_encryption+=chr(s)
                for v in range(1568,1611):
                    Arabic_encryption+=chr(v) 
                result=""
                result1=""
                for i in Plaint:
                    cat=unicodedata.name(i).split()[0]
                    match cat:
                        case "LATIN":
                            n_encryption=(English_encryption.index(i.lower())-KEY)%len(English_encryption)
                            if i.isupper():
                                result+=English_encryption[n_encryption] 
                            else:
                                result+=English_encryption[n_encryption]
                        case "ARABIC":
                            n_encryption1=(Arabic_encryption.index(i)-KEY)%len(Arabic_encryption)
                            result1+=Arabic_encryption[n_encryption1] 

                return result1 + result
        #---------------------------------------------------------------------- RC4------------------------------------------------------
        def RC4(message, key):
            def KSA(key):
                
                S = list(range(256))

                j = 0

                for i in range(256):
                    j = (j + S[i] + key[i % len(key)]) % 256
                    S[i], S[j] = S[j], S[i]

                return S

            def PRGA(S):
                
                i = j = 0
                while True:
                    i = (i + 1) % 256

                    j = (j + S[i]) % 256
                    S[i], S[j] = S[j], S[i]

                    yield S[(S[i] + S[j]) % 256]

            # تحويل النصوص إلى بايتات
            
            key = [ord(c) for c in key]

            S = KSA(key)

            keystream = PRGA(S)


            # تشفير/فك التشفير

            result = ''.join([chr(ord(c) ^ next(keystream)) for c in message])
            
            return result

        
        
        #----------------------------------------------------------------     =================================================================
        def Multiplicative(Plaint, KEY):
                    less1=[]
                    value=[]

                    resault=""
                    for i in Plaint:

                        less1.append(ord(i))
                        
                        for j in less1:
                          j-=97
                        value+=chr(((KEY*j)%26)+97)
                        
                    for k in value:
                        resault+=k
                   
                    return resault


        # --------------------- خوارزمية RSA ----------------------------------------------------------------------------------------------------------
        def generate_rsa_keys():
   # """توليد مفاتيح RSA"""
            def generate_prime():
                while True:
                    num = random.randint(100, 999)
                    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
                        return num

            p, q = generate_prime(), generate_prime()
            n = p * q
            phi = (p - 1) * (q - 1)
            e = 65537
            while math.gcd(e, phi) != 1:
                e += 2
            d = pow(e, -1, phi)
            return (e, n), (d, n)
        global public_key, private_key
        public_key, private_key = generate_rsa_keys()

        def rsa_encrypt(public_key, plaintext):
            """تشفير النص باستخدام المفتاح العام"""
            
            e, n = public_key
            ciphertext = [str(pow(ord(char), e, n)) for char in plaintext]
            return ' '.join(ciphertext)
        #----------------

        def rsa_decrypt(private_key, ciphertext):
            """فك تشفير النص باستخدام المفتاح الخاص"""
            d, n = private_key
            ciphertext_numbers = map(int, ciphertext.split())
            plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext_numbers])
            return plaintext

        # --------------------- وظائف الأزرار ---------------------
        def generate_keys_action():
            """توليد وعرض المفاتيح"""
            global public_key, private_key
            public_key, private_key = generate_rsa_keys()

            displayy_ras.delete("1.0", END)
            displayy_ras.insert(END, f"المفتاح العام:  {public_key}\n")
            displayy_ras.insert(END, f"المفتاح الخاص:  {private_key}\n")
#----------------------------------------------------------------

        def encrypt_action():
            """تشفير النص وعرض النتيجة"""
            plaintext = plaintext_entry.get().strip() 
            if not plaintext:
                displayy_mess.delete("1.0", END)
                displayy_mess.insert(END, "يرجى إدخال نص لتشفيره")
                return

            encrypted_text = rsa_encrypt(public_key, plaintext)

            displayy_mess.delete("1.0", END)
            displayy_mess.insert(END, f"النص المشفر: {encrypted_text}\n")


        def decrypt_action():
            """فك تشفير النص وعرض النتيجة"""
            ciphertext = displayy_mess.get("1.0", END).strip().replace("النص المشفر: ", "")
            if not ciphertext:
                displayy_mess.insert(END, "يرجى إدخال نص مشفر لفكه")
                return

            decrypted_text = rsa_decrypt(private_key, ciphertext)

            displayy_mess.insert(END, f"النص المفكوك: {decrypted_text}\n")
 #----------------------------------------------------------------

        def reset_action():
            """إعادة تعيين الحقول"""
            plaintext_entry.delete(0, END)
            displayy_ras.delete("1.0", END)
            displayy_mess.delete("1.0", END)

        def exit_app():
            """إغلاق التطبيق"""
            root.quit()

        # --------------------- واجهة RSA ---------------------
        def GUI_RSA():
            """عرض واجهة التشفير RSA"""
            manage_fras = Frame(self.root, bg='lightblue')
            manage_fras.place(x=0, y=65, width=500, height=300)

            # مربع عرض المفاتيح
            global displayy_ras
            displayy_ras = Text(manage_fras, height=5, width=40, bg="lightyellow")
            displayy_ras.pack(pady=8)

            # إدخال النص
            global plaintext_entry
            plaintext_entry = Entry(manage_fras, justify='center', bg="powder blue", font=("Arial", 14))
            plaintext_entry.pack(pady=10)

            # مربع عرض النتائج
            global displayy_mess
            displayy_mess = Text(manage_fras, height=5, width=40, bg="lightyellow")
            displayy_mess.pack(pady=10)

            # أزرار التحكم
            btn_generate_keys = Button(manage_fras, text="توليد المفاتيح", bg='#11922E',command=generate_keys_action)
            btn_generate_keys.place(x=380, y=20, width=90, height=25)

            btn_encrypt = Button(manage_fras, text="تشفير", bg='#11900E', command=encrypt_action)
            btn_encrypt.place(x=380, y=135, width=90, height=25)

            btn_decrypt = Button(manage_fras, text="فك التشفير", bg='#11922E', command=decrypt_action)
            btn_decrypt.place(x=380, y=100, width=90, height=25)

            btn_reset = Button(manage_fras, text="Reset", bg="powder blue", command=reset_action)
            btn_reset.place(x=20, y=250, width=40, height=25)
            clear_button = Button(manage_fras, text="رجوع", bg='red', fg='white', command=lambda: manage_fras.destroy())
            clear_button.place(x=390, y=270, width=60, height=30)


     ########################################################################################################################################33 
      #--------------------------------- المتغيرات ----------------------------
        self.plaintext = StringVar()
        self.key = StringVar()
        self.typeofcipher = StringVar()
        Result = StringVar()
          #---------------------------------------------------------------- متغيرات rc4
        self.Message_rc4 =StringVar()
        self.key_rc4=StringVar()
        #----------------
        self.key_var=StringVar()


                #--------------------------------------------------------- تشفير  الخوارزميات القديمة-------
        def encrypt_old_algorithms():

                                manage_frame1 = Frame(self.root, bg='lightblue')
                                manage_frame1.place(x=0, y=65,width=500, height=300)

                                manage_text = Label(manage_frame1, text='ادخل النص  ')
                                manage_text.pack(fill=X)
                                plaintext = Entry(manage_frame1, justify='center', textvariable=self.plaintext, bg="powder blue")
                                plaintext.pack(pady=20)

                                manage_text = Label(manage_frame1, text='ادخل المفتاح   ')
                                manage_text.pack(fill=X)
                                key = Entry(manage_frame1, justify='center', textvariable=self.key, bg="powder blue")
                                key.pack(pady=20)

                                manage_text = Label(manage_frame1, text='النوع  ')
                                manage_text.pack(fill=X)

                                typeofcipher = ttk.Combobox(manage_frame1, textvariable=self.typeofcipher)
                                typeofcipher['values'] = ('1- additive', '2- multiplicitive', '3- keyless')
                                typeofcipher.pack()

                                btnTotal = Button(manage_frame1, text="فك تشفير", bg="powder blue",command=Results_de)
                                btnTotal.place(x=440, y=220, width=55, height=30)
                                
                                btnTotal2 = Button(manage_frame1, text="تشفير", bg="powder blue",command=Results)
                                btnTotal2.place(x=440, y=180, width=55, height=30)

                                btnReset = Button(manage_frame1, text="Reset", bg="powder blue",command=Reset)
                                btnReset.place(x=20, y=220, width=55, height=30)

                                global displayy
                                displayy = Text(manage_frame1, height=3, width=15)
                                displayy.pack(pady=10)
                                clear_button = Button(manage_frame1, text="رجوع", bg='red', fg='white', command=lambda: manage_frame1.destroy())
                                clear_button.place(x=390, y=270, width=60, height=30)
          #------------------------------------------------------------------------------------------------------------------------
          # 
          
        def Reset():

            self.plaintext.set("")
            self.key.set("")
            self.typeofcipher.set("")
            displayy.delete("1.0", END)  

        
            ##############################################
        def Results():  
               
            Plaint = self.plaintext.get()
            KEY =int(self.key.get())
            m=self.typeofcipher.get()
           
            match m:
                                case "1- additive":
                                    encrypted_text = Caesar_algorithm(Plaint, KEY)
                                    displayy.insert(END, encrypted_text)
                                case "2- multiplicitive":   
                                        encrypted_text =   Multiplicative(Plaint, KEY)
                                        displayy.insert(END, encrypted_text) 
                                case "3- keyless":  
                                        
                                        encrypted_text =  keyless(Plaint, KEY)
                                        displayy.insert(END, encrypted_text) 

        def Results_de():
                  Plaint = self.plaintext.get()
                  KEY =int(self.key.get())
                  m=self.typeofcipher.get()
                   
                  match m:
                                case "1- additive": 
                                    encrypted_text1 = Caesar_algorithm_De(Plaint,KEY)
                                    displayy.insert(END, encrypted_text1)
                                case "2- multiplicitive":   
                                        encrypted_text1 =Multiplicative(Plaint,KEY)
                                        displayy.insert(END, encrypted_text1)  
                                case "3- keyless":  
                                        
                                        encrypted_text =railway_de(Plaint, KEY)
                                        displayy.insert(END, encrypted_text)  

       #---------------------------------------------------------------- واجهة RC4
        def encrypt_rc4(): 
                                    
                                manage_fras_rc4 = Frame(self.root, bg='lightblue')
                                manage_fras_rc4.place(x=0, y=65,width=500, height=300)

                                manage_text = Label(manage_fras_rc4, text='Message :')
                                manage_text.pack(fill=X)

                                Message_rc4 = Entry(manage_fras_rc4, justify='center', textvariable=self.Message_rc4 , bg="powder blue")
                                Message_rc4 .pack(pady=20)
                                
                                manage_text = Label(manage_fras_rc4, text='Enter the Key :')
                                manage_text.pack(fill=X)
                                
                                key_rc4 = Entry(manage_fras_rc4, justify='center', textvariable=self.key_rc4, bg="powder blue")
                                key_rc4.pack(pady=20)




                                btnReset = Button(manage_fras_rc4, text="Reset", bg="powder blue",command= Reset_rc4)
                                btnReset.place(x=20, y=100, width=40, height=25)

                                btn_en_rc4 = Button(manage_fras_rc4, text="تشفير  ",bg='#11900E',command=Results_rc4)
                                btn_en_rc4.place(x=380, y=167, width=90, height=25)

                                btn_de_rc4= Button(manage_fras_rc4, text="فك تشفير ",bg='#11900E',command=Decrypt_rc4)
                                btn_de_rc4.place(x=380, y=200, width=90, height=25)


                                global displayy_rc4
                                displayy_rc4 = Text(manage_fras_rc4, height=3, width=30)
                                displayy_rc4.pack(pady=8)
                                clear_button = Button(manage_fras_rc4, text="رجوع", bg='red', fg='white', command=lambda:manage_fras_rc4.destroy())
                                clear_button.place(x=390, y=270, width=60, height=30)
#----------------------------------------------------------------
        def Reset_rc4():

            self.Message_rc4.set("")
            self.key_rc4.set("")
            
            displayy_rc4.delete("1.0", END)
            
            
                               
                               
         #----------------------------ارسال البيانات من الادخال 
         
        def Results_rc4():
            message = self.Message_rc4.get()
            key = self.key_rc4.get()
            if not message or not key:
                displayy_rc4.insert(END, "يرجى إدخال الرسالة والمفتاح!\n")
                return
            encrypted_message = RC4(message, key)
            displayy_rc4.insert(END, f"النص المشفر: {encrypted_message}\n")

        def Decrypt_rc4():
            encrypted_message = self.Message_rc4.get()
            key = self.key_rc4.get()
            if not encrypted_message or not key:
                displayy_rc4.insert(END, "يرجى إدخال النص المشفر والمفتاح!\n")
                return
            decrypted_message = RC4(encrypted_message, key)
            displayy_rc4.insert(END, f"النص الأصلي: {decrypted_message}\n")
                                      
#--------------------
                               
                        

        # --------------------- واجهة التحكم العلوية ---------------------------------------------------------------------------------
        def encrypt_teyp():
                # إنشاء الإطار الرئيسي
                manage_frame = Frame(self.root, bg='#85929E')
                manage_frame.place(x=10, width=488, height=70)

                # نص السؤال
                manage_text = Label(manage_frame, text=' Choose an Algorithm ? ', font=('Deco'))
                manage_text.pack(fill=X)

                # الأزرار الأساسية
                encrption = Button(manage_frame, text='RSA', bg='#85925E', fg='white', command=GUI_RSA)
                encrption.place(x=30, y=30, width=88, height=30)

                decrption = Button(manage_frame, text='RC4', bg='#85519E', fg='white', command=encrypt_rc4)
                decrption.place(x=100, y=30, width=88, height=30)

                decrption = Button(manage_frame, text='خوارزميات قديمة', bg='#11919E', fg='white', command=encrypt_old_algorithms)
                decrption.place(x=170, y=30, width=88, height=30)

                # زر "أخرى"
                decrption = Button(manage_frame, text='اخرى', bg='#11399E', fg='white', command=show_other_options)
                decrption.place(x=252, y=30, width=88, height=30)
               


#--------------------------------------------------------------------------------------------------------------------------------
            # دالة عرض الخيارات الإضافية عند الضغط على "أخرى"
        def show_other_options():
                other_frame = Frame(root, bg='#D5DBDB')
                other_frame.place(x=10, y=80, width=488, height=120)

                # زر تحميل الصورة
                load_button = Button(other_frame, text="تحميل صورة", bg='#5DADE2', fg='white')
                load_button.place(x=30, y=20, width=120, height=30)

                # إدخال المفتاح
                key_label = Label(other_frame, text="أدخل المفتاح:", bg='#D5DBDB')
                key_label.place(x=30, y=60)
                key_entry = Entry(other_frame, textvariable=self.key_var)
                key_entry.place(x=120, y=60, width=150)

                # زر التشفير
                encrypt_button = Button(other_frame, text="تشفير", bg='green', fg='white')
                encrypt_button.place(x=300, y=20, width=100, height=30)

                # زر فك التشفير
                decrypt_button = Button(other_frame, text="فك التشفير", bg='blue', fg='white')
                decrypt_button.place(x=300, y=60, width=100, height=30)

                # زر المسح
                clear_button = Button(other_frame, text="رجوع", bg='red', fg='white', command=lambda: other_frame.destroy())
                clear_button.place(x=410, y=40, width=60, height=30)


        # --------------------- واجهة التحكم الجانبية ---------------------
        manage_frame = Frame(self.root, bg='blue')
        manage_frame.place(x=500, width=150, height=400)

        manage_text = Label(manage_frame, text='لوحه التحكم', font=('Deco'))
        manage_text.pack(fill=X)

        encrption = Button(manage_frame, text='تشفير', bg='#85929E', fg='white')
        encrption.place(x=40, y=30, width=70, height=30)

        decrption = Button(manage_frame, text='فك تشفير', bg='#85929E', fg='white')
        decrption.place(x=40, y=65, width=70, height=30)

        exit2 = Button(manage_frame, text='خروج', bg='red', fg='white', command=exit_app)
        exit2.place(x=40, y=100, width=70, height=30)

        # عرض الواجهة العلوية
        encrypt_teyp()
        

#loop
root = Tk()
app = Encrypt(root=root)
root.mainloop()
