import sys


class Plan(object):
    #Constructor de la clase
    def __init__(self,descripcion,nombre,rif_empresa):
        self.descripcion = descripcion
        self.nombre = nombre
        self.rif_empresa = rif_empresa

    def __eq__(self,otr):
        return self.nombre==otr.getNombre() and self.rif_empresa==otr.getRif_Empresa()

    #Definicion de getters y setters de la clase
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
   
    def getRif_Empresa(self):
	return self.rif_empresa
    
    def setRif_Empresa(self, rif_empresa):
	self.rif_empresa = rif_empresa
