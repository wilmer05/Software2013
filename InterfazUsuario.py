# -*- coding: iso-8859-15 -*-
import sys
    
"""
Clase InterfazUsuario:

Clase dedicada a la interaccion con el usuario.
Segun la accion que se desea realizar se piden los datos necesarios.
    
"""

class InterfazUsuario:

    """
Constructor de la clase:

Se inicializa la lista donde se guardaran los datos a procesar.

    """
    def __init__(self):

        self.datos = []

    """
metodo obtenerAccion:

En este menu se filtra con que actor se desea interactuar durante el
proceso.

    
    """

    def obtenerAccion(self):

        correcto = False
        while(not(correcto)):
            print "\n\n>Seleccione la acción que desea ejecutar:"
            print "1.- Manejo de clientes"
            print "2.- Manejo de productos"
            print "3.- Manejo de afiliaciones"
            print "4.- Manejo de consumos"
            print "5.- Facturacion"
            print "6.- Salir"
            seleccion = raw_input('Seleccion:')
            if(seleccion.isdigit()):
                seleccion = int(seleccion)
                correcto = ((seleccion>0) and (seleccion<7))
              
        if(int(seleccion)==6):
            sys.exit("Programa finalizado.")
        self.obtenerDatos(int(seleccion))

    """
metodo obtenerCliente:

En este menu se obtienen los datos completos del cliente.

    
    """

    def obtenerCliente(self):

        print ">Por favor, ingresa los datos principales del cliente"
        print "El cliente es:"
        print "1. Jurídico"
        print "2. Natural"
        seleccion = raw_input('Seleccion:')
        self.datos.append(int(seleccion)-1)
        if (int(seleccion)==2):
            self.datos.append(raw_input('Nombre del cliente:'))
            ci = 'a'
            while(not ci.isdigit()):
                ci = raw_input('Cédula: ')
                if (not ci.isdigit()):
                   print 'La cédula debe ser un número' 
            self.datos.append(int(ci))
            self.datos.append(raw_input('Dirección de domicilio:'))
        else:
            self.datos.append(raw_input('Nombre de la empresa:'))
            rif = raw_input('RIF: ') 
            self.datos.append(rif)
            self.datos.append(raw_input('Dirección del establecimiento:'))

    """
metodo obtenerClaveCliente:

En este menu se obtienen los datos minimos para reconocer cliente.

    
    """

    def obtenerClaveCliente(self):

        print ">Por favor, ingresa los datos principales del cliente"
        print "El cliente es:"
        print "1. Natural"
        print "2. Jurídico"
        seleccion = raw_input('Seleccion:')
        if (int(seleccion)==1):
            ci='a'
            while(not ci.isdigit()):
                ci = raw_input('Cedula:') 
                if (not ci.isdigit()):
                   print 'La cédula debe ser un número' 
            self.datos.append(int(ci))
        else:
            rif = raw_input('RIF: ') 
            self.datos.append(rif)
 
    """
metodo obtenerProducto:

En este menu se obtienen los datos completos del producto.

    
    """
       
    def obtenerProducto(self):

        print ">Por favor, ingresa los datos principales del producto a agregar"
        print "El cliente dueño del producto es:"
        print "1. Natural"
        print "2. Jurídico"
        seleccion = raw_input('Seleccion:')
        if (int(seleccion)==1):
            ci = raw_input('Cedula:') 
            self.datos.append(int(ci))
        else:
            rif = raw_input('RIF: ')
            self.datos.append(rif)
        self.datos.append(raw_input('Nombre del producto:'))
        id_emp = 'a'
        while(not id_emp.isdigit()):
                id_emp = raw_input('Identificador del producto en la empresa:')
                if (not id_emp.isdigit()):
                   print 'El identificador debe ser un número' 
        self.datos.append(int(id_emp)) 
        self.datos.append(raw_input('RIF de la empresa:'))
        self.datos.append(raw_input('Nombre del plan:'))


    """
metodo obtenerClaveProducto:

En este menu se obtienen los datos minimos para reconocer un producto.

    
    """

    def obtenerClaveProducto(self): 

        print ">Por favor, ingresa los datos principales del producto:"
        self.datos.append(raw_input('Nombre del producto:'))
        id_emp = 'a'
        while(not id_emp.isdigit()):
                id_emp = raw_input('Identificador del producto en la empresa:')
                if (not id_emp.isdigit()):
                   print 'El identificador debe ser un número' 
        self.datos.append(int(id_emp)) 
 

    """
metodo obtenerServicio:

En este menu se obtienen los datos minimos para reconocer un servicio.

    
    """        
                
    def obtenerServicio(self):  

        print ">Ahora, por favor, ingresa los datos principales del servicio que desea:"
        self.datos.append(raw_input('Nombre del servicio:'))

    def obtenerConsumo(self): 
 
        print ">Por favor, ingresa los datos del consumo"
	self.datos.append(raw_input("Ingrese la fecha del consumo de la siguiente manera: YYYY-MM-DD hh:mm:ss:"))
        costo = 'a'
        while(not costo.isdigit()):
                costo = raw_input('Identificador costo del consumo:')
                if (not costo.isdigit()):
                   print 'El costo debe ser un número positivo' 
        self.datos.append(int(costo)) 
	self.datos.append(raw_input("Ingrese el nombre del servicio:"))
	self.datos.append(raw_input("Ingrese el nombre del producto:"))
        id_emp = 'a'
        while(not id_emp.isdigit()):
                id_emp = raw_input('Identificador del producto en la empresa:')
                if (not id_emp.isdigit()):
                   print 'El identificador debe ser un número' 
        self.datos.append(int(id_emp)) 


    """
metodo obtenerFactura:

En este menu se obtienen los datos para procesar una factura.

    
    """

    def obtenerFactura(self):

        print ">Por favor, ingrese los datos necesarios para hacer el consumo"
        print "El cliente al que se facturará es:"
        print "1. Natural"
        print "2. Jurídico"
        seleccion = raw_input('Seleccion:')
        if (int(seleccion)==1):
            ci='a'
            while(not ci.isdigit()):
                ci = raw_input('Cedula:') 
                if (not ci.isdigit()):
                   print 'La cédula debe ser un número' 
            self.datos.append(int(ci))
        else:
            rif = raw_input('RIF: ')
            self.datos.append(rif)
        mes='a'
        while(not mes.isdigit()):
            mes = raw_input("Mes a facturar:") 
            if (not mes.isdigit()):
               print 'El mes debe ser un número' 
        self.datos.append(int(mes))
        anio='a'
        while(not anio.isdigit()):
            anio = raw_input("Año de la factura:") 
            if (not anio.isdigit()):
               print 'El año debe ser un número' 
        self.datos.append(int(anio))
        correcto = False
        while(not correcto):

            print "Se facturarán sus productos"
            print "1. Con plan prepago"
            print "2. Con plan postpago"
            seleccion = raw_input('Seleccion:')
            if (seleccion.isdigit()):
                seleccion = (int(seleccion))
                correcto = ((seleccion>0)and(seleccion<3))
        if(int(seleccion)==1):
            self.datos.append("pre")
        else:
            self.datos.append("pos")

    """
metodo obtenerDatos:

Este metodo tiene todo los submenus para cada actor y ofrece las 
acciones que se puede realizar.

    
    """

    def obtenerDatos(self,seleccion):

        seleccion = int(seleccion)
        print ">Qué desea hacer?"

        if(seleccion==1):
            correcto = False
            while(not correcto):            
                print "1.- Agregar un cliente"
                print "2.- Consultar la información de un cliente"
                print "3.- Regresar"
                opcion = raw_input('Seleccion:')
                if (opcion.isdigit()):
                    opcion = (int(opcion))
                    correcto = ((opcion>0)and(opcion<4))
            if(opcion==3):
                return 
            self.datos.append(int(opcion))
            if(int(opcion)==1):
                self.obtenerCliente()
            elif (int(opcion)==2):
                self.obtenerClaveCliente()           

        elif(seleccion==2):
            correcto = False
            while(not correcto): 
                print "1.-Registrar producto"
                print "2.-Buscar un producto"
                print "3.-Eliminar un producto o desafiliar un plan del producto"
                print "4.- Regresar"
                opcion = raw_input('Seleccion:')
                if (opcion.isdigit()):
                    opcion = (int(opcion))
                    correcto = ((opcion>0)and(opcion<5))
            if(opcion==4):
                return 
            self.datos.append(int(opcion)+2)
            if(int(opcion)>1):
                self.obtenerClaveProducto()
            elif(int(opcion)==1):
                self.obtenerProducto()

        elif(seleccion==3):

            correcto = False
            while(not correcto): 
                print "1.-Afiliar un producto a un plan." 
                print "2.-Afiliar un producto a un servicio."
                print "3.-Desafiliar un producto de un servicio."
                print "4.-Consultar planes asociados a un producto."
                print "5.-Consultar servicios asociados a un producto."
                print "6.- Regresar"
                opcion = raw_input('Seleccion:')
                if (opcion.isdigit()):
                    opcion = (int(opcion))
                    correcto = ((opcion>0)and(opcion<7))
            if(opcion==6):
                return 
            self.datos.append(int(opcion)+5)
            if (int(opcion)==1):
                self.obtenerProducto() 
            elif ((int(opcion)==2) or (int(opcion)==3)):
                self.obtenerClaveProducto()
                self.obtenerServicio()
            elif ((int(opcion)==4)or (int(opcion)==5)):
                self.obtenerClaveProducto()                
                

        elif(seleccion==4):

            correcto = False
            while(not correcto): 
                print "1.- Mostrar todos los consumos del producto."
                print "2.- Registrar un consumo de un producto"
                print "3.- Regresar"
                opcion = raw_input('Seleccion:')
                if (opcion.isdigit()):
                    opcion = (int(opcion))
                    correcto = ((opcion>0)and(opcion<4))
            if(opcion==3):
                return 
            self.datos.append(int(opcion)+10)

            if (int(opcion)==1):
                self.obtenerClaveProducto()
            elif (int(opcion)==2):
                self.obtenerConsumo()

        elif(seleccion==5):

            correcto = False
            while(not correcto): 
                print "1.-Facturar a un cliente"
                print "2.- Regresar"
                opcion = raw_input('Seleccion:')
                if (opcion.isdigit()):
                    opcion = (int(opcion))
                    correcto = ((opcion>0)and(opcion<3))
            if(opcion==2):
                return 
            self.datos.append(int(opcion)+12) 
            if(int(opcion)==1):

                self.obtenerFactura()     


    """
metodo obtenerConexion:

En este menu se obtienen los datos necesarios para hacer la conexion
con la base de datos.

    
    """

    def obtenerConexion(self):

        bdname=raw_input("Introduzca nombre de la base de datos:")
        username=raw_input("Introduzca su username:")
        password=raw_input("Introduzca su password:")
        self.datos = [bdname, password, username]



    #Se obtiene la lista con los datos completos
    def getDatos(self):

        return self.datos 

