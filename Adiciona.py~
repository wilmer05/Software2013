import DBhandler as db

#Clase encargada de establecer las relaciones entre los productos y sus servicios adicionales
class Adiciona:
  
  def __init__(self,id_producto,nombre_producto,nombre_servicio):
    
    self.id_producto = id_producto
    self.nombre_producto = nombre_producto
    self.nombre_servicio = nombre_servicio
  
  #Funcion para obtener el Id del producto en una instancia de Adiciona
  def getId_Producto(self):
    return self.id_producto
    
  #Funcion para obtener el nombre del producto en una instancia de Adiciona  
  def getNombre_Producto(self):
    return self.nombre_producto
  
  #Funcion para obtener el nombre del servicio en una instancia de Adiciona
  def getNombre_Servicio(self):
    return self.nombre_servicio
  
  #Funcion para modificar el Id del producto en una instancia de Adiciona
  def setId_Producto(self,id_p):
    self.id_producto = id_p
  
  #Funcion para modificar el nombre del producto en una instancia de Adiciona
  def setNombre_Producto(self,nomb_p):
    self.nombre_producto = nomb_p
  
  #Funcion para modificar el nombre del servicio en una instancia de Adiciona
  def setNombre_Servicio(self,nomb_s):
    self.nombre_servicio = nomb_s
  
  #Funcion que se encarga de agregar una de las instancias de adiciona a la base de datos
  def Agregar(self,manejador):
    
    manejador.agregarAdiciona(self.id_producto,self.nombre_producto,self.nombre_servicio)
    return True
  
  #Funcion que se encarga de eliminar una de las instancias de adiciona a la base de datos
  def Eliminar(self,manejador):
    
    manejador.eliminarAdiciona(self.id_producto,self.nombre_producto,self.nombre_servicio)
    return True