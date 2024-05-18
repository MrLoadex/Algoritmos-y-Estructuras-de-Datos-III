import tkinter as tk
from tkinter import ttk
import ctypes

# Cargar la DLL
calculadora_dll = ctypes.CDLL('C:/Users/Admin/Desktop/Kata_1_2024/Calculadora/calculadora.dll')  # Ruta a la DLL generada

# Definir los tipos de los argumentos y el tipo de retorno de las funciones de la DLL
calculadora_dll.sumar.argtypes = [ctypes.c_double, ctypes.c_double]
calculadora_dll.sumar.restype = ctypes.c_double

calculadora_dll.restar.argtypes = [ctypes.c_double, ctypes.c_double]
calculadora_dll.restar.restype = ctypes.c_double

calculadora_dll.multiplicar.argtypes = [ctypes.c_double, ctypes.c_double]
calculadora_dll.multiplicar.restype = ctypes.c_double

calculadora_dll.dividir.argtypes = [ctypes.c_double, ctypes.c_double]
calculadora_dll.dividir.restype = ctypes.c_double

# Función para manejar los cálculos
def calcular():
    try:
        expression = entry_resultado.get()
        result = eval(expression, {"__builtins__": None}, {
            'sumar': calculadora_dll.sumar,
            'restar': calculadora_dll.restar,
            'multiplicar': calculadora_dll.multiplicar,
            'dividir': calculadora_dll.dividir
        })
        historial_label.config(text=expression)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, result)
    except (ValueError, ZeroDivisionError, SyntaxError):
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")

# Función para ingresar números y operadores
def ingresar_dato(dato):
    entry_resultado.insert(tk.END, dato)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.resizable(0, 0)  # Evitar redimensionar la ventana

# Widgets
historial_label = ttk.Label(root, text="", font=('Arial', 10), anchor='e')
historial_label.grid(row=0, column=0, columnspan=4, padx=10, pady=2, sticky="nsew")

entry_resultado = ttk.Entry(root, justify='right', font=('Arial', 20))
entry_resultado.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Botones de la calculadora
botones = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3)
]

for (text, row, column) in botones:
    if text == '=':
        btn = ttk.Button(root, text=text, command=calcular)
    else:
        btn = ttk.Button(root, text=text, command=lambda t=text: ingresar_dato(t))
    btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

# Ajustar las filas y columnas
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Ejecutar la aplicación
root.mainloop()
