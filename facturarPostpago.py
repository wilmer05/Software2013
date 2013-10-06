import Cliente as c
import Producto as p
import Adiciona as a
import Consumo as co
from time import gmtime,strftime
import datetime

#Estrategia de facturacion para productos postpago de un cliente dado.
class facturarPostpago:
  def __init__(self):
    pass
  
  #Devuelve si prod es postpago
  def es_post(self,producto,lplan):
    planprod=producto.getNombre_Plan()
    for a in lplan:
      ilim=str(a.getIlimitado())
      if (((ilim=='0')|(ilim=='1')) & (planprod == a.getNombre())):
	return True
    return False
   
  def conseguir_productosPost(self,cliente,lproductos,lplan):
    #Lista con los productos del cliente
    lp=[]
    #Obtenemos identificador del cliente
    idcliente=cliente.getIde()
    
    for a in lproductos:
      if (self.es_post(a,lplan)):
	lp.append(a)
    return lp

  #Devuelve renta del producto por concepto de plan.
  def obtener_renta(self,producto,lplan):
    planprod=producto.getNombre_Plan()
    for a in lplan:
      if (planprod == a.getNombre()):
	return int(a.getRenta())
	
     
    
  #Metodo que aplica la estrategia correspondiente.(facturar postpago)
  #La funcion retornara el monto total, y un string que sera la impresion de la factura.
  def aplicar(self,cliente,ladiciona,lconsumos,lincluPlan,lincluServ,lplan,lproductos,lservicios,mes,anio):
    
    #String que se devolvera
    strimpr=''
    #Obtenemos los productos del cliente que sean post
    lp=self.conseguir_productosPost(cliente,lproductos,lplan)
    
    #Aca se sumaran el total de cada producto facturado, para asi tener un monto
    #total de la factura
    montoGlobal=0
    
    #Guardamos el string con la info de la factura.
    #Util para su posterior impresion.
    strimpr=strimpr+"-->Factura Fiscal generada:"+"\n"
    strimpr=strimpr+"Nombre:"+cliente.getNombre()+"\n"
    strimpr=strimpr+"\n"
    #strimpr=strimpr+cliente.getId()
    strimpr=strimpr+"Direccion:"+cliente.getDireccion()
    strimpr=strimpr+"\n"
    strimpr=strimpr+"Mes/Anio factura:"+str(mes)+"-"+str(anio)
    strimpr=strimpr+"\n"
    strimpr=strimpr+"Fecha emision:"+str(datetime.datetime.now())
    strimpr=strimpr+"\n"
    
    #Iteraremos sobre los productos
    for a in lp:
      rentaplan=self.obtener_renta(a,lplan)
      
      nombreprod=a.getNombre()
      idprod=str(a.getIdn())
      
      strimpr=strimpr+"-->Producto:"+nombreprod+"-"+idprod
      strimpr=strimpr+"\n"
      montototal=0
      montototal=montototal+rentaplan
      
      #Sumaremos el total de sus consumos
      #Esta lista sera de la forma (descripcion),(total),(descripcion),(total),...
      listasumadaconsumos=[]
      for b in lconsumos:
	#Revisamos que sea un consumo para el producto que analizamos en esta iteracion
	if ((b.getNombre_Producto() == nombreprod) & (str(b.getId_Producto()) == idprod)):
	  #Si es un consumo que no hemos visto, lo ponemos por primera vez en la
	  #lista
	  if (not ((b.getDescripcion()) in listasumadaconsumos)):
	    listasumadaconsumos.append(b.getDescripcion())
	    listasumadaconsumos.append(int(b.getCosto()))
	  #Si ya el consumo de ese tipo ha sido puesto en la lista, se le va sumando
	  #a la posicion aledanha que es lo que se habia consumido mas lo nuevo.
	  else:
	    i=listasumadaconsumos.index(b.getDescripcion())
	    listasumadaconsumos[i+1]=int(listasumadaconsumos[i+1])+int(b.getCosto())
	    
	#Veremos el total de lo incluido en su plan(mismo formato-logica de arrib
	
      linclud=[]
      laux=[]
      #laux es para evitar caso especifico en que varios productos del cliente
      #esten asociados al mismo plan. De esta manera no estaremos sumando
      #incluidos de mas.
      for c in lincluPlan:
	#TOmamos solo los incluidos en el plan en cuestion.
	if ((c.getNombre() == a.getNombre_Plan()) & (c.getTipo() not in laux)):
	  linclud.append(c.getTipo())
	  linclud.append(c.getCantidad())
	  laux.append(c.getTipo())
	  
	#Vemos los servicios que tengo para este prod
      lservs=[]
      for w in ladiciona:
	if ((w.getNombre_Producto() == nombreprod) & (str(w.getId_Producto()) == idprod)):
	  lservs.append(w)
	  
      print "servicios para este prod:",lservs
	   
      #Vemos lo incluido en dichos servicios y metemos todo en una lista
      lincluservs=[]
      laux2=[]
      #laux2 tiene la misma funcion que laux para la inclusion en los planes.
      
      #Itero sobre los servicios del producto en cuestion
      for x in lservs:
	#Recorro a ver que tiene incluido el servicio x
	for y in lincluServ:
	  if (x.getNombre_Servicio() == y.getNombre_Sextr()):
	    if (not((x.getNombre_Servicio in laux2) & (y.getTipo() in laux2))):
	      lincluservs.append(y.getTipo())
	      lincluservs.append(int(y.getCantidad()))
	      laux2.append(x.getNombre_Servicio())
	      laux2.append(y.getTipo())
	      
	#Mezclo las listas de incluidoplan e incluidoservs para tener una total
	
	#Recorro la lista de lo que se incluye en todos sus servs extra:
	#Si algo de ese tipo ya esta incluido en su plan, se le suma.
	#Si no, se "appendea" a la lista para tenerlo todo en una lista que
	#englobe todo.
      for d in lincluservs:
	if (isinstance(d,str)):
	  if ((d in linclud)):
	    i2=linclud.index(d)
	    i3=lincluservs.index(d)
	    linclud[i2+1]=linclud[i2+1]+int(lincluservs[i3+1])
	  else:
	    i4=lincluservs.index(d)
	    linclud.append(d)
	    linclud.append(int(lincluservs[i4+1]))
      
	#Sumaremos las rentas de los servicios que tiene afiliado
	#Veo los servicios que ha adicionado y lo comparo con 
	#los servicios en general, si coinice, agarro su costo.
      sumaservs=0
      for e in lservicios:
	for h in lservs:
	  if (e.getNombre() == h.getNombre_Servicio()):
	    sumaservs=sumaservs+e.getCosto()
	  
	#Falta contrastar lo consumido(en listasumadaconsumos) con lo incluido
	#(en lincud)
	
	#Iteramos sobre lo que consumio y sobre lo que tiene incluido:
	#Vamos restando a lo que consumio segun lo que tiene incluido, a ver si
	#sobran consumos, que significaria haber consumido de mas.
      for t in listasumadaconsumos:
	for k in linclud:
	  if ((isinstance(k,str)) & (isinstance(t,str))):
	    if (k == t):
	      index1=listasumadaconsumos.index(t)
	      index2=linclud.index(k)
	      listasumadaconsumos[index1+1]=listasumadaconsumos[index1+1]-linclud[index2+1]
	      
	#Recorremos a ver si se sobrepaso con algun consumo
	#Vamos por la lista, si consigo un string: no hago nada, pues
	#el string es el tipo de consumo que esta en la casilla siguiente
	#de la lista.
      sobrepaso=0
      for v in listasumadaconsumos:
	if (isinstance(v, str)):
	  pass
	else:
	  if (v > 0):
	    sobrepaso=sobrepaso+v
	
	#Luego el monto total de la factua es:
	#La renta de su plan, mas la renta de los servicios que ha agregado,
	#mas algun consumo que haya hecho en exceso.
      montototal=sumaservs+rentaplan+sobrepaso
      strimpr=strimpr+"  Plan contratado:"+a.getNombre_Plan()+"\n"
      strimpr=strimpr+"  Renta del plan:"+str(rentaplan)+"\n"
      strimpr=strimpr+"  Servicios Contratados para este producto:"+"\n"
      for z in lservs:
	strimpr=strimpr+"  "+z.getNombre_Servicio()+"\n"
      strimpr=strimpr+"  Total por sobrepaso de consumos:"+str(sobrepaso)+"\n"
      strimpr=strimpr+"  Total por este producto:"+str(montototal)+"\n"
	  
      #Agregamos el costo de facturar este producto al total.
      montoGlobal=montoGlobal+montototal
	    
    strimpr=strimpr+"-->Monto total de la factura:"+str(montoGlobal)+"\n"
    return (montoGlobal,strimpr)
	      

    
	      
  
