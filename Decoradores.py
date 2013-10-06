import sys
from Decorador import Decorador
#Decoradores para el sistema

#Primer decorador
class DecoradorSegundos(Decorador):
    def __init__(self,id_Cliente,idn,nombre,nombre_plan,padre,rif_empresa,saldo):
        super(DecoradorSegundos,self).__init__(id_Cliente,idn,nombre,nombre_plan,rif_empresa,saldo)
        self.padre = padre
        self.costoServicio = 300
        self.nombreServicio = "200 segundos adicionales"
        pass

    def getNombreServicio(self):
        return self.nombreServicio

    def getCostoServicio(self):
        return self.costoServicio

    def imprimir(self):
        self.padre.imprimir(),
        print ", posee el servicio \"" + self.nombreServicio+"\" que cuesta " + str(self.costoServicio),

    def agregar(self,BD):
        adicionado = Adiciona(self.idn,self.nombre,self.nombreServicio)
        BD.agregarAdiciona(self.idn,self.nombre,self.nombreServicio)
        return adicionado
        

#Segundo decorador
class DecoradorMensajes(Decorador):
    def __init__(self,id_Cliente,idn,nombre,nombre_plan,padre,rif_empresa,saldo):
        super(DecoradorMensajes,self).__init__(id_Cliente,idn,nombre,nombre_plan,rif_empresa,saldo)
        self.padre = padre
        self.costoServicio = 200
        self.nombreServicio = "300 mensajes adicionales"
   
    def getNombreServicio(self):
        return self.nombreServicio

    def getCostoServicio(self):
        return self.costoServicio

    def imprimir(self):
        self.padre.imprimir()
        print ", posee el servicio \"" + self.nombreServicio+"\" que cuesta " + str(self.costoServicio),
    
    def agregar(self,BD):
        adicionado = Adiciona(self.idn,self.nombre,self.nombreServicio)
        BD.agregarAdiciona(self.idn,self.nombre,self.nombreServicio)
        return adicionado
