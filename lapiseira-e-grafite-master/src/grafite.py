from dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.tamanho = tamanho
        super().__init__(dureza)
        self.folhas_usadas = 0

    def desgastePorFolha(self):
        if self.setTamanho() == 1:
            print("Uma folha")
            self.folhas_usadas = 1
        elif self.setTamanho() == 2:
            print("Dusa folhas")
            self.folhas_usadas = 2
        elif self.setTamanho() == 4:
            print("Quatro folhas")
            self.folhas_usadas = 4
        elif self.setTamanho() == 6:
            print("Seis folhas")
            self.folhas_usadas = 6

        return self.folhas_usadas

    def getDureza(self):
        self.dureza
        return self.dureza

    def getCalibre(self):
        self.calibre
        return self.calibre

    def getTamanho(self):
        self.tamanho
        return -1

    def setTamanho(self, tamanho:int):
        self.tamanho = tamanho
        return tamanho