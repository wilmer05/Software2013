import Cliente as c
import Producto as p
import Prepago as pr
import Adiciona as a
import Consumo as co
from time import gmtime,strftime
import datetime


class facturarPrepago:
  
  #Creamos un constructor standard de la clase facturarPrepago
  def __init__(self):
    
    self.control = None
    

  #Funcion encargada de determinar si un producto esta afiliado a un plan prepago    
  def Es_Prepago(self,producto,lplan):
    
    NombrePlan = producto.getNombre_Plan()
    
    for plan in lplan:
      
      if ((NombrePlan == plan.getNombre()) & not (plan.getIlimitado() in {0,1})):
	return True
	
    return False
    

  #Funcion encargada de devolver todos los productos prepago asoiados a un cliente
  def Conseguir_Productos_Prepago(self,cliente,lproducto,lplan):
    
    #Lista de productos a devolver
    Productos = []
    #Identificador del cliente
    Identificador = cliente.getId()
    
    for producto in lproducto:
      
      if (Identificador == producto.getid_Cliente()):
	
	if (self.Es_Prepago(producto,lplan)):
	  
	  Productos.append(producto)
	  
    return Productos
	  

  #Funcion que determina la renta del plan prepago asociado a un producto
  def Renta_Prepago(self,producto,lplan):
    
    renta = 0
    
    for plan in lplan:
      
      if (producto.getNombre_Plan() == plan.getNombre()):
	
	renta = plan.getRenta()
	break

    return renta
    

  #Metodo que aplica la estrategia correspondiente.(facturar prepago)
  #La funcion retornara el monto total, y un string que sera la impresion de la factura.
  def aplicar(self,cliente,ladiciona,lplan,lproductos,lservicios,mes,anio):
    
    #Identificador del cliente que se desea facturar
    Identificador = cliente.getId()
    #Productos prepago asociados al cliente
    productos = self.Conseguir_Productos_Prepago(cliente,lproductos,lplans)
    #variable que aloja temporalmente el plan asociado a cada producto
    plan_producto = None
    #Monto total de la factura en cuestion
    costo_total = 0
    #Informacion que se desea imprimir de la factura
    Datos_Impresos = ""
    Datos_Impresos += "Nombre: "+str(cliente.getNombre())+"\n"
    Datos_Impresos += "Direccion: "+str(cliente.getDireccion())+"\n"
    Datos_Impresos += "Periodo de facturacion (mes/anio): "+str(mes)+"/"+str(anio)+"\n"
    Datos_Impresos += "Fecha de Emision: "+str(datetime.datetime.now())+"\n"
    
    #COntador que se encarga de llevar un control de la cantidad de productos asociados a un cliente
    contador = 1
    #COntador que se encarga de llevar un control de los servicios adicionales (si es que estan) asociados a un producto
    contador2 = 1
    Datos_Impresos += "Productos Asociados: \n\n"
    
    #Para cada uno de los productos asociados al cliente se consigue su informacion de facturacion
    for producto in productos:
      
      Datos_Impresos += ("%d. %s\n" % (contador,producto.getNombre()))
      costo_producto = 0
      adicionales_producto = []
      
      #Conseguimos el plan asociado al producto
      for plan in lplan:
	
	if (producto.getNombre_Plan() == plan.getNombre()):
	  
	  plan_producto = plan
	  Datos_Impresos += ("Plan contratado: %s\n" % (plan.getNombre())) 
	  break
	  
      #Conseguimos el valor de la renta del plan asociado al prducto
      renta = self.Renta_Prepago(producto,plan_producto)
      Datos_Impresos += ("Costo: %d\n\n" % (renta))
      costo_producto = += renta
      
      #Sacamos el nombre de todos los servicios adicionales asociados a cada producto
      for adicionales in ladiciona:
	
	if ((producto.getIdn() == adicionales.getId_Producto()) & (producto.getNombre() == adicionales.getNombre_Producto())):
	  
	  adicionales_producto.append(adicionales)
	  
      if len(adicionales_producto)>0:
	
	Datos_Impresos += "Servicios adicionales contratados: \n"
	contador2 = 1
	  
      #Una vez encontrado el nombre de los servicios adicionales incluidos al producto, buscamos el costo de dichos servicios
      for servi_adic in adicionales_producto:
	
	#se debe buscar el costo del servicio adicional en la lista de servicios extras
	for servicios in lservicios:
	  
	  if (servi_adic.getNombre() == servicios.getNombre()):
	    
	    Datos_Impresos += "%d. %s\n" % (contador2,servi_adic.getNombre())
	    Datos_Impresos += "Costo: %d\n" % (servicios.getCosto())
	    costo_producto += servicios.getCosto()
	    contador2 += 1
	    break
	      
      #Aumentamos en control de productos que se esta facturando
      contador += 1
	  
      Datos_Impresos += "\nMonto total asociado al producto: %d\n\n" % (costo_producto)
      costo_total += costo_producto
      
    Datos_Impresos += "Monto total de la factura: %d\n\n" % (costo_total)
    
    return(costo_total,Datos_Impresos)
    
    
      
	  
	  
    
    






      