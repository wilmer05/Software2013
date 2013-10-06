'''
Created on 05/10/2013

@author: sm
'''
"""Modulo para la Clase Incluidos_sextras"""
class Incluidos_sextras(object):
    
    #Constructor
    def __init__(self,cantidad,nombre,tipo):
                self.setCantidad(cantidad)
                self.setNombreSextr(nombre)
                self.setTipo(tipo)
       
    #Metodos
    def __repr__(self):
            return "Incluidos_sextras(cantidad=%r,nombre_sextr=%r,tipo=%r)"%(self.cantidad,self.nombre_sextr,self.tipo)
    
    def __str__(self):
            return "Incluidos_sextras(%d,%s,%s)"%(self.cantidad,self.nombre_sextr,self.tipo)
    
    def __eq__(self,otro):
            """x.__eq__(y) <==> x==y
                Dos servicios extra son iguales si sus nombres y su tipo son iguales"""
            if isinstance(otro,Incluidos_sextras):
                return self.nombre_sextr==otro.nombre_sextr and self.tipo==otro.tipo
            else:
                raise NotImplementedError("Un servicio extra solo puede ser comparado con otro servicio extra")
    
   def __hash__(self):
        return hash((self.__nombre_sextr,self.tipo) 
    
    #Setters    
    def setNombreSextr(self,valor):
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
                raise ValueError("La cantidad debe ser un numero, o un string de un numero")
    
    def setTipo(self,valor):
            if isinstance(valor,basestring):
                self.__tipo=valor
            else:
                raise ValueError("El tipo debe ser un string")
        
   
            
            
    nombre_sextr=property(lambda self:self.__name, setNombreSextr,doc="Nombre del servicio extra")
    tipo=property(lambda self:self.__tipo, setTipo,doc="Tipo de servicio adicional")
    cantidad=property(lambda self:self.__cant,  setCantidad, doc="Cantidad disponible de recursos del servicio extra")
    
    #Getters    
    def getNombreSextr(self):
            return self.nombre_sextr
    def getTipo(self):
            return self.tipo
    def getCantidad(self):
            return self.cantidad
