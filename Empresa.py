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

class Empresa:


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

    def cargar(self):

        self.cargarCliente()
        self.cargarProducto()
        self.cargarConsumo()
        self.cargarServicio()
        self.cargarPlan()
        self.cargarAdiciona()
        self.cargarIncluidoPlan()
        self.cargarIncluidoServicio()
  

    def cargarCliente(self):

        clientes = self.manejador.cargarCliente()
        for cl in clientes:
            if ('cedula' in cl):
                 cliente = CL.Cliente(str(cl['direccion']),1,int(cl['cedula']),str(cl['nombre'])) 
            else:
                 cliente = CL.Cliente(str(cl['direccion']),0,str(cl['rif']), str(cl['nombre'])) 
            self.listaCliente.append(cliente)
      
    def cargarProducto(self):

        productos = self.manejador.cargarProducto()
        for p in productos:
            producto = P.Producto(p['id_cliente'],p['idn'],p['nombre'],p['nombre_plan'],p['renta'],p['rif_em'], p['saldo']) 
            self.listaProducto.append(producto) ##

    def cargarAdiciona(self):

        tablaadiciona = self.manejador.cargarAdiciona()
	for a in tablaadiciona:
            ad = A.Adiciona(a['id_producto'], a['nombre_producto'], a['nombre_servicio'])
            self.listaAdiciona.append(ad)  ##

    def cargarConsumo(self):

	consumos = self.manejador.cargarConsumo()
	for c in consumos:
            con = C.Consumo(c['costo'],c['descripcion'],c['fecha'],c['id_producto'], c['nombre_producto']) 
            self.listaConsumo.append(con) ##


    def cargarServicio(self):

	servicios = self.manejador.cargarServicio()
	for s in servicios:
            serv = S.Servicio(s['costo'], s['nombre']) 
            self.listaServicio.append(serv) ##

    def cargarPlan(self):


        planes = self.manejador.cargarPlan()
        for pl in planes:
            if (len(pl)==5):
                plan = PL.Plan(pl['descripcion'],pl['nombre'],pl['ilimitado'],pl['renta'],pl['rif_empresa'])
            if (len(pl)==4):
                plan = PL.Plan(pl['descripcion'], pl['nombre'], 2, pl['renta'], pl['rif_empresa']) ##
            self.listaPlan.append(plan)


    def cargarIncluidoPlan(self):

	iplanes = self.manejador.cargarIncluidoPlan()
	for ip in iplanes:
            iplan = IP.IncluidoPlan(ip['cantidad'], ip['nombre'],ip['rif_empresa'], ip['tipo']) ## 
            self.listaIncluidoPlan.append(iplan)



    def cargarIncluidoServicio(self):

        iservicios = self.manejador.cargarIncluidoServicio()
	for iserv in iservicios:
            iservicio = IS.IncluidoPlan(iserv['cantidad'], iserv['nombre_sextr'], iserv['tipo']) ##
            self.listaIncluidoPlan.append(iservicio)


    def verificarCliente(self, cliente):

        tamano = len(self.listaCliente)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaCliente[i]==cliente)
            i=i+1

        return (not existe)


    def verificarProducto(self, producto):

        tamano = len(self.listaProducto)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaProducto[i]==producto)
            i=i+1

        return (not existe)

    def verificarConsumo(self, consumo):

        tamano = len(self.listaConsumo)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaConsumo[i]==consumo)
            i=i+1

        return (not existe)

    def verificarServicio(self, servicio):

        tamano = len(self.listaServicio)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaServicio[i]==servicio)
            i=i+1

        return (not existe)


    def verificarPlan(self, plan):

        tamano = len(self.listaPlan)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaPlan[i]==plan)
            i=i+1

        return (not existe)

    def verificarAdiciona(self, adiciona):

        tamano = len(self.listaAdiciona)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaAdiciona[i]==adiciona)
            i=i+1

        return (not existe)


    def agregarCliente(self,cliente):

        cliente.agregar(self.manejador)
        self.listaCliente.append(cliente)
        

    def agregarProducto(self, producto):

        producto.agregar(self.manejador)
        self.listaProducto.append(producto)

    def agregarConsumo(self, consumo):

        consumo.agregar(self.manejador)
        self.listaConsumo.append(consumo)

    def agregarAdiciona(self, adiciona):

        adiciona.agregar(self.manejador)
        self.listaAdiciona.append(adiciona)

    def eliminarProducto(self, producto):

        self.eliminarConsumo(producto)
        self.eliminarAdiciona(producto)
        tamano = len(self.listaProducto)
        encontrado= False
        i=0
        while((i<tamano)and(not(encontrado))):

            if (self.listaProducto[i]==producto):
                listaProducto[i].eliminar(self.manejador)
                del listaProducto[i]
                encontrado = True
            i=i+1      

    def eliminarConsumo(self, producto):

        for consumo in self.listaConsumo:

           if((producto.getNombre_Producto()==consumo.getNombre_Producto()) \
               and (producto.getId()==consumo.getId())): ##ojo con los gets
              
                consumo.eliminar(self.manejador)
                del consumo    
    
    def eliminarAdiciona(self, producto):    

        for adiciona in self.listaAdiciona:

           if((producto.getNombre_Producto()==adiciona.getNombre_Producto()) \
               and (producto.getId()==adiciona.getId())): ##ojo con los gets
              
                adiciona.eliminar(self.manejador)
                del adiciona

    def desafiliarServicio(self, adiciona):

        tamano = len(self.listaAdiciona)
        encontrado= False
        i=0
        while((i<tamano)and(not(encontrado))):

            if (listaAdiciona[i]==adiciona):
                listaAdiciona[i].eliminar(self.manejador)
                del listaProducto[i]
                encontrado = True
            i=i+1

         

    def consultarCliente(self,cliente):

        tamano = len(self.listaCliente)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = (self.listaCliente[i]==cliente)
            i=i+1
        if (existe):
            print self.listaCliente[i-1]
        else:
            print "El cliente no existe"


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
     
    def consultarPlanProducto(self, producto):
 
        tamano = len(self.listaPlan)
        existe= False
        i=0
        while((i<tamano)and(not(existe))):

            existe = ((self.listaProducto[i].getnombre()==producto.getNombre()) \
                     and (self.listaProducto[i].getIdn()==producto.getIdn()))
            i=i+1    ##ojo con los gets
        if (existe):
            print listaProducto[i-1]
        #existe obligatoriamente

    def consultarServiciosProducto(self, producto):

        existe =False
        for serv in self.listaServicio:

            if ((serv.getnombre()==producto.getNombre()) \
            and (serv.getIdn()==producto.getIdn())): ##ojo con los gets
                print serv
                existe = True

        if(not(existe)):

            print "\nNo hay servicios afiliados con el producto \n"

    def consultarConsumosProducto(self, producto):

        existe = False
        for consumo in self.listaConsumo:

            if ((consumo.getnombre()==producto.getNombre()) \
            and (consumo.getIdn()==producto.getIdn())): ##ojo con los gets
                print serv
                existe = True

        if(not(existe)):

            print "\nNo hay consumos realizados con el producto indicado \n"

    def buscarCliente(self, cliente):

        for cl in self.listaCliente:

            if (cl==cliente):
                return cl

    def filtrarProducto(self, cliente):

        prodfiltrados = []
        for p in self.listaProducto:

            if(p.getIde()==cliente.getIde()): ##ojo gets
     
                prodfiltrados.append(p)

        return prodfiltrados

    def filtrarPlan(self, listaproductos):
         
        planfiltrados= []
        for p in listproductos:

            tamano= len(self.listaPlan)
            i=0
            encontrado = False
            while((i<tamano)and(not(encontrado))):

                if ((p.getNombre()==self.listaPlan[i].getNombre()) and \
                   (p.getrif()==self.listaPlan[i].getrif())): ##ojo gets plan
                  
                    planfiltrados.append(self.listaPlan[i])
                    encontrado = True

        return planfiltrados

    def filtrarConsumo(self, listaproductos, mes, anio):

        consumofiltrados = []
        for p in listaproductos:

           for c in self.listaConsumo:
                                                 ####MEGA OJO ACA gets
                if((p.getNombre()==c.getNombre())and(p.getIdn()==c.getIdn())and \
                  (mes==c.getFecha()[3:5]) and (anio==c.getFecha()[6:10])):

                    consumofiltrados.append(c)

        return consumofiltrados


    def filtrarAdiciona(self, listaproductos):

        adicionafiltrados = []
        for p in listaproductos:

           for a in self.listaAdiciona:
                                                 ##OJO aca gets y 
                if((p.getNombre()==a.getNombre())and(p.getIdn()==a.getIdn())):

                    adicionafiltrados.append(a)

        return adicionafiltrados

    def filtrarServicio(self, listaadiciona):

        serviciofiltrados = []
        for a in listaadiciona:

           for s in self.listaServicio:
                                                 ##OJO aca gets y 
                if(a.getNombreS()==s.getNombreS()):

                    serviciofiltrados.append(s)

        return serviciofiltrados

    def filtrarIncluidoPlan(self, listaPlan):

        iplanfiltrados = []
        for p in listaplan:

           for ip in self.listaIncluidoPlan:
                                                 ##OJO aca gets y 
                if ((p.getNombre()==ip.getNombre()) and \
                   (p.getrif()==ip.getrif())): ##ojo gets
                  
                    iplanfiltrados.append(ip)

        return iplanfiltrados


    def filtrarIncluidoServicio(self, listaServicio):

        iserviciofiltrados = []
        for s in listaplan:

           for iserv in self.listaIncluidoPlan:
                                                 ##OJO aca gets y 
                if (s.getNombre()==iserv.getNombre()): ##ojo gets servicio
                  
                    iserviciofiltrados.append(iserv)

        return iserviciofiltrados

    def obtenerRenta(self,plan):

        for pl in self.listaPlan:

            if ((plan.getNombre()==pl.getNombre()) and \
               (plan.getRif_Empresa()== pl.getRif_Empresa())):

                return pl.getRenta() 

    def procesar(self,datos):

        if(datos[0]==1): #agregar cliente

            cliente = CL.Cliente(datos[4], datos[1], datos[3], datos[2]) # 1-esnat 2-nom 3-ide 4-direccion
            if(self.verificarCliente(cliente)):

                self.agregarCliente(cliente)
            
        elif(datos[0]==2): #consultar cliente

            cliente = CL.Cliente('','', datos[1], '')
            cliente.setIde(datos[1])      ##ojo aca
            self.consultarCliente(cliente)

        elif(datos[0]==3): #agregar producto   #1-idcl 2-nompr 3idp 4rif 5nompl
                                   
            producto = P.Producto(datos[1],datos[3],datos[2],datos[5],None,datos[4], 0)  
            
            plan = PL.Plan(None,datos[5],None,None,datos[4])
            producto.setRenta(self.obtenerRenta(plan))
            if (not(self.verificarPlan(plan))):
                print 'No existe plan'
                return 
            
            cliente = CL.Cliente('', '',datos[1],'')  
            if (not(self.verificarCliente(cliente))):
               print 'No existe cliente'
               return
            
            if (self.verificarProducto(producto)):

                self.agregarProducto(producto)
 
        elif(datos[0]==4): #consultar producto  #1-nompr 2-idn

            producto = P.Producto(None,datos[2],datos[1],None,None,None, None)
            self.consultarProducto(producto)  

        elif(datos[0]==5): #eliminar producto #1-nompr 2-idn 

            producto = P.Producto(None,datos[2],datos[1],None,None,None, None)
            if(verificarProducto(producto)):
                
                self.eliminarProducto(producto)

            else:

                print 'No existe el producto'

        elif(datos[0]==6): #afiliar producto/plan    #parece estar con el 3      
 
            pass

        elif(datos[0]==7): #afiliar producto/servicio
        
            producto = P.Producto(None,None,None) ##
            producto.setClaves ##      
            
            if(not(self.verificarProducto(producto))):

                #No existe el producto
                return

            servicio = S.Servicio(None, None)
            servicio.setNombre(datos[3]) #revisar
            
            if(self.verificarServicio(servicio)):

                adiciona = A.Adiciona(datos[2], datos[1], datos[3]) # 1-idp 2-nomp 3-nomserv
                self.agregarAdiciona(adiciona)


        elif(datos[0]==8): #desafiliar producto/servicio
        
            producto = P.Producto(None,None,None) ##
            producto.setClaves ##      
            
            if(not(self.verificarProducto(producto))):

                #No existe el producto
                return

            servicio = S.Servicio(None, None)
            servicio.setNombre(datos[3]) #revisar
            
            if(self.verificarServicio(servicio)):

                adiciona = A.Adiciona(datos[2], datos[1], datos[3]) # 2-idp 1-nomp 3-nomserv
                self.desafiliarServicio(adiciona)

        elif(datos[0]==9): #consultar plan/producto       
            
            producto = P.Producto(None,None,None) ##
            producto.setClaves ##
            if(self.verificarProducto(producto)):

                self.consultarPlanProducto(producto)

        elif(datos[0]==10): #consultar servicios/producto

            producto = P.Producto(None,None,None) ##
            producto.setClaves ##
            if(self.verificarProducto(producto)):

                self.consultarServiciosProducto(producto)

        elif(datos[0]==11): #consultar consumos/producto

            producto = P.Producto(None,None,None) ##
            producto.setClaves ##
            if(self.verificarProducto(producto)):

                self.consultarConsumosProducto(producto)

        elif(datos[0]==12): #agregar consumo

            producto = P.Producto(None,None,None) ##
            producto.setClaves ##
            if(not(self.verificarProducto(producto))):
                                                 #1-fecha 2-costo 3-serv 4-nomp 5-idnp
                #no existe el producto
                return

            consumo = C.Consumo(datos[2],datos[3],datos[1],datos[5], datos[4])
            if(self.verificarConsumo(consumo)):
                
                self.agregarConsumo(consumo) 

        elif(datos[0]==13): #facturar 


            cliente = CL.Cliente(None,None,None,None)
            cliente.setIde(datos[1])
            if(not(self.verificarCliente(cliente))):
                #no existe cliente
                return
            cliente = self.buscarCliente(cliente)
            productosfiltrados= self.filtrarProducto(cliente)
            planesfiltrados = self.filtrarPlan(productosfiltrados)
            consumosfiltrados = self.filtrarConsumo(productosfiltrados, \
                                datos[2], datos[3]) ##mes-anio
            adicionafiltrados = self.filtrarAdiciona(productosfiltrados)
            serviciofiltrados = self.filtrarServicio(adicionafiltrados)
            iplanfiltrados= self.filtrarIncluidoPlan(planesfiltrados)
            iserviciofiltrados = self.filtrarIncluidoServicio(serviciofiltrados)
            factura = F.Factura()
            factura.facturar(cliente,adicionafiltrados,consumosfiltrados,iplanfiltrados,iserviciofiltrados,planesfiltrados, \
                             productosfiltrados,serviciofiltrados ,datos[2],datos[3],datos[4]) #4-pre o pos         

            
#def aplicar(self,cliente,ladiciona,lconsumos,lincluPlan,lincluServ,lplan,lproductos,lservicios,mes,anio,flag):
            

