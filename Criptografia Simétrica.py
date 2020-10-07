#I M P O R T S

from tkinter import *
from random import randint

#F U N C T I O N S

#Encrypt
def encrypt(word):
     number, key = new_key()
     ans = ''
     for w in word:
          for i in range (0, 15000):
               if(w==chr(i)):
                    ans += chr(i+number)
     
     #Renders
     encrypt_input.delete(0, END)
     encrypt_input.insert(0, ans)
     encrypt_key.delete(0, END)
     encrypt_key.insert(0, key)

def new_key():
     key = ''
     number = 0
     for i in range (10):
          aux = randint(97, 126)
          number += aux-97
          key += chr(aux)
     return number, key

#Decrypt
def key_to_number(key):
     number = 0
     for c in key:
          for i in range(0, 300):
               if(c==chr(i)):
                    number+=i-97
                    break
     return number

def decrypt(word, key):
     ans = ''
     for w in word:
          for i in range(0, 15000):
               if(w==chr(i)):
                    ans += chr(i-key)

     #Renders
     decrypt_input.delete(0, END)
     decrypt_input.insert(0, ans)
     decrypt_key.delete(0, END)

#G U I

gui = Tk()
gui.title("Criptografia simétrica")
gui.geometry("400x240")

#W I D G E T S

encrypt_label = Label(gui, text="Criptografar").pack()
encrypt_input = Entry(gui, width=55)
encrypt_input.pack()
encrypt_key = Entry(gui, width=55)
encrypt_key.pack()
encrypt_button = Button(gui, text="Criptografar", command=lambda: encrypt(encrypt_input.get()))
encrypt_button.pack()

placeholder_label1 = Label(gui, text=" ").pack()

decrypt_label = Label(gui, text="Descriptografar").pack()
decrypt_input = Entry(gui, width=55)
decrypt_input.pack()
decrypt_key = Entry(gui, width=55)
decrypt_key.pack()
decrypt_button = Button(gui, text="Descriptografar", command=lambda: decrypt(decrypt_input.get(), key_to_number(decrypt_key.get())))
decrypt_button.pack()

placeholder_label1 = Label(gui, text=" ").pack()

close_button = Button(gui, text="  Fechar  ", command=lambda: gui.quit()).pack()

#W I N D O W
gui.mainloop()