class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
    

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
               return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
            
class PerroAsistencia(Perro):
    def __init__(self, nonbre, edad, peso, amo):
        Perro.__init__(self, nonbre, edad, peso)
        self.amo = amo
        self.__trabajando = False
        
    def __str__(self):
               return "Perro de asistencia de {}".format(self.amo)

    
    def pasear(self):
        print("{} ayuda a su dueño, {} a pesear".format(self.nombre, self.amo))


    def ladrar(self):
        if self.trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor = None): #función getter setter
        if valor == None:
            return self.__trabajando
        else:
            self.trabajando = valor
        

#rantamplan = PerroAsistencia('Ran Tan Plan', 4, 8, 'Lucky Luke')  
#rantamplan.ladrar()
#print(rantamplan)
#rantamplan.pasear()
#rantamplan.ladrar() prueba cambiando de False a True en trabajando
#rantamplan.trabajando = True
#rantamplan.ladrar()
#rantamplan.__trabajando   no se puede acceder por que asi se simula un método privado en python
#rantamplan._PerroAsistencia__trabajando
#rantamplan.trabajando  metodo getter
#rantamplan.trabajando = True  metodo setter
#rantamplan.trabajando
            
#miko = Dog()
#miko.nombre
#miko.peso
#miko.ladrar()