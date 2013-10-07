# -*- coding: iso-8859-15 -*-

import DBhandler as D
import Consumo as C
import Adiciona as A
import Servicio as S
import Incluidos_plan as IP
import Incluidos_sextras as IS
import Plan as PL
import Cliente as CL
import Producto as P
import Factura as F
"""
Clase Empresa:
Encargada de todas las funcionalidades del programa.
Cumple con las tareas de una fachada.

Elaborada por Juan A. Escalante
"""


class Empresa:

    """
Constructor de la clase
Contiene la inicializacion de todas las listas a ser cargadas
desde la base de datos, cuya conexion tambien se inicializa.

    """
    def __init__(self, datosBD):

        self.manejador= D.DB_Handler()
        self.manejador.Establecer_Conexion(datosBD[0],datosBD[1],datosBD[2])
        self.listaCliente = []
        self.listaProducto = []
        self.listaAdiciona = []
        self.listaConsumo = []
        self.listaServicio = []
        self.listaPlan= []
        self.listaIncluidoPlan = []
        self.listaIncluidoServicio = []

    """
Metodo cargar:

Llamado desde el main para inializar todas las listas y tener 
toda la informacion en memoria.

    """

    def cargar(self):

        self.cargarCliente()
        self.cargarProducto()
        self.cargarConsumo()
        self.cargarServicio()
        self.cargarPlan()
        self.cargarAdiciona()
        self.cargarIncluidoPlan()
        self.cargarIncluidoServicio()
 
    """
Metodo cargarCliente:

Encargada de la carga de todos los clientes presentes en la base de datos.

    """ 

    def cargarCliente(self):

        clientes = self.manejador.cargarCliente()
        for cl in clientes:
            if ('cedula' in cl):
                 cliente = CL.Cliente(str(cl['direccion']),1,int(cl['cedula']),str(cl['nombre'])) 
            else:
                 cliente = CL.Cliente(str(cl['direccion']),0,str(cl['rif']), str(cl['nombre'])) 
            self.listaCliente.append(cliente)

    """
Metodo cargarProducto:

Encargada de la carga de todos los productos presentes en la base de datos.

    """ 
      
    def cargarProducto(self):

        productos = self.manejador.cargarProducto()
        for p in productos:
            producto = P.Producto(p['id_cliente'],p['idn'],p['nombre'],p['nombre_plan'],p['renta'],p['rif_em'], p['saldo']) 
            self.listaProducto.append(producto) ##

    """
Metodo cargarAdiciona:

Encargada de la carga de todos los adiciona presentes en la base de datos.
Adiciona contiene la afiliacion de un producto con un servicio extra.

    """ 

    def cargarAdiciona(self):

        tablaadiciona = self.manejador.cargarAdiciona()
	for a in tablaadiciona:
            ad = A.Adiciona(a['id_producto'], a['nombre_producto'], a['nombre_servicio'])
            self.listaAdiciona.append(ad)  ##

    """
Metodo cargarConsumo:

Encargada de la carga de todos los consumos presentes en la base de datos.

    """ 

    def cargarConsumo(self):

	consumos = self.manejador.cargarConsumo()
	for c in consumos:
            con = C.Consumo(c['costo'],c['descripcion'],c['fecha'],c['id_producto'], c['nombre_producto']) 
            self.listaConsumo.append(con) 


    """
Metodo cargarServicio:

Encargada de la carga de todos los servicios extras a 
ofrecer presentes en la base de datos.

    """ 

    def cargarServicio(self):

	servicios = self.manejador.cargarServicio()
	for s in servicios:
            serv = S.Servicio(s['costo'], s['nombre']) 
            self.listaServicio.append(serv) 

    """
Metodo cargarPlan:

Encargada de la carga de todos los planes a ofrecer presentes en la base de datos.

    """ 

    def cargarPlan(self):

        planes = self.manejador.cargarPlan()
        for pl in planes:
            if (len(pl)==5):
                plan = PL.Plan(pl['descripcion'],pl['ilimitado'],pl['nombre'],pl['renta'],pl['rif_empresa'])
            if (len(pl)==4):
                plan = PL.Plan(pl['descripcion'], 2, pl['nombre'], pl['renta'], pl['rif_empresa']) ##
            self.listaPlan.append(plan)


    """
Metodo cargarIncluidoPlan:

Encargada de la carga de todos los consumos incluidos en los 
planes a ofrecer presentes en la base de datos.

    """ 

    def cargarIncluidoPlan(self):

	iplanes = self.manejador.cargarIncluidoPlan()
	for ip in iplanes:
            iplan = IP.IncluidoPlan(ip['cantidad'], ip['nombre'],ip['rif_empresa'], ip['tipo']) ## 
            self.listaIncluidoPlan.append(iplan)


    """
Metodo cargarIncluidoServicio:

Encargada de la carga de todos los consumos incluidos en los 
servicios a ofrecer presentes en la base de datos.

    """  

    def cargarIncluidoServicio(self):

        iservicios = self.manejador.cargarIncluidoServicio()
	for iserv in iservicios:
            iservicio = IS.IncluidoServicio(iserv['cantidad'], iserv['nombre_sextr'], iserv['tipo']) ##
            self.listaIncluidoServicio.append(iservicio)

    """
Metodo verificarCliente:

Verifica si un cliente puede ser agregado, es decir, que no existe en
las listas previamente.

    """ 


    def verificarCliente(self, cliente):

        tamano = len(self.listaCliente)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaCliente[i]==cliente)
            i=i+1

        return (not existe)

    """
Metodo verificarProducto:

Verifica si un producto puede ser agregado, es decir, que no existe en
las listas previamente.

    """

    def verificarProducto(self, producto):

        tamano = len(self.listaProducto)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaProducto[i]==producto)
            i=i+1

        return (not existe)

    """
Metodo verificarConsumo:

Verifica si un consumo puede ser agregado, es decir, que no existe en
las listas previamente.

    """

    def verificarConsumo(self, consumo):

        tamano = len(self.listaConsumo)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaConsumo[i]==consumo)
            i=i+1

        return (not existe)

    """
Metodo verificarServicio:

Verifica si un servicio puede ser afiliado, es decir, que existe en
las listas previamente.

    """

    def verificarServicio(self, servicio):

        tamano = len(self.listaServicio)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaServicio[i]==servicio)
            i=i+1

        return (not existe)

    """
Metodo verificarPlan:

Verifica si un plan puede ser afiliado, es decir, que existe en
las listas previamente.

    """

    def verificarPlan(self, plan):

        tamano = len(self.listaPlan)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaPlan[i]==plan)
            i=i+1

        return (not existe)

    """
Metodo verificarAdiciona:

Verifica si un servicio ya no ha sido afiliado a producto, es decir, que existe en
las listas previamente.

    """

    def verificarAdiciona(self, adiciona):

        tamano = len(self.listaAdiciona)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaAdiciona[i]==adiciona)
            i=i+1

        return (not existe)

    """
Metodo agregarCliente:

Agrega un cliente verificado a la lista de clientes y a la base 
de datos configurada. El programa queda actualizado al momento para 
la siguiente accion.

    """

    def agregarCliente(self,cliente):

        cliente.agregar(self.manejador)
        self.listaCliente.append(cliente)
        

    """
Metodo agregarProducto:

Agrega un producto verificado a las lista de productos y a la base 
de datos configurada. El programa queda actualizado al momento para 
la siguiente accion.

    """

    def agregarProducto(self, producto):

        producto.agregar(self.manejador)
        self.listaProducto.append(producto)

    """
Metodo agregarConsumo:

Agrega un consumo verificado a la lista de consumos y a la base 
de datos configurada. El programa queda actualizado al momento para 
la siguiente accion.

    """

    def agregarConsumo(self, consumo):

        consumo.agregar(self.manejador)
        self.listaConsumo.append(consumo)

    """
Metodo agregarAdiciona:

Agrega una afiliacion de servicio verificada a la lista de afiliaciones
 y a la base de datos configurada. El programa queda actualizado
 al momento para la siguiente accion.

    """

    def agregarAdiciona(self, adiciona):

        adiciona.agregar(self.manejador)
        self.listaAdiciona.append(adiciona)

    """
Metodo eliminarProducto:

Elimina un producto del sistema incluyendo todas sus interacciones.

    """

    def eliminarProducto(self, producto):

        self.eliminarConsumo(producto)
        self.eliminarAdiciona(producto)
        tamano = len(self.listaProducto)
        encontrado= False
        i=0
        while((i<tamano)and(not(encontrado))):

            if (self.listaProducto[i]==producto):
                self.listaProducto[i].eliminar(self.manejador)
                del self.listaProducto[i]
                encontrado = True
            i=i+1      

    """
Metodo eliminarConsumo:

Elimina todos los consumos de un producto dado del sistema.

    """

    def eliminarConsumo(self, producto):

        for consumo in self.listaConsumo:

           if((producto.getNombre()==consumo.getNombre_Producto()) \
               and (producto.getIdn()==consumo.getId_Producto())): ##ojo con los gets
              
                consumo.eliminar(self.manejador)
                del consumo    

    """
Metodo eliminarAdiciona:

Elimina todas las afiliaciones de un producto dado del sistema.

    """
    
    def eliminarAdiciona(self, producto):    

        for adiciona in self.listaAdiciona:

           if((producto.getNombre()==adiciona.getNombre_Producto()) \
               and (producto.getIdn()==adiciona.getId_Producto())): ##ojo con los gets
              
                adiciona.eliminar(self.manejador)
                del adiciona

    """
Metodo desafiliarServicio:

Elimina una afiliacion de un servicio a un producto del sistema.

    """

    def desafiliarServicio(self, adiciona):

        tamano = len(self.listaAdiciona)
        encontrado= False
        i=0
        while((i<tamano)and(not(encontrado))):

            if (self.listaAdiciona[i]==adiciona):
                self.listaAdiciona[i].eliminar(self.manejador)
                del self.listaAdiciona[i]
                
                encontrado = True
            i=i+1

    """
Metodo consultarCliente:

Muestra en pantalla la informacion principal de un cliente.

    """         

    def consultarCliente(self,cliente):

        tamano = len(self.listaCliente)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaCliente[i]==cliente)
            i=i+1
        if (existe):
	    cl = self.listaCliente[i-1]
            print "Cliente: "+cl.getNombre()+", Dirección: "+cl.getDireccion()
        else:
            print "El cliente no existe"

    """
Metodo consultarProducto:

Muestra en pantalla la informacion principal de un producto.

    """

    def consultarProducto(self,producto):

        tamano = len(self.listaProducto)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaProducto[i]==producto)
            i=i+1
        if (existe):
            self.listaProducto[i-1].imprimir()
            
        else:
            print "El producto no existe"

    """
Metodo consultarPlanProducto:

Muestra en pantalla la informacion principal del plan afiliado
a un producto dado.

    """
     
    def consultarPlanProducto(self, producto):
 
        tamano = len(self.listaProducto)
        existe= False
        i=0
        
        while((i<tamano)and(not(existe))):

            existe = (self.listaProducto[i]==producto)
            i=i+1    
        if (existe):
            print "El producto tiene asociado el plan: \""+self.listaProducto[i-1].getNombre_Plan()+"\""
        #existe obligatoriamente

    """
Metodo consultarServiciosProducto:

Muestra en pantalla la informacion principal de los servicios afiliados
a un producto dado.

    """

    def consultarServiciosProducto(self, producto):
	
        existe =False
        for serv in self.listaAdiciona:

            if ((serv.getNombre_Producto()==producto.getNombre()) \
            and (serv.getId_Producto()==producto.getIdn())): 
                print serv.getNombre_Servicio()
                existe = True

        if(not(existe)):

            print "\nNo hay servicios afiliados con el producto \n"

    """
Metodo consultarConsumosProducto:

Muestra en pantalla la informacion principal de los consumos realizados
por un producto dado.

    """

    def consultarConsumosProducto(self, producto):

        existe = False
        for consumo in self.listaConsumo:

            if ((consumo.getNombre_Producto()==producto.getNombre()) \
            and (consumo.getId_Producto()==producto.getIdn())): 
                consumo.imprimir()
                existe = True

        if(not(existe)):

            print "\nNo hay consumos realizados con el producto indicado \n"

    """
Metodo buscarCLiente:

Devuelve la informacion completa de un cliente dado.

    """

    def buscarCliente(self, cliente):

        for cl in self.listaCliente:

            if (cl==cliente):
                return cl

    """
Metodo filtrarProducto:

Devuelve los productos asociados a un cliente dado.

    """

    def filtrarProducto(self, cliente):

        prodfiltrados = []
        for p in self.listaProducto:

            if(p.getId_Cliente()==cliente.getIde()): ##ojo gets
     
                prodfiltrados.append(p)

        return prodfiltrados

    """
Metodo filtrarPlan:

Devuelve los planes asociados a los productos de un cliente.

    """

    def filtrarPlan(self, listproductos):
         
        planfiltrados= []
        for p in listproductos:

            tamano= len(self.listaPlan)
            i=0
            encontrado = False
            while((i<tamano)and(not(encontrado))):

                if ((p.getNombre_Plan()==self.listaPlan[i].getNombre()) and (p.getRif_Empresa()==self.listaPlan[i].getRif_Empresa())): ##ojo gets plan
                  
                    planfiltrados.append(self.listaPlan[i])
                    encontrado = True
		i=i+1

        return planfiltrados


    """
Metodo filtrarConsumo:

Devuelve los consumos realizados por los productos de un cliente en un
mes y anio especifico.

    """

    def filtrarConsumo(self, listaproductos, mes, anio):

       consumofiltrados = []
       for p in listaproductos:

          for c in self.listaConsumo:
                                                 ####MEGA OJO ACA gets
            if((p.getNombre()==c.getNombre_Producto())and(p.getIdn()==c.getId_Producto())and \
                  (mes==int(c.getFecha()[5:7])) and (anio==int(c.getFecha()[0:4]))):
		    

                    consumofiltrados.append(c)

       return consumofiltrados

    """
Metodo filtrarAdiciona:

Devuelve las afiliaciones a servicios de los productos de 
un cliente dado.

    """

    def filtrarAdiciona(self, listaproductos):

        adicionafiltrados = []
        for p in listaproductos:

           for a in self.listaAdiciona:
                                                
                if((p.getNombre()==a.getNombre_Producto())and(p.getIdn()==a.getId_Producto())):

                    adicionafiltrados.append(a)

        return adicionafiltrados

    """
Metodo filtrarServicio:

Devuelve los servicios afiliados a los productos de un cliente dado.

    """

    def filtrarServicio(self, listaadiciona):

        serviciofiltrados = []
        for a in listaadiciona:

           for s in self.listaServicio:
                                                  
                if(a.getNombre_Servicio()==s.getNombre()):

                    serviciofiltrados.append(s)

        return serviciofiltrados

    """
Metodo filtrarIncluidoPlan:

Devuelve los servicios incluidos en los planes asociados a los productos de un
 cliente dado.

    """

    def filtrarIncluidoPlan(self, listaplan):

        iplanfiltrados = []
        for p in listaplan:

           for ip in self.listaIncluidoPlan:
                                                 
                if ((p.getNombre()==ip.getNombre()) and \
                   (p.getRif_Empresa()==ip.getRif_Empresa())): 
                  
                    iplanfiltrados.append(ip)

        return iplanfiltrados

    """
Metodo filtrarIncluidoServicio:

Devuelve los servicios consumibles incluidos en los servicios extras
asociados a los productos de un cliente dado.

    """
    def filtrarIncluidoServicio(self, listaservicio):

        iserviciofiltrados = []
        for s in listaservicio:

           for iserv in self.listaIncluidoServicio:
                                                 ##OJO aca gets y 
                if (s.getNombre()==iserv.getNombre_Sextr()): ##ojo gets servicio
                  
                    iserviciofiltrados.append(iserv)
        return iserviciofiltrados

    """
Metodo obtenerRenta:

Devuelve la renta de un plan dado. 

    """

    def obtenerRenta(self,plan):

        for pl in self.listaPlan:

            if ((plan.getNombre()==pl.getNombre()) and \
               (plan.getRif_Empresa()== pl.getRif_Empresa())):

                return pl.getRenta() 
    """
Metodo procesar:

Metodo que toma las decisiones de todas las acciones del programa 
por la solicitud del usuario a traves de la interfaz.

Sus acciones estan definidas y separadas segun la peticion del usuario.

    """
    def procesar(self,datos):

	if (len(datos)==0):
	  return
	  
        if(datos[0]==1): #agregar cliente

            cliente = CL.Cliente(datos[4], datos[1], datos[3], datos[2]) # 1-esnat 2-nom 3-ide 4-direccion
            if(self.verificarCliente(cliente)):

                self.agregarCliente(cliente)
            
        elif(datos[0]==2): #consultar cliente

            cliente = CL.Cliente('','', datos[1], '')
            cliente.setIde(datos[1])      ##ojo aca
            self.consultarCliente(cliente)

        elif((datos[0]==3)or(datos[0]==6)): #agregar producto   #1-idcl 2-nompr 3idp 4rif 5nompl
                                   
            producto = P.Producto(datos[1],datos[3],datos[2],datos[5],None,datos[4], 0)  
           
            plan = PL.Plan(None,None,datos[5],None,datos[4])
            producto.setRenta(self.obtenerRenta(plan))
            if (self.verificarPlan(plan)):
                print 'No existe el plan'
                return 
            
            cliente = CL.Cliente('', '',datos[1],'')  
            if (self.verificarCliente(cliente)):
               print 'No existe cliente'
               return
            
            if (self.verificarProducto(producto)):

                self.agregarProducto(producto)
                print "El producto se ha agregado con exito"
            else:
		print "El producto ya existe"
 
        elif(datos[0]==4): #consultar producto  #1-nompr 2-idn
	    
            producto = P.Producto(None,datos[2],datos[1],None,None,None, None)
            self.consultarProducto(producto)  

        elif(datos[0]==5): #eliminar producto #1-nompr 2-idn 

            producto = P.Producto(None,datos[2],datos[1],None,None,None, None)
            if(not(self.verificarProducto(producto))):
                
                self.eliminarProducto(producto)
		print "El producto se ha eliminado con éxito"

            else:

                print 'No existe el producto'


        elif(datos[0]==7): #afiliar producto/servicio #1-nompr 2-idn 3-nomserv
        
            producto = P.Producto(None,datos[2],datos[1],None,None,None,None) 
            if(self.verificarProducto(producto)):
                print 'No existe el producto'
                return

            servicio = S.Servicio(None, datos[3])
            
            if(not(self.verificarServicio(servicio))):

                adiciona = A.Adiciona(datos[2], datos[1], datos[3]) 
                self.agregarAdiciona(adiciona)
                print "El producto se ha afiliado con exito"
            else:
                print 'No existe el servicio'

        elif(datos[0]==8): #desafiliar producto/servicio #1-nompr 2-idn 3-nomserv
        
            producto = P.Producto(None,datos[2],datos[1],None,None,None,None) 
            if(self.verificarProducto(producto)):

                print 'No existe el producto'
                return

            servicio = S.Servicio(None, datos[3])
            
            if(not(self.verificarServicio(servicio))):

                adiciona = A.Adiciona(datos[2], datos[1], datos[3]) 
                self.desafiliarServicio(adiciona)
                print "El producto se ha desafiliado con éxito"
            else:
                print 'No existe el servicio'
            


        elif(datos[0]==9): #consultar plan/producto   #1-nompr 2-idn    
            
            producto = P.Producto(None,datos[2],datos[1],None,None,None,None)

            if(not(self.verificarProducto(producto))):
		
                self.consultarPlanProducto(producto)

        elif(datos[0]==10): #consultar servicios/producto #1-nompr 2-idn 

            producto = P.Producto(None,datos[2],datos[1],None,None,None,None)
            if(not(self.verificarProducto(producto))):

                self.consultarServiciosProducto(producto)

        elif(datos[0]==11): #consultar consumos/producto #1-nompr 2-idn 

            producto = P.Producto(None,datos[2],datos[1],None,None,None,None)

            if(not(self.verificarProducto(producto))):

                self.consultarConsumosProducto(producto)
            else:
	      print "Los datos introducidos son inválidos, debe ser un producto existente"

        elif(datos[0]==12): #agregar consumo

            producto = P.Producto(None,datos[5],datos[4],None,None,None,None)
            if(self.verificarProducto(producto)):
                                                 #1-fecha 2-costo 3-serv 4-nomp 5-idnp
                print 'No existe el producto'
                return
            consumo = C.Consumo(datos[2],datos[3],datos[1],datos[5], datos[4])
            if(self.verificarConsumo(consumo)):
                
                self.agregarConsumo(consumo) 
		print "Se ha agregado el consumo"
            else: 

                print 'Ya este consumo fue registrado'

        elif(datos[0]==13): #facturar 


            cliente = CL.Cliente('','',datos[1],'')
            if(self.verificarCliente(cliente)):
                print 'No existe el cliente'
                return
            cliente = self.buscarCliente(cliente)
            productosfiltrados= self.filtrarProducto(cliente)
            planesfiltrados = self.filtrarPlan(productosfiltrados)
            consumosfiltrados = self.filtrarConsumo(productosfiltrados, \
                                datos[2], datos[3]) ##2mes-3anio
            adicionafiltrados = self.filtrarAdiciona(productosfiltrados)
            serviciofiltrados = self.filtrarServicio(adicionafiltrados)
            iplanfiltrados= self.filtrarIncluidoPlan(planesfiltrados)
            iserviciofiltrados = self.filtrarIncluidoServicio(serviciofiltrados)
            factura = F.Factura()
            factura.facturar(cliente,adicionafiltrados,consumosfiltrados,iplanfiltrados,iserviciofiltrados,planesfiltrados, \
                             productosfiltrados,serviciofiltrados ,datos[2],datos[3],datos[4]) #4-pre o pos  
            factura.imprimir()

            

            

