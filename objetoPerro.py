class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
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