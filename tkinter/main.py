import tkinter as tk
from tkinter import ttk
from estilo import Estilo
from formulario import Formulario


ventana = tk.Tk() 
ventana.title("Programa que dice cosas que ya sabias")
ventana.geometry("800x600")
ventana.configure(bg='#75E2E0')

estilo = Estilo(ventana)

titulo = tk.Label(estilo.frame, text="Bienvenido", font=("System", 20), bg='#02364A', fg='BLACK').pack(pady=20)
texto = tk.Label(estilo.frame, text="Por favor completa tus datos personales:", font=("Terminal", 12), bg='#02364A', fg='BLACK').pack(pady=10, anchor='w', padx=20)

formulario = Formulario(estilo.frame)   

def crear_lista():
    lista = []
    lista.append(formulario.nombre.get())
    lista.append(formulario.apellido.get())
    lista.append(formulario.fechaNacimiento.get())
    lista.append(formulario.profesion.get())
    print(lista)

def abrir_ventana_hija():
    ventana_hija = tk.Toplevel(ventana)  
    ventana_hija.title("Si ves que ya sabias")
    ventana_hija.geometry("928x154") 
    ventana_hija.configure(bg='#D9F5F0')
    
    mensaje = f"Hola {formulario.nombre.get()} {formulario.apellido.get()} naciste el {formulario.fechaNacimiento.get()} y actualmente eres {formulario.profesion.get()}"
    
    etiqueta = tk.Label(ventana_hija, text=mensaje, font=("Terminal", 12), bg='#D9F5F0')
    etiqueta.pack(pady=10)


boton = tk.Button(estilo.frame, text="Listo",font=("Terminal", 12), bg='#D9F5F0',command=lambda: [crear_lista(), abrir_ventana_hija()])
boton.pack(pady=10)

ventana.mainloop()