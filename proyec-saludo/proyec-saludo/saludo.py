#  Se crea  la clase saludo:
from cliente import cliente

class Saludo:
    def __init__(self):
        pass
        self.obj_cliente=cliente()
        
    def hacer_saludo_formal(self):    
        mensaje= "Buenos  saludos formales: "
        return mensaje
     
     
    def hacer_despedida_formal(self):
        mensaje= " Hasta luego formales "
        return mensaje
    
    