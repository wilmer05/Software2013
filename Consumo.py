import sys

class Consumo:
    #Constructor de la clase
    def __init__(self,instanciaBD,costo,descripcion,fecha,id_producto,nombre_producto):
        self.BD = instanciaBD
        self.costo = costo
        self.descripcion = descripcion
        self.fecha = fecha
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
    
    def agregar(self):
        self.BD.agregarConsumo(self.costo,self.descripcion,self.fecha,self.id_producto,self.nombre_producto)

    def eliminar(self):
        self.BD.eliminarConsumo(self.fecha,self.id_producto,self.nombre_producto)

    def imprimir(self):
        print ""+self.fecha+"  "+self.descripcion+"  "+str(self.costo)
    
        
    def __eq__(self,otro):
        #Dos consumos son iguales, si su fecha, y tanto el nombre como el id del producto son los mismos
        return self.fecha==otro.getFecha() and self.nombre_producto==otro.getNombre_Producto() and self.id_producto==otro.getId_Producto()

    #Definicion de getters y setters de la clase

    def getId_Producto(self):
        return self.id_producto

    def setId_Producto(self, id):
        self.id_producto = id

    def getNombre_Producto(self):
        return self.nombre_producto

    def setNombre_Producto(self,nombre):
        self.nombre_producto = nombre

    def getCosto(self):
        return self.costo

    def setCosto(self,costo):
        self.costo = costo

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def setFecha(self, fecha):
        self.fecha = fecha

    def getFecha(self):
        return self.fecha

    
