class TV:
    canal = 1
    precio = 500
    volumen = 1
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.control = None
        self.numTV += 1

    def setNumTV(self, num):
        self.numTV = num

    def setCanal(self, canal):
        if self.estado == True and canal > 0 and canal <= 120:
            self.canal = canal

    def getCanal(self):
        return self.canal

    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen):
        if self.estado == True and volumen >= 0 and volumen <= 7:
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    def getNumTV(self):
        return self.numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if self.estado == True and self.canal < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado == True and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado == True and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado == True and self.volumen > 0:
            self.volumen -= 1
