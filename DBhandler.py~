import sys
import pg
import random as rdm

#Esta clase sirve para manejar una base de datos generica, ofrece
#los metodos basicos para dicho manejo: conectarse a ella, listar
#las tablas de ella, realizar una consulta y cerrar la coenxion
#Realizada por: Carlos Da Silva y Juan Carpio

class DB_Handler:
    #PGobect: conexion con la base de datos. A traves de ella sse realiza todo
    #lo referente a la base de datos.
    BD_Abierta = None

    #Abre una conexion con la base de datos especificada.
    def Establecer_Conexion(self):
        #dbname=raw_input("Introduzca nombre de base de datos:")
        #username=raw_input("Introduzca username:")
        #password=raw_input("Introduzca password:")
        self.BD_Abierta=pg.connect(dbname="mc2", user="postgres", passwd="postgres")

    #Lista las tablas de la base de datos a la que se haya conectado
    def Listar_Tablas(self):
        result=self.BD_Abierta.query("SELECT * FROM pg_tables WHERE schemaname = 'public'")
        #Dictresult devuelve los resultados como diccionario, la clave sera el nobmre de la columna
        result=result.dictresult()
        for a in result:
            print a[1]

    #Hace la consulta especificada, devuelve como resultado una lista, cada elem
    #es una fila obtenida. Se devuelve a manera de diccionario, donde la clave es
    #el nombre de la columna
    def Hacer_Consulta(self,str_consulta):
        resultado=self.BD_Abierta.query(str_consulta)
        if(type(resultado)!=str):
            return resultado.dictresult()
        return resultado

    #Cierra la conexion a la base de datos.
    def Cerrar_Conexion(self):
        self.BD_Abierta.close()
    
    #Cargado de datos
    def cargarProducto(self):
      
      #Para prepagos-naturales
      consulta="SELECT p.nombre,p.idn,p.rif_em,p.nombre_plan,p.saldo,pre.renta"
      consulta2=" FROM producto as p,prepago as pre,cl_natural as cl WHERE ((p.nombre_plan=pre.nombre) AND (p.postiza_c=cl.postiza_n))"
      consulta=consulta+consulta2
      res=self.Hacer_Consulta(consulta)
      
      #Para prepagos-juridicos
      consulta="SELECT p.nombre,p.idn,p.rif_em,p.nombre_plan,p.saldo,pre.renta"
      consulta2=" FROM producto as p,prepago as pre,cl_juridico as cl WHERE ((p.nombre_plan=pre.nombre) AND (p.postiza_c=cl.postiza_j))"
      consulta=consulta+consulta2
      res2=self.Hacer_Consulta(consulta)
      
      for a in res2:
	res.append(a)
      
      #Postpagos-naturales
      consulta="SELECT p.nombre,p.idn,p.rif_em,p.nombre_plan,p.saldo,pre.renta"
      consulta2=" FROM producto as p,postpago as pre,cl_natural as cl WHERE ((p.nombre_plan=pre.nombre) AND (p.postiza_c=cl.postiza_n))"
      consulta=consulta+consulta2
      res3=self.Hacer_Consulta(consulta)
      
      for a in res3:
	res.append(a)
      
      #Postpagos-juridicos
      consulta="SELECT p.nombre,p.idn,p.rif_em,p.nombre_plan,p.saldo,pre.renta"
      consulta2=" FROM producto as p,postpago as pre,cl_juridico as cl WHERE ((p.nombre_plan=pre.nombre) AND (p.postiza_c=cl.postiza_j))"
      consulta=consulta+consulta2
      res4=self.Hacer_Consulta(consulta)
      
      for a in res4:
	res.append(a)
	
      return res
      
    def cargarCliente(self):
      #Clientes naturales
      consulta="SELECT * from cliente as c,cl_natural as cl WHERE c.postiza=cl.postiza_n"
      res=self.Hacer_Consulta(consulta)
      
      #CLientes juridicos
      consulta="SELECT * from cliente as c,cl_juridico as cl WHERE c.postiza=cl.postiza_j"
      res2=self.Hacer_Consulta(consulta)
      
      for a in res2:
	res.append(a)
	
      return res
      
    def cargarPlan(self):
      #Planes prepago
      consulta="SELECT p.nombre,p.descripcion,p.rif_empresa,pr.renta FROM plan1 as p,prepago as pr WHERE p.nombre=pr.nombre"
      res=self.Hacer_Consulta(consulta)
      
      #Planes postpago
      consulta="SELECT p.nombre,p.descripcion,p.rif_empresa,pr.renta,pr.ilimitado FROM plan1 as p,postpago as pr WHERE p.nombre=pr.nombre"
      res2=self.Hacer_Consulta(consulta)
      
      for a in res2:
	res.append(a)
	
      return res
      
    def cargarConsumo(self):
      consulta="SELECT * FROM consumo"
      res=self.Hacer_Consulta(consulta)
      return res
      
    def cargarAdiciona(self):
      consulta="SELECT * FROM adiciona"
      res=self.Hacer_Consulta(consulta)
      return res
      
    def cargarServicio(self):
      consulta="SELECT * FROM servicios_extra"
      res=self.Hacer_Consulta(consulta)
      return res
      
    def cargarIncluidoPlan(self):
      consulta="SELECT * FROM incluidos"
      res=self.Hacer_Consulta(consulta)
      return res
      
    def cargarIncluidoServicio(self):
      consulta="SELECT * FROM incluido_servex"
      res=self.Hacer_Consulta(consulta)
      return res
      
    #Agregaciones a la base de datos
    
    def agregarCliente(self,direccion,ide,nombre,flag):
      
      #Genero postiza aleatoria.
      aceptada = False
      while (aceptada == False):
	postiza = rdm.randint(1,1000000)
	existe  = self.Hacer_Consulta("SELECT postiza FROM cliente where postiza = "+str(postiza))
	if len(existe) == 0:
	  aceptada = True
	else:
	  pass
	
      self.Hacer_Consulta("INSERT INTO cliente VALUES ('"+nombre+"',"+str(postiza)+",'"+direccion+"')")
      #True si es natural
      if (flag):
	 self.Hacer_Consulta("INSERT INTO cl_natural VALUES ("+str(postiza)+","+str(ide)+")")
      else:
	 self.Hacer_Consulta("INSERT INTO cl_juridico VALUES ("+str(postiza)+","+str(ide)+")")
	 
	 
    def agregarConsumo(self,costo,descripcion,fecha,id_producto,nombre_producto):
      
      self.Hacer_Consulta("INSERT INTO consumo VALUES ('"+str(fecha)+"','"+str(costo)+"','"+str(descripcion)+"','"+str(nombre_producto)+"',"+str(id_producto)+")")
	
	
    def agregarAdiciona(self,idn,nombre,nombre_servicio):
      
      self.Hacer_Consulta("insert into adiciona values ('"+nombre+"','"+str(idn)+"','"+nombre_servicio+"')")
      
    def agregarProducto(self,idn,idcliente,nombre,nombre_plan,rif_em,saldo):
      #Consigo la postiza del cliente
      pnum=-1
      postiza= self.Hacer_Consulta( "select postiza_n from cl_natural where cedula='"+str(idcliente)+"'")
      if (len(postiza) == 0):
	postiza=self.Hacer_Consulta( "select postiza_j from cl_juridico where rif='"+str(idcliente)+"'")
	if (len(postiza) != 0):
	  pnum=postiza[0]['postiza_j']
      else:
	pnum = 0
	pnum=postiza[0]['postiza_n']
	
      self.Hacer_Consulta("INSERT INTO producto VALUES ('"+nombre+"','"+str(idn)+"','"+str(pnum)+"','"+str(rif_em)+"','"+nombre_plan+"','"+str(saldo)+"')")
    
    #Eliminaciones de la BD
    
    def eliminarConsumo(self,fecha,idproducto,nombreproducto):
      self.Hacer_Consulta("DELETE FROM consumo WHERE nombre_producto = '"+nombreproducto+"' AND id_producto = '"+str(idproducto)+"'")
      
    def eliminarAdiciona(self,idproducto,nombreproducto):
      self.Hacer_Consulta("DELETE FROM adiciona WHERE nombre_producto='"+nombreproducto+"' and id_producto='"+str(idproducto)+"'")
      
    def eliminarProducto(self,idproducto,nombreproducto):
      self.Hacer_Consulta("DELETE FROM producto WHERE nombre ='"+nombreproducto+"' and idn='"+str(idproducto)+"'")
