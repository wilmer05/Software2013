import sys

#Clase que representa un servicio
class Servicio:
    def __init__(self,costo,nombre):
        self.costo = costo
        self.nombre = nombre


    #Sobrecarga del operador == para esta clase
    def __eq__(self,otro):
        return self.nombre == otro.nombre

    #Definicion de getters y setters de la clase
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getCosto(self):
        return self.costo

    def setCosto(self,costo):
        self.costo = costo

