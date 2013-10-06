import sys
from Producto import Producto
#Interfaz del decorador
class Decorador(Producto):

  def __init__(self,id_Cliente,idn,nombre,nombre_plan,rif_empresa,saldo):
    super(Decorador,self).__init__(id_Cliente,idn,nombre,nombre_plan,rif_empresa,saldo)
  

  """Un objeto para poder anadir un servicio a un producto'"""

  def getNombre(self):
    """Retorna el nombre del servicio agregado al producto"""
    pass
    
  def getCosto(self):
    """Retorna el nombre del servicio agregado al producto"""
    pass

  def imprimir(self):
    """Imprime una cadena indicando el servicio poseido"""
    pass

  def agregar(self,BD):
    """agregara un asociacion del producto con el decorador a la BD"""
    pass
