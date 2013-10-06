# -*- coding: iso-8859-15 -*-

class InterfazUsuario:

    def __init__(self):

        self.datos = []

    def obtenerAccion(self):
        
        print "\n\n>Seleccione la acción que desea ejecutar:"
        print "1.- Manejo de clientes"
        print "2.- Manejo de productos"
        print "3.- Manejo de afiliaciones"
        print "4.- Manejo de consumos"
        print "5.- Facturacion"
        
        self.obtenerDatos(raw_input('Seleccion:'))

    def obtenerCliente(self):

        print ">Por favor, ingresa los datos principales del cliente"
        print "El cliente es:"
        print "1. Natural"
        print "2. Jurídico"
        seleccion = raw_input('Seleccion:')
        self.datos.append(seleccion)
        if (int(seleccion)==1):
            self.datos.append(raw_input('Nombre del cliente:'))
            ci = raw_input('Cédula: ') ##verificacion
            self.datos.append(int(ci))
            self.datos.append(raw_input('Dirección de domicilio:'))
        else:
            self.datos.append(raw_input('Nombre de la empresa:'))
            rif = raw_input('RIF: ') 
            self.datos.append(rif)
            self.datos.append(raw_input('Dirección del establecimiento:'))

    def obtenerClaveCliente(self):

        print ">Por favor, ingresa los datos principales del cliente"
        print "El cliente es:"
        print "1. Natural"
        print "2. Jurídico"
        seleccion = raw_input('Seleccion:')
        if (int(seleccion)==1):
            ci = raw_input('Cedula:') ##verificacion
            self.datos.append(int(ci))
        else:
            rif = raw_input('RIF: ') 
            self.datos.append(rif)
        
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
        self.datos.append(int(raw_input('Identificador del producto en la empresa:'))) ##verifcacion numerica
        self.datos.append(raw_input('RIF de la empresa:'))
        self.datos.append(raw_input('Nombre del plan:'))

    def obtenerClaveProducto(self): 

        print ">Por favor, ingresa los datos principales del producto:"
        self.datos.append(raw_input('Nombre del producto:'))
        self.datos.append(int(raw_input('Identificador del producto en la empresa:'))) ##verifcacion numerica
                
    def obtenerServicio(self):  

        print ">Ahora, por favor, ingresa los datos principales del servicio que desea:"
        self.datos.append(raw_input('Nombre del servicio:'))

    def obtenerConsumo(self): 
 
        print ">Por favor, ingresa los datos del consumo"
	self.datos.append(raw_input("Ingrese la fecha del consumo de la siguiente manera: DD-MM-YYYY hh:mm:ss:"))
	self.datos.append(int(raw_input("Ingrese el costo"))) ##numerico
	self.datos.append(raw_input("Ingrese el nombre del servicio:"))
	self.datos.append(raw_input("Ingrese el nombre del producto"))
	self.datos.append(int(raw_input("Ingrese el idn del producto"))) #numerico


    def obtenerFactura(self):

        print ">Por favor, ingrese los datos necesarios para hacer el consumo"
        print "El cliente al que se facturará es:"
        print "1. Natural"
        print "2. Jurídico"
        seleccion = raw_input('Seleccion:')
        if (int(seleccion)==1):
            ci = raw_input('Cedula:') ##verificacion
            self.datos.append(ci)
        else:
            rif = raw_input('RIF: ')
            self.datos.append(rif)
	self.datos.append(raw_input("Mes a facturar:")) #numerico
	self.datos.append(raw_input("Año de la factura:")) ##numerico
        print "Se facturarán sus productos"
        print "1. Con plan prepago"
        print "2. Con plan postpago"
        seleccion = raw_input('Seleccion:')
        if(int(seleccion)==1):
            self.datos.append("pre")
        else:
            self.datos.append("pos")

    def obtenerDatos(self,seleccion):

        seleccion = int(seleccion)
        print ">Qué desea hacer?"

        if(seleccion==1):
            
            print "1.- Agregar un cliente"
            print "2.- Consultar la información de un cliente"
            opcion = raw_input('Seleccion:')
            self.datos.append(int(opcion))
            if(int(opcion)==1):
                self.obtenerCliente()
            elif (int(opcion)==2):
                self.obtenerClaveCliente()           

        elif(seleccion==2):

            print "1.-Registrar producto"
            print "2.-Buscar un producto"
            print "3.-Eliminar un producto o desafiliar un plan del producto"
            opcion = raw_input('Seleccion:')
            self.datos.append(int(opcion)+2)
            if(int(opcion)>1):
                self.obtenerClaveProducto()
            elif(int(opcion)==1):
                self.obtenerProducto()

        elif(seleccion==3):

            print "1.-Afiliar un producto a un plan." 
            print "2.-Afiliar un producto a un servicio."
            print "3.-Desafiliar un producto de un servicio."
            print "4.-Consultar planes asociados a un producto."
            print "5.-Consultar servicios asociados a un producto."
            opcion = raw_input('Seleccion:')
            self.datos.append(int(opcion)+5)

            if (int(opcion)==1):
                self.obtenerProducto() 
            elif ((int(opcion)==2) or (int(opcion)==3)):
                self.obtenerClaveProducto()
                self.obtenerServicio()
            elif ((int(opcion)==4)or (int(opcion)==5)):
                self.obtenerClaveProducto()                
                

        elif(seleccion==4):

            print "1.- Mostrar todos los consumos del producto."
            print "2.- Registrar un consumo de un producto"
            opcion = raw_input('Seleccion:')
            self.datos.append(int(opcion)+10)

            if (int(opcion)==1):
                self.obtenerClaveProducto()
            elif (int(opcion)==2):
                self.obtenerConsumo()

        elif(seleccion==5):

            print "1.-Facturar a un cliente"
            opcion = raw_input('Seleccion:')
            self.datos.append(int(opcion)+12) 
       
            if(int(opcion)==1):

                self.obtenerFactura()     

    def obtenerConexion(self):

        bdname=raw_input("Introduzca nombre de la base de datos:")
        username=raw_input("Introduzca su username:")
        password=raw_input("Introduzca su password:")
        self.datos = [bdname, password, username]

    def getDatos(self):

        return self.datos 

