import tkinter as tk

class Formulario:
    def __init__(self, frame_principal):
        self.frame_principal = frame_principal
        
        # Frame para nombre
        self.frame_nombre = tk.Frame(self.frame_principal, bg='#02364A')
        self.frame_nombre.pack(fill='x', padx=20, pady=10)

        self.texto1 = tk.Label(self.frame_nombre, text="Nombre:", font=("Terminal", 12), bg='#02364A', fg='BlACK')
        self.texto1.pack(side='left', pady=5)

        self.nombre = tk.Entry(self.frame_nombre, font=("System", 12),bg='#D9F5F0',fg='black')
        self.nombre.pack(side='left', padx=(10, 0))

        # Frame para apellido
        self.frame_apellido = tk.Frame(self.frame_principal, bg='#02364A')
        self.frame_apellido.pack(fill='x', padx=20, pady=10)

        self.texto2 = tk.Label(self.frame_apellido, text="Apellido:", font=("Terminal", 12), bg='#02364A', fg='BLACK')
        self.texto2.pack(side='left', pady=5)

        self.apellido = tk.Entry(self.frame_apellido, font=("System", 12), bg='#D9F5F0', fg='black')
        self.apellido.pack(side='left', padx=(10, 0))
    
        # Frame para FECHA DE NACIMIENTO
        self.frame_fechaNacimiento = tk.Frame(self.frame_principal, bg='#02364A')
        self.frame_fechaNacimiento.pack(fill='x', padx=20, pady=10)

        self.texto3 = tk.Label(self.frame_fechaNacimiento, text="Fecha de nacimiento:", font=("Terminal", 12), bg='#02364A', fg='BLACK')
        self.texto3.pack(side='left', pady=5)

        self.fechaNacimiento = tk.Entry(self.frame_fechaNacimiento, font=("System", 12), bg='#D9F5F0', fg='black')
        self.fechaNacimiento.pack(side='left', padx=(10, 0))

        # Frame para profesion
        self.frame_profesion = tk.Frame(self.frame_principal, bg='#02364A')
        self.frame_profesion.pack(fill='x', padx=20, pady=10)

        self.texto4 = tk.Label(self.frame_profesion, text="Profesion:", font=("Terminal", 12), bg='#02364A', fg='BLACK')
        self.texto4.pack(side='left', pady=5)

        self.profesion = tk.Entry(self.frame_profesion, font=("System", 12), bg='#D9F5F0', fg='black')
        self.profesion.pack(side='left', padx=(10, 0))