import sys
from Plan import Plan 

class Prepago(Plan): 
  
    #Constructor de la clase
    def __init__(self,descripcion,nombre,renta,rif_empresa):
	super(Prepago,self).__init__(descripcion,nombre,rif_empresa)
        self.renta=renta
        
    def __eq__(self,otro):
        return self.nombre==otro.getNombre() and self.rif_empresa==otro.getRif_Empresa()
        
    #Definicion de getters y setters de la clase

    

    def getRenta(self):
        return self.renta

    def setRenta(self,renta):
        self.renta = renta
