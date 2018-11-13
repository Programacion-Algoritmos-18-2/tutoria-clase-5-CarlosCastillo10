"""
    @CarlosCastillo10
"""

class Ciudad(object):
    
    def __init__(self):
        self.nombre = " "
        self.poblacion = 0

    def agregar_nombre(self, n):
        self.nombre = n

    def agregar_poblacion(self, p):
        self.poblacion = p

    def obtener_nombre(self):
        return self.nombre

    def obtener_poblacion(self):
        return self.poblacion

    def presentar_datos_ciudad(self):
        return ("%s, con una poblacion de %d\n\n"%(self.obtener_nombre(),self.obtener_poblacion()))
    
class Persona(object): #Clase Padre
    
    #Constructor
    def __init__(self):
        self.nombre = " "
        self.apellido = " "
        self.ciudad = " "

    #Metodos de agregar
    def agregar_nombre(self, n):  
        self.nombre = n

    def agregar_apellido(self, a):
        self.apellido = a

    def agregar_ciudad(self, c):  
        self.ciudad = c

     #  Metodos de obtener   
    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_ciudad(self):
        return self.ciudad

"""
    # Metodo de presentar datos
    def presentar_datos(self):
        cadena =  "Informacion de %s %s\n\tCedula: %s" % (self.obtener_nombre(),self.obtener_apellido(),self.obtener_cedula())
        return cadena#Retorna cadena
"""
class Estudiante(Persona):#Clase hija que era de la clase padre ("Empleado")
    
    def __init__(self):
        
        super(Estudiante, self).__init__()       
        self.id_estudiante = 0


    #Metodos de agregar  
    def agregar_id_estudiante(self, id_est):  
        self.id_estudiante = id_est

    def obtener_id_estudiante():
        return self.id_estudiante

"""
    #Metodo de presentar datos(Llama al metodo presentar_datos de la clase padre "Empleado")
    def presentar_datos(self):
        #Llamamos al metodo presentar datos de la clase padre
        cadena = "%s\n\tNumero de horas: %d\n\tValor por Hora: %d\n\tSueldo Final: %.1f\n" % (super(EmpleadoPorHoras, self).presentar_datos(), self.obtener_numero_horas()
            ,self.obtener_valor_hora(),self.calcular_sueldo_final())

        return cadena#Retorna cadena
"""
class EstPresencial(Estudiante):#Clase hija que era de la clase padre ("Empleado")

    def __init__(self):
        
        super(EstPresencial, self).__init__()       
        self.ciclo = 0
        self.num_creditos = 0
    
    def agregar_ciclo(self, c):  
        self.ciclo = c

    def agregar_num_creditos(self, creditos):  
        self.agregar_num_creditos = creditos

        #Metodos de obtener 
    def obtener_sueldo_fijo(self):
        return self.sueldo_fijo

    def obtener_ciclo(self):
        return self.ciclo

    def obtener_num_creditos(self):
        return self.agregar_num_creditos

    
    def presentar_datos(self):
        #Llamamos al metodo presentar datos de la clase padre
        cadena = ("Reporte\n\n%s %s-%d\nCiclo: %d\nCreditos: %d\nPertenece a ciudad %s"%(self.obtener_nombre(),self.obtener_apellido(),
            self.obtener_id_estudiante(),self.obtener_ciclo(),self.obtener_num_creditos(),self.presentar_datos_ciudad()))


        return cadena
"""
class EmpleadoPorSemana(Empleado):#Clase hija que era de la clase padre ("Empleado")

    def __init__(self):
        
        super(EmpleadoPorSemana, self).__init__()       
        self.numero_semanas = 0
        self.valor_semanal = 0

    def agregar_numero_semanas(self, nums):  
        self.numero_semanas = nums

    def agregar_valor_semanal(self, vsemanal):  
        self.valor_semanal = vsemanal

        #Metodos de obtener 
    def obtener_numero_semanas(self):
        return self.numero_semanas

    def obtener_valor_semanal(self):
        return self.valor_semanal

    def calcular_sueldo_final(self):
        sueldo_final = (self.obtener_numero_semanas() * self.obtener_valor_semanal()) + self,obtener_comision_fija()

        return sueldo_final#Retorna el sueldo final


    def presentar_datos(self):
        #Llamamos al metodo presentar datos de la clase padre
        cadena = "%s\n\tNumero de Horas: %.1f\n\tValor Semanal: %d%s\n\tSueldo Final: %.1f\n" % (super(EmpleadoFijo, self).presentar_datos(), self.obtener_numero_semanas()
            ,self.obtener_valor_semanal(),"%",self.calcular_sueldo_final1())

        return cadena

    

