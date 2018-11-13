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


class Estudiante(Persona):#Clase hija que era de la clase padre ("Persona")
    
    def __init__(self):
        
        super(Estudiante, self).__init__()       
        self.id_estudiante = 0


    #Metodos de agregar  
    def agregar_id_estudiante(self, id_est):  
        self.id_estudiante = id_est

    def obtener_id_estudiante(self):
        return self.id_estudiante


class EstPresencial(Estudiante):#Clase hija que era de la clase padre ("Estudiante")

    def __init__(self):
        
        super(EstPresencial, self).__init__()       
        self.ciclo = 0
        self.num_creditos = 0
    
    def agregar_ciclo(self, c):  
        self.ciclo = c

    def agregar_num_creditos(self, creditos):  
        self.num_creditos = creditos

        #Metodos de obtener 

    def obtener_ciclo(self):
        return self.ciclo

    def obtener_num_creditos(self):
        return self.num_creditos

    
    def presentar_datos(self):
        #Llamamos al metodo presentar datos de la clase padre
        cadena = "\nReporte\n\n%s %s-%d\nCiclo: %s\nCreditos: %d\nPertenece a la ciudad de %s, con una poblacion de %d\n" %(self.obtener_nombre()
            ,self.obtener_apellido(),self.obtener_id_estudiante(),self.obtener_ciclo(),self.obtener_num_creditos()
            ,self.obtener_ciudad().obtener_nombre(),self.obtener_ciudad().obtener_poblacion())

        return cadena

class EstDistancia(Estudiante):

    def __init__(self):
        
        super(EstDistancia, self).__init__()       
        self.modulo = 0
        self.num_materias = 0
    
    def agregar_modulo(self, m):  
        self.modulo = m

    def agregar_num_materis(self, materias):  
        self.num_materias = materias

        #Metodos de obtener 
    def obtener_modulo(self):
        return self.modulo

    def obtener_num_materias(self):
        return self.num_materias

    

