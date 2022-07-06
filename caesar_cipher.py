# import libraries

import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from string import ascii_letters


def encrypt():
    encrypted_text = ""
    text = text_messagebox.get("1.0",tk.END)
    code = int(code_value.get())
    for i in range(len(text)):
        for j in range(len(ascii_letters)):
            value = text[i]
            if value.isalpha():
                if value == ascii_letters[j]:
                    encrypted_text += ascii_letters[((j + code)%26)]
            else :
                encrypted_text += text[i]
                break
    text_messagebox.delete('1.0',END)
    text_messagebox.insert(tk.INSERT,"Your encrypted text is :\n\n"+encrypted_text)
    text_messagebox.update()

    

def decrypt():
    decrypted_text = ""
    text = text_messagebox.get("1.0",tk.END)
    code = int(code_value.get())
    for i in range(len(text)):
        for j in range(len(ascii_letters)):
            value = text[i]
            if value.isalpha():
                if value == ascii_letters[j]:
                    decrypted_text += ascii_letters[((j - code)%26)]
            else :
                decrypted_text += text[i]
                break
    text_messagebox.delete('1.0',END)
    text_messagebox.insert(tk.INSERT,"Your decrypted text is :\n\n"+decrypted_text)
    text_messagebox.update()

def clear():
    text_messagebox.delete('1.0',END)


# declare the tkinter window
win = tk.Tk()
win.config(background='dark gray')

# declare message boxes and buttons
win.title("Encryption Frame Message")
win.geometry('450x250')
win.resizable(False,False)


label = tk.Label(text="ENTER TEXT BELOW",background="light blue").grid(column=0,row=0,columnspan=3)
text_messagebox  = scrolledtext.ScrolledText(win,wrap=tk.WORD,width=50,height=10)
text_messagebox.config(background="light gray")
text_messagebox.grid(column=0,row=1,columnspan=3)
text_messagebox.focus()
encrypt_button = tk.Button(text="Encrypt",command=encrypt).grid(column=1,row=4)
decrypt_button = tk.Button(text="Decrypt",command=decrypt).grid(column=2,row=4)
exit_button = tk.Button(text="Exit",command=exit).grid(row=5,column=1)
clear_button = tk.Button(text="Clear",command=clear).grid(row=5,column=0)
code_value = tk.StringVar()
code_entry = ttk.Entry(show="Enter encryption or decryption code",textvariable=code_value).grid(row=4,column=0)

# show the window 
win.mainloop()