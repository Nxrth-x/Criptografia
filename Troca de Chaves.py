import tkinter as tk
import tkinter.ttk as ttk
from random import randint

#Main window
root = tk.Tk()
root.geometry("600x350")
root.title("Troca de Chaves - Diffie Hellman")

#Variables
primos = [977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103]
g = 1129
n = 7873

#Functions
def Generate_Values():
     #Sorteia um número aleatório
     Render_Entry(primos[randint(0, len(primos)-1)], entry_valor_alice)
     Render_Entry(primos[randint(0, len(primos)-1)], entry_valor_bob)
     return

def Render_Entry(value, reference):
     #Útil para renderizar o valor de uma entry sem ter que fazer várias vezes
     reference.delete(0, tk.END)
     reference.insert(0, value)
     return

def Calculate_Values():
     #Fórmula de Diffie Hellman
     #(g**Valor)%n
     Render_Entry((g**int(entry_valor_alice.get()))%n, entry_alice_enviado)
     Render_Entry((g**int(entry_valor_bob.get()))%n, entry_bob_enviado)
     return

def Send_Values():
     #Envia os valores calculados para a outra pessoa
     Render_Entry(entry_alice_enviado.get(), entry_bob_chave)
     Render_Entry(entry_bob_enviado.get(), entry_alice_chave)
     return
     
def Calculate_Key():
     #Estabelece uma chave comum entre ambas as partes
     Render_Entry((int(entry_alice_chave.get())**int(entry_valor_alice.get()))%n, entry_alice_chave)
     Render_Entry((int(entry_bob_chave.get())**int(entry_valor_bob.get()))%n, entry_bob_chave)
     return

def Reset():
     Render_Entry(0, entry_alice_chave)
     Render_Entry(0, entry_alice_enviado)
     Render_Entry(0, entry_valor_alice)
     Render_Entry(0, entry_bob_chave)
     Render_Entry(0, entry_bob_enviado)
     Render_Entry(0, entry_valor_bob)
     return

#Widgets
lbl_valores = tk.Label(root, text="Valores:\nG: 1129\nN: 7873").pack()

lbl_alice = tk.Label(root, text="Alice").pack()
entry_valor_alice = tk.Entry(root)
entry_valor_alice.pack()
entry_alice_enviado = tk.Entry(root)
entry_alice_enviado.pack()
entry_alice_chave = tk.Entry(root)
entry_alice_chave.pack()

lbl_bob = tk.Label(root, text="Bob").pack()
entry_valor_bob = tk.Entry(root)
entry_valor_bob.pack()
entry_bob_enviado = tk.Entry(root)
entry_bob_enviado.pack()
entry_bob_chave = tk.Entry(root)
entry_bob_chave.pack()

ttk.Button(root, text="Gerar valores", command=Generate_Values).pack()
ttk.Button(root, text="Calcular valor enviado", command=Calculate_Values).pack()
ttk.Button(root, text="Enviar valores", command=Send_Values).pack()
ttk.Button(root, text="Estabelecer chave", command=Calculate_Key).pack()
ttk.Button(root, text="Resetar", command=Reset).pack()

#Runs main window
root.mainloop()