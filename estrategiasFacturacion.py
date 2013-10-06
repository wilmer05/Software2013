import facturarPrepago as fpre
import facturarPostpago as fpos

class estrategiasFacturacion:
  
  def __init__:
    
  
  def ObtenerEstrategia(self,flag):
    if (flag == 'pre'):
      return fpre.facturarPrepago()
    elif (flag == 'pos'):
      return fpos.facturarPostpago()
      
    ##Posibilidad de agregar mas estrategias ##