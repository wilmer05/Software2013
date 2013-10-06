import estrategiasFacturacion as ef

#Clase que implementa una factura en la BD.
#Mediante el patron estrategia, se decide el metodo de facturacion
class Factura:
  
  #Constructor de la clase
  def __init__(self):
  
  #Mediante el patron estrategia, decidimos como facturar
  def ObtenerEstrategia(self,flag):
    self.estrategia=ef.ObtenerEstrategia(flag)
   
  #Funcion a ser llamada por la fachada, con la info que provee se decide (mediante estrategia)
  #el metodo de facturacion y se factura.
  def facturar(self,cliente,ladiciona,lconsumos,lincluPlan,lincluServ,lplan,lproductos,lservicios,mes,anio,flag):
    #Obtenemos la estrategia segun la informacion que nos llegue.
    self.ObtenerEstrategia(flag)
    #Aplicamos la estrategia adecuada (la clase abstracta estrategia decide)
    retorno=self.estrategia.aplicar(cliente,ladiciona,lconsumos,lincluPlan,lincluServ,lplan,lproductos,lservicios,mes,anio)
    self.monto=retorno[0]
    self.descripcionImpr=retorno[1]
    
  def imprimir(self):
    print self.descripcion