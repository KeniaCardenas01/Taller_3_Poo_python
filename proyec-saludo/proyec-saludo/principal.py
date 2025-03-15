#++++++++ CODIGO PRINCIPAL++++++
from cliente import cliente 
from saludo import Saludo


# creo objetos
objcliente= cliente()
objsaludo=Saludo()

#uso los  metodos de los objetos

objcliente.tomar_datos()
aux_mensaje = objsaludo.hacer_saludo_formal()
objcliente.hacer_saludo(aux_mensaje)

#llamo  alos metodos del objeto