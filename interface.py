from tkinter import *
from tkinter import ttk
from Algorithms import Caesar_algorithm, Caesar_algorithm_De, Multiplicative, keyless, railway_de, RC4, generate_keys, encrypt_rsa, decrypt_rsa

class Encrypt:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x400')
        self.root.title('برنامج تشفير متعدد')
        self.root.config(background='lightgray')
        self.root.resizable(False, False)

        # المتغيرات
        self.plaintext = StringVar()
        self.key = StringVar()
        self.typeofcipher = StringVar()
        self.Message_rc4 = StringVar()
        self.key_rc4 = StringVar()
        self.key_var = StringVar()
        self.public_key = None
        self.private_key = None

        # إنشاء الواجهات
        self.create_main_ui()

    def create_main_ui(self):
        # واجهة اختيار الخوارزمية
        top_frame = Frame(self.root, bg='#85929E')
        top_frame.place(x=10, width=488, height=70)
        Label(top_frame, text='Choose an Algorithm?', font=('Arial', 12)).pack(fill=X)
        Button(top_frame, text='RSA', bg='#85925E', fg='white', command=self.GUI_RSA).place(x=30, y=30, width=88, height=30)
        Button(top_frame, text='RC4', bg='#85519E', fg='white', command=self.encrypt_rc4).place(x=100, y=30, width=88, height=30)
        Button(top_frame, text='خوارزميات قديمة', bg='#11919E', fg='white', command=self.encrypt_old_algorithms).place(x=170, y=30, width=88, height=30)
        Button(top_frame, text='اخرى', bg='#11399E', fg='white', command=self.show_other_options).place(x=252, y=30, width=88, height=30)

        # لوحة جانبية
        side_frame = Frame(self.root, bg='blue')
        side_frame.place(x=500, width=150, height=400)
        Label(side_frame, text='لوحه التحكم', font=('Arial', 12)).pack(fill=X)
        Button(side_frame, text='تشفير', bg='#85929E', fg='white').place(x=40, y=30, width=70, height=30)
        Button(side_frame, text='فك تشفير', bg='#85929E', fg='white').place(x=40, y=65, width=70, height=30)
        Button(side_frame, text='خروج', bg='red', fg='white', command=self.root.quit).place(x=40, y=100, width=70, height=30)

    # ---------------- RSA ----------------
    def GUI_RSA(self):
        self.manage_fras = Frame(self.root, bg='lightblue')
        self.manage_fras.place(x=0, y=65, width=500, height=300)
        self.displayy_ras = Text(self.manage_fras, height=5, width=40, bg="lightyellow")
        self.displayy_ras.pack(pady=8)
        self.plaintext_entry = Entry(self.manage_fras, justify='center', bg="powder blue", font=("Arial", 14))
        self.plaintext_entry.pack(pady=10)
        self.displayy_mess = Text(self.manage_fras, height=5, width=40, bg="lightyellow")
        self.displayy_mess.pack(pady=10)

        Button(self.manage_fras, text="توليد المفاتيح", bg='#11922E', command=self.generate_keys_action).place(x=380, y=20, width=90, height=25)
        Button(self.manage_fras, text="تشفير", bg='#11900E', command=self.encrypt_action).place(x=380, y=135, width=90, height=25)
        Button(self.manage_fras, text="فك التشفير", bg='#11922E', command=self.decrypt_action).place(x=380, y=100, width=90, height=25)
        Button(self.manage_fras, text="Reset", bg="powder blue", command=self.reset_rsa_action).place(x=20, y=250, width=40, height=25)
        Button(self.manage_fras, text="رجوع", bg='red', fg='white', command=lambda: self.manage_fras.destroy()).place(x=390, y=270, width=60, height=30)

    # ---------------- دوال RSA ----------------
    def generate_keys_action(self):
        self.public_key, self.private_key = generate_keys()
        self.displayy_ras.delete("1.0", END)
        self.displayy_ras.insert(END, f"Public: {self.public_key}\nPrivate: {self.private_key}\n")

    def encrypt_action(self):
        plaintext = self.plaintext_entry.get()
        if self.public_key:
            encrypted = encrypt_rsa(plaintext, self.public_key)
            self.displayy_mess.delete("1.0", END)
            self.displayy_mess.insert(END, str(encrypted))

    def decrypt_action(self):
        try:
            ciphertext = eval(self.displayy_mess.get("1.0", END))
            if self.private_key:
                decrypted = decrypt_rsa(ciphertext, self.private_key)
                self.displayy_mess.delete("1.0", END)
                self.displayy_mess.insert(END, decrypted)
        except:
            self.displayy_mess.insert(END, "خطأ في النص المشفر\n")

    def reset_rsa_action(self):
        self.plaintext_entry.delete(0, END)
        self.displayy_mess.delete("1.0", END)
        self.displayy_ras.delete("1.0", END)

    # ---------------- دوال الخوارزميات القديمة ----------------
    def encrypt_old_algorithms(self):
        self.manage_frame1 = Frame(self.root, bg='lightblue')
        self.manage_frame1.place(x=0, y=65, width=500, height=300)
        Label(self.manage_frame1, text='ادخل النص').pack(fill=X)
        Entry(self.manage_frame1, justify='center', textvariable=self.plaintext, bg="powder blue").pack(pady=20)
        Label(self.manage_frame1, text='ادخل المفتاح').pack(fill=X)
        Entry(self.manage_frame1, justify='center', textvariable=self.key, bg="powder blue").pack(pady=20)
        Label(self.manage_frame1, text='النوع').pack(fill=X)
        typeofcipher = ttk.Combobox(self.manage_frame1, textvariable=self.typeofcipher)
        typeofcipher['values'] = ('1- additive', '2- multiplicitive', '3- keyless')
        typeofcipher.pack()
        self.displayy = Text(self.manage_frame1, height=3, width=15)
        self.displayy.pack(pady=10)
        Button(self.manage_frame1, text="تشفير", bg="powder blue", command=self.Results).place(x=440, y=180, width=55, height=30)
        Button(self.manage_frame1, text="فك تشفير", bg="powder blue", command=self.Results_de).place(x=440, y=220, width=55, height=30)
        Button(self.manage_frame1, text="Reset", bg="powder blue", command=self.Reset).place(x=20, y=220, width=55, height=30)
        Button(self.manage_frame1, text="رجوع", bg='red', fg='white', command=lambda: self.manage_frame1.destroy()).place(x=390, y=270, width=60, height=30)

    def Reset(self):
        self.plaintext.set("")
        self.key.set("")
        self.typeofcipher.set("")
        self.displayy.delete("1.0", END)

    def Results(self):
        try:
            Plaint = self.plaintext.get()
            KEY = int(self.key.get())
            m = self.typeofcipher.get()
            if m == "1- additive":
                encrypted_text = Caesar_algorithm(Plaint, KEY)
            elif m == "2- multiplicitive":
                encrypted_text = Multiplicative(Plaint, KEY)
            elif m == "3- keyless":
                encrypted_text = keyless(Plaint, KEY)
            else:
                encrypted_text = "نوع غير صحيح"
            self.displayy.insert(END, encrypted_text + "\n")
        except:
            self.displayy.insert(END, "خطأ في التشفير\n")

    def Results_de(self):
        try:
            Plaint = self.plaintext.get()
            KEY = int(self.key.get())
            m = self.typeofcipher.get()
            if m == "1- additive":
                decrypted_text = Caesar_algorithm_De(Plaint, KEY)
            elif m == "2- multiplicitive":
                decrypted_text = Multiplicative(Plaint, KEY)
            elif m == "3- keyless":
                decrypted_text = railway_de(Plaint, KEY)
            else:
                decrypted_text = "نوع غير صحيح"
            self.displayy.insert(END, decrypted_text + "\n")
        except:
            self.displayy.insert(END, "خطأ في فك التشفير\n")

    # ---------------- RC4 ----------------
    def encrypt_rc4(self):
        self.manage_fras_rc4 = Frame(self.root, bg='lightblue')
        self.manage_fras_rc4.place(x=0, y=65, width=500, height=300)
        Label(self.manage_fras_rc4, text='Message :').pack(fill=X)
        Entry(self.manage_fras_rc4, justify='center', textvariable=self.Message_rc4, bg="powder blue").pack(pady=20)
        Label(self.manage_fras_rc4, text='Enter the Key :').pack(fill=X)
        Entry(self.manage_fras_rc4, justify='center', textvariable=self.key_rc4, bg="powder blue").pack(pady=20)
        self.displayy_rc4 = Text(self.manage_fras_rc4, height=3, width=30)
        self.displayy_rc4.pack(pady=8)
        Button(self.manage_fras_rc4, text="Reset", bg="powder blue", command=self.Reset_rc4).place(x=20, y=100, width=40, height=25)
        Button(self.manage_fras_rc4, text="تشفير", bg="#90240E", command=self.Results_rc4).place(x=380, y=167, width=90, height=25)
        Button(self.manage_fras_rc4, text="فك تشفير", bg="#902C0E", command=self.Decrypt_rc4).place(x=380, y=200, width=90, height=25)
        Button(self.manage_fras_rc4, text="رجوع", bg='red', fg='white', command=lambda: self.manage_fras_rc4.destroy()).place(x=390, y=270, width=60, height=30)

    def Reset_rc4(self):
        self.Message_rc4.set("")
        self.key_rc4.set("")
        self.displayy_rc4.delete("1.0", END)

    def Results_rc4(self):
        message = self.Message_rc4.get()
        key = self.key_rc4.get()
        if message and key:
            encrypted_message = RC4(message, key)
            self.displayy_rc4.insert(END, f"النص المشفر: {encrypted_message}\n")

    def Decrypt_rc4(self):
        message = self.Message_rc4.get()
        key = self.key_rc4.get()
        if message and key:
            decrypted_message = RC4(message, key)
            self.displayy_rc4.insert(END, f"النص الأصلي: {decrypted_message}\n")

    # ---------------- خيارات أخرى ----------------
    def show_other_options(self):
        other_frame = Frame(self.root, bg="#DADBD5")
        other_frame.place(x=10, y=80, width=488, height=120)
        Label(other_frame, text="أدخل المفتاح:", bg="#6F9516").place(x=30, y=60)
        Entry(other_frame, textvariable=self.key_var).place(x=120, y=60, width=150)
        Button(other_frame, text="رجوع", bg='red', fg='white', command=lambda: other_frame.destroy()).place(x=410, y=40, width=60, height=30)
