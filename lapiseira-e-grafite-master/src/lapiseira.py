from grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        super().__init__(calibre)

    def inserir (self, grafite: Grafite):
        if grafite == 0:
            self.getCalibre()
            self.getDureza()
            self.getTamanho()
            return True
        return False

    def remover(self):
        if self.grafite == 1:
            self.grafite -= 1
            return True

        return False

    def escrever(self, folhas: int):
        print(folhas)
        self.getFolhasEscritas()
        return self.escrever()


    def getGrafite(self):
        self.grafite
        return self.grafite

    def getCalibre(self):
        self.calibre
        return self.calibre

    def getFolhasEscritas(self):
        self.desgastePorFolha()
        return self.desgastePorFolha