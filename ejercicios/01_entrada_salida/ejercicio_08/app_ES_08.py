import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Leonel
apellido:Gima
---
Ejercicio: entrada_salida_08
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, calcular y mostrar el resto de la división utilizando el Dialog Alert. 
Ej: "El resto de dividir 7 por 2 es: 1" 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_uno_texto = self.txt_operador_a.get()
        numero_uno_a_numero = int(numero_uno_texto)

        numero_dos_texto = self.txt_operador_b.get()
        numero_dos_a_numero = int(numero_dos_texto)

        resultado = numero_dos_a_numero % numero_uno_a_numero

        resultado_a_texto = str(resultado)

        mensaje="el resultado del resto es :" + resultado_a_texto  

        alert(title="resto",messege=mensaje)
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()