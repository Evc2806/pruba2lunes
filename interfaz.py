import tkinter as tk
from tkinter import messagebox
from operaciones import realizar_operacion


class CalculadoraGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.crear_interfaz()

    def crear_interfaz(self):
        self.entrada = tk.Entry(self.root, width=20, font=("Arial", 18), bd=10, relief=tk.RIDGE)
        self.entrada.grid(row=0, column=0, columnspan=4, pady=10)

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for texto, fila, columna in botones:
            if texto == "=":
                btn = tk.Button(self.root, text=texto, width=5, height=2, bg="lightblue",
                                command=self.calcular)
            elif texto == "C":
                btn = tk.Button(self.root, text=texto, width=5, height=2, bg="lightcoral",
                                command=self.limpiar)
            else:
                btn = tk.Button(self.root, text=texto, width=5, height=2,
                                command=lambda t=texto: self.agregar_texto(t))

            btn.grid(row=fila, column=columna, padx=5, pady=5)

    def agregar_texto(self, texto):
        self.entrada.insert(tk.END, texto)

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def calcular(self):
        expresion = self.entrada.get()
        try:
            resultado = realizar_operacion(expresion)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, resultado)
        except Exception as e:
            messagebox.showerror("Error", "Expresión no válida")

    def run(self):
        self.root.mainloop()
