"""Modulo para la Clase Incluidos_plan"""

class IncluidoPlan(object):

    #Constructor
    def __init__(self,cantidad,nombre,rif_empresa,tipo):
        self.setCantidad(cantidad)
        self.setNombre(nombre)
        self.setRif_Empresa(rif_empresa)
        self.setTipo(tipo)

    #Metodos
    def __repr__(self):
        return "IncluidoPlan(cantidad=%r,nombre=%r,rif_empresa=%r,tipo=%r)"%(self.cantidad,self.nombre,self.rif_Empresa,self.tipo)

    def __str__(self):
        return "IncluidoPlan(%d,%s,%d,%s)"%(self.cantidad,self.nombre,self.rif_Empresa,self.tipo)

    def __eq__(self,otro):
        """x.__eq__(y) <==> x==y
           Dos planes son iguales si sus nombres, rifs de empresa y sus tipos son iguales"""
        if isinstance(otro,IncluidoPlan):
            return self.nombre==otro.nombre and self.rif_Empresa==otro.rif_Empresa and self.tipo==otro.tipo
        else:
            raise NotImplementedError("Un plan con servicio incluido solo puede ser comparado con otro plan con servicio incluido")

    def __hash__(self):
        return hash( (self.nombre, self.rif_Empresa, self.tipo) )

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

    def setRif_Empresa(self,valor):
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

    #Getters
    def getNombre(self):
        return self.nombre
    def getRif_Empresa(self):
        return self.rif_Empresa
    def getTipo(self):
        return self.tipo
    def getCantidad(self):
        return self.cantidad

    #atributos
    nombre      =property(lambda self:self.__name,setNombre,     doc="Nombre del servicio extra")
    rif_Empresa =property(lambda self:self.__rif, setRif_Empresa,doc="Rif de la empresa")
    tipo        =property(lambda self:self.__tipo,setTipo,       doc="Tipo de servicio adicional")
    cantidad    =property(lambda self:self.__cant,setCantidad,   doc="Cantidad disponible de recursos del servicio extra")


