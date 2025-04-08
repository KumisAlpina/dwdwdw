import tkinter as tk

class Estilo:
    def __init__(self, ventana):
        self.ventana = ventana
        
        self.ventana.grid_columnconfigure(0, weight=3)  
        self.ventana.grid_columnconfigure(1, weight=2)  
        self.ventana.grid_columnconfigure(2, weight=3) 
        self.ventana.grid_rowconfigure(0, weight=1)

        self.frame = tk.Frame(self.ventana, bg='#02364A')
        self.frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))