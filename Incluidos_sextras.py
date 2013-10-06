"""Modulo para la Clase IncluidoServicio"""

class IncluidoServicio(object):
    
    #Constructor
    def __init__(self,cantidad,nombre,tipo):
        self.setCantidad(cantidad)
        self.setNombre_Sextr(nombre)
        self.setTipo(tipo)
       
    #Metodos
    def __repr__(self):
        return "IncluidoServicio(cantidad=%r,nombre_Sextr=%r,tipo=%r)"%(self.cantidad,self.nombre_Sextr,self.tipo)
    
    def __str__(self):
        return "IncluidoServicio(%d,%s,%s)"%(self.cantidad,self.nombre_Sextr,self.tipo)
    
    def __eq__(self,otro):
        """x.__eq__(y) <==> x==y
        Dos servicios extra son iguales si sus nombres y su tipo son iguales"""
        if isinstance(otro,IncluidoServicio):
            return self.nombre_Sextr==otro.nombre_Sextr and self.tipo==otro.tipo
        else:
            raise NotImplementedError("Un servicio extra solo puede ser comparado con otro servicio extra")
    
    def __hash__(self):
        return hash( (self.nombre_Sextr, self.tipo) )
    
    #Setters    
    def setNombre_Sextr(self,valor):
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
   
    #Getters    
    def getNombre_Sextr(self):
        return self.nombre_Sextr
    def getTipo(self):
        return self.tipo
    def getCantidad(self):
        return self.cantidad

    #atributos
    nombre_Sextr = property(lambda self:self.__name, setNombre_Sextr, doc="Nombre del servicio extra")
    tipo         = property(lambda self:self.__tipo, setTipo,         doc="Tipo de servicio adicional")
    cantidad     = property(lambda self:self.__cant, setCantidad,     doc="Cantidad disponible de recursos del servicio extra")
 
