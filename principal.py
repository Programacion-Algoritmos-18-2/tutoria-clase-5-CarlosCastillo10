
from paquete_academico.modelo import *

est1 = EstPresencial()
est1.agregar_nombre("Luis")
est1.agregar_apellido("Diaz")
est1.agregar_id_estudiante(123456)
est1.agregar_ciclo(10)
est1.agregar_num_creditos(200)

c = Ciudad()
c.agregar_nombre("Loja")
c.agregar_poblacion(200564)

est1.agregar_ciudad(c)

print(est1.presentar_datos())