import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk 
import utils.calculadora as calcula

if __name__=="__main__":
    app = calcula.CalculadoraGeometrica()
    app.mainloop()
