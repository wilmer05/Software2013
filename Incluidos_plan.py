'''
Created on 05/10/2013

@author: sm
'''
"""Modulo para la Clase Incluidos_plan"""
class Incluidos_plan(object):
    
    #Constructor
    def __init__(self,cantidad,nombre,rif_empresa,tipo):
                self.setCantidad(cantidad)
                self.setNombre(nombre)
                self.setRifEmpresa(rif_empresa)
                self.setTipo(tipo)
    
    #Metodos
    def __repr__(self):
            return "Incluidos_plan(cantidad=%r,nombre=%r,rif_empresa=%r,tipo=%r)"%(self.cantidad,self.nombre,self.rif_empresa,self.tipo)
    
    def __str__(self):
            return "Incluidos_plan(%d,%s,%d,%s)"%(self.cantidad,self.nombre,self.rif_empresa,self.tipo)
    
    def __eq__(self,otro):
            """x.__eq__(y) <==> x==y
                Dos planes son iguales si sus nombres, rifs de empresa y sus tipos son iguales"""
            if isinstance(otro,Incluidos_plan):
                return self.nombre==otro.nombre and self.rif_empresa==otro.rif_empresa and self.tipo==otro.tipo
            else:
                raise NotImplementedError("Un plan con servicio incluido solo puede ser comparado con otro plan con servicio incluido")
    
    
    
#Setters    
    def setNombre(self,valor):
            if isinstance(valor,basestring):
                self.__name=valor
            else:
                raise ValueError("El nombre debe ser un string")
    
    def setCantidad(self,valor):
            if type(valor) in {int,long}:
                self.__cant=valor
            elif isinstance(valor, basestring):
                try:
                    self.__cant=int(valor)
                except ValueError:
                    raise ValueError("La cantidad debe ser un numero, o un string de un numero")
            else:
                raise ValueError("La cantidad, o un string de un numero")
    
    def setRifEmpresa(self,valor):
            if type(valor) in {int,long}:
                self.__rif=valor
            elif isinstance(valor, basestring):
                try:
                    self.__rif=int(valor)
                except ValueError:
                    raise ValueError("El Rif debe ser un numero, o un string de un numero")
            else:
                raise ValueError("El Rif debe ser un numero, o un string de un numero")
    
    def setTipo(self,valor):
            if isinstance(valor,basestring):
                self.__tipo=valor
            else:
                raise ValueError("El tipo debe ser un string")
        
    
            
            
    nombre=property(lambda self:self.__name, setNombre,doc="Nombre del servicio extra")
    rif_empresa=property(lambda self:self.__rif, setRifEmpresa,doc="Rif de la empresa")
    tipo=property(lambda self:self.__tipo, setTipo,doc="Tipo de servicio adicional")
    cantidad      =property(lambda self:self.__cant,  setCantidad, doc="Cantidad disponible de recursos del servicio extra")
    
#Getters
    
    def getNombre(self):
            return self.nombre
    def getRifEmpresa(self):
            return self.rif_empresa
    def getTipo(self):
            return self.tipo
    def getCantidad(self):
            return self.cantidad
