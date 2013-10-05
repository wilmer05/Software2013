import sys
from Plan import Plan 

class Postpago(Plan): 
  
    #Constructor de la clase
    def __init__(self,ilimitado,nombre,renta,rif_empresa,descripcion=""):
	super(Postpago,self).__init__(descripcion,nombre,rif_empresa)
        self.ilimitado = ilimitado
        self.renta = renta

    def __eq__(self,otro):
        return self.nombre==otro.getNombre() and self.rif_empresa==otro.getRif_Empresa()
        
    #Definicion de getters y setters de la clase

    def getIlimitado(self):
        return self.ilimitado

    def setIlimitado(self, ilimitado):
        self.ilimitado = ilimitado

    def getRenta(self):
        return self.renta

    def setRenta(self,renta):
        self.renta = renta
