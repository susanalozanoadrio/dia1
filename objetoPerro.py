class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print('guau, guau')
            
    def __str__(self):
        #este return es para practicar con lo de abajo en consola 
        #return "Soy el perro {}".format(self.nombre)
        #el que se hace de verdad es este para descubrir si hay algún fallo
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    


class Timido():
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def preguntarNombreConCuidado(self):
        return self.__nombre
        
#salchicho = Perro('Salchicho', 3, 12)
#lola = Perro('Lola', 8, 1.5)
#miko = Perro('Miko', 8, 3)
#salchicho.ladrar()
#lola.ladrar()
#miko.ladrar()
        
#salchicho = Perro('Salchicho', 3, 12)
#print(salchicho)
#salchicho.nombre = 'Chicho'
#print(salchicho)
    
#salchicho = Perro('Salchicho', 3, 12)
#print(salchicho)
        
#chico = Timido('Raul')
#self.__nombre = nombre
#asi no nos devuelve el nombre por que el método es privado
#chico.preguntarNombreConCuidado()
#asi si nos lo devuelve por que le hemos dado permiso a acceder al atributo mediante una función
    