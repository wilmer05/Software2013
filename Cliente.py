"""Modulo para la Clase cliente"""


class Cliente(object):
    """Clase para un cliente"""

    def __init__(self,direccion,esNatural,ide,nombre):
        """Cliente(direccion,esNatural,ide,nombre)"""
        self.setDireccion(direccion)
        self.setEsNatural(esNatural)
        self.setIde(ide)
        self.setNombre(nombre)

    def __repr__(self):
        return "Cliente(direccion=%r,esNatural=%r,ide=%r,nombre=%r)"%(self.direccion,self.esNatural,self.ide,self.nombre)

    def __str__(self):
        return "Cliente(%s,%s,%d,%s)"%(self.direccion,self.esNatural,self.ide,self.nombre)

    def __eq__(self,otro):
        """x.__eq__(y) <==> x==y
            Dos cliente son iguales si sus identificadores son iguales"""
        if isinstance(otro,Cliente):
            return self.ide==otro.ide
        else:
            raise NotImplementedError("Un cliente solo puede ser comparado con otro cliente")

    def __hash__(self):
        return hash(self.__ide)

    def setDireccion(self,valor):
        if isinstance(valor,basestring):
            self.__dire=valor
        else:
            raise ValueError("La direccion debe ser un string")
    
    def setEsNatural(self,valor):
        self.__natu=bool(valor)
    
    def setIde(self,valor):
        if type(valor) in {int,long}:
            self.__ide=valor
        elif isinstance(valor, basestring):
            try:
                self.__ide=int(valor)
            except ValueError:
                raise ValueError("El identificador del cliente debe ser un numero, o un string de un numero")
        else:
            raise ValueError("El identificador del cliente debe ser un numero, o un string de un numero")
    
    def setNombre(self,valor):
        if isinstance(valor,basestring):
            self.__name=valor
        else:
            raise ValueError("El nombre debe ser un string")

    def agregar(self,manejador):
        manejador.agregarCliente(self.direccion, self.ide, self.nombre, self.esNatural)

    def imprimir(self):
        print self

    def getDireccion(self):
        return self.direccion
    def getEsNatural(self):
        return self.esNatural
    def getIde(self):
        return self.ide
    def getNombre(self):
        return self.nombre

    direccion=property(lambda self:self.__dire, setDireccion,doc="Direccion del cliente")
    esNatural=property(lambda self:self.__natu, setEsNatural,doc="Booleano para indicar si es un cliente natural")
    ide      =property(lambda self:self.__ide,  setIde,      doc="Identificador del cliente")
    nombre   =property(lambda self:self.__name, setNombre,   doc="Nombre del cliente")    
