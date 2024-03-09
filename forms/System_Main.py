import tkinter as tk

class System_main:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana Centrada")

        # Establece las dimensiones de la ventana
        ancho_ventana = 800
        alto_ventana = 500

        self.centrar_ventana(ancho_ventana, alto_ventana)

        self.ventana.mainloop()

    def centrar_ventana(self, ancho, alto):
        # Obtiene las dimensiones de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcula la posición x, y para centrar la ventana
        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2

        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')


