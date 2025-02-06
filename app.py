from controlador.controlador_login import ControladorLogin
from tkinter import Tk

def app():
    root = Tk()
    app = ControladorLogin(root)
    root.mainloop()

if __name__ == '__main__':
    app()
