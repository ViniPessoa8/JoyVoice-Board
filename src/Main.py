from control.Controlador import Controlador

class Main:
    def __init__(self):
        self.controlador = Controlador()
        self.controlador.soundboard.carregar_sons()

if __name__ == '__main__':
    main = Main()