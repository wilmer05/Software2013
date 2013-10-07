import sys

class Producto(object):
    def __init__(self,id_Cliente,idn,nombre,nombre_plan,renta,rif_empresa,saldo):
        self.id_Cliente = id_Cliente
        self.idn = idn
        self.nombre = nombre
        self.nombre_plan = nombre_plan
        self.renta = renta
        self.rif_empresa = rif_empresa
        self.saldo = saldo

    def __eq__(self,otro):
        return str(self.idn) == str(otro.getIdn()) and str(self.nombre)==str(otro.getNombre())


    def imprimir(self):
        print "El producto \""+str(self.nombre)+"\" tiene asociado el plan \""+str(self.nombre_plan) + "\" y pertenece \nal cliente de id: "+str(self.id_Cliente),


    def agregar(self,BD):
        BD.agregarProducto(self.idn,self.id_Cliente,self.nombre,self.nombre_plan,self.rif_empresa,self.saldo)

    def eliminar(self,BD):
        BD.eliminarProducto(self.idn,self.nombre)
        

    #Definicion de los getters y setters

    def getId_Cliente(self):
        return self.id_Cliente

    def setId_Cliente(self,valor):
        self.id_Cliente = valor

    def getIdn(self):
        return self.idn

    def setIdn(self,valor):
        self.idn = valor

    def getNombre(self):
        return self.nombre

    def setNombre(self,valor):
        self.nombre = valor

    def getNombre_Plan(self):
        return self.nombre_plan

    def setNombre_Plan(self,valor):
        self.nombre_plan = valor

    def getRif_Empresa(self):
        return self.rif_empresa

    def setRif_Empresa(self,valor):
        self.rif_empresa = valor

    def getSaldo(self):
        return self.saldo

    def setSaldo(self,valor):
        self.saldo = valor

    def getRenta(self):
        return self.renta

    def setRenta(self,valor):
        self.renta = valor

    

    
        

