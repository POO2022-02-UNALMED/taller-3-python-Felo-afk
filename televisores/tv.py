class TV:

    def __init__(self, marca, estado):
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.numTV = 0
        self.marca = marca
        self.estado = estado
        self.control = None
        TV.numTV += 1

    def setNumTV(self, num):
        TV.numTV = num

    def getNumTV(self):
        return TV.numTV

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
