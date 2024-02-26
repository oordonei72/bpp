import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk  
import utils.operaciones as operaciones 


"""
 Calculadora Geometrica, calcula la area de un circulo,cuadrado asi mismo determina el volumend de un cubo,
 se crea una clase que genere la interfas de usuario utilizando la libreria tkinter.

 Nota: es importan te tener instalado la libreria Pillow, si no lo tiene ejecuta en la linea de comando lo siguiente:
 >>> pip install Pillow

 asi mismo las operaciones de la calculadora estan en el archivo operaciones.py que se encuentra dentro del 
 directorio utils
 
"""
class CalculadoraGeometrica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Geométrica")
        #Establecer dimension iniciales de lka ventana principal

        self.geometry("300x200")
        #Muestr el titulo de las opciones
        self.label = tk.Label(self, text="Seleccione una opción:")
        self.label.pack()
        # prepara y carga las opciones a elejir
        self.opcion_var = tk.StringVar(self)
        opciones = ["Círculo", "Cuadrado", "Cubo"]
        self.opcion_var.set(opciones[0])

        self.menu_opciones = tk.OptionMenu(self, self.opcion_var, *opciones)
        self.menu_opciones.pack()
        
        # sirve para mostrar la opcion elejida
        self.valor_label = tk.Label(self,text="Ingrese la radio")
        self.valor_label.pack()

        #es para solicitar el dato
        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack()

         #Etiquetas para los resultados

        self.resultado_label = tk.Label(self,text="Resultado:")
        self.resultado_label.pack()

        # para detectar la opcion seleccionada

        self.opcion_var.trace_add("write",self.actualizar_opcion_label)


        #Cargar imagenes para los botones Usando ImageTk
        calcular_icon = Image.open("img/calcular_icon.png").resize((30,30))
        salir_icon = Image.open("img/salir_icon.png").resize((30,30))

        #Convertir imagenes a formato compatible con tkinter
        self.calcular_icon = ImageTk.PhotoImage(calcular_icon)
        self.salir_icon=ImageTk.PhotoImage(salir_icon)

        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular,image=self.calcular_icon,compound=tk.LEFT)
        self.calcular_btn.pack(side=tk.LEFT,padx=5)

        self.salir_btn = tk.Button(self,text="Salir",command=self.salir,image=self.salir_icon,compound=tk.LEFT)
        self.salir_btn.pack(side=tk.LEFT,padx=5)

       
    def calcular(self):
        """
        Metodo que optiene el valor y opcion que el usuario elije para realizar el calculo
        """
        opcion = self.opcion_var.get()
        valor = self.entry_valor.get()

        try:
            valor = float(valor)
            # Verificamos si el valor sea mayor que 0
            if valor<=0:
                raise ValueError("Error: El Valor debe ser mayor que 0")
                
            if opcion == "Círculo":
                resultado = operaciones.areaCirculo(valor)
                
                self.resultado_label.config(text=f"Resultado: \r Area del Circulo es: {resultado:.2f}")

            elif opcion == "Cuadrado":
                resultado = operaciones.areaCuadrado(valor)
               
                self.resultado_label.config(text=f"Resultado: \r Area del cuadrado es: {resultado:.2f}")

            elif opcion == "Cubo":
                resultado = operaciones.volCubo(valor)
                
                self.resultado_label.config(text=f"Resultado: \r El volumen del cubo es: {resultado:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    


    def salir(self):
        self.destroy()

    def actualizar_opcion_label(self,*args):
        """
        Metodo que actualiza el mensaje para que el usuario tenga una referencia que dato ingresar
        """
        mensaje=""
        op_elegida=self.opcion_var.get()

        if op_elegida=="Circulo":
           mensaje="Ingresa el radio del circulo:"
        elif op_elegida=="Cuadrado":
           mensaje="Ingrese el lado del cuadrado:"
        elif op_elegida=="Cubo":
           mensaje="Ingresa el lado del cubo:"
           
        self.valor_label.config(text=mensaje)

if __name__ == "__main__":
    app = CalculadoraGeometrica()
    app.mainloop()
