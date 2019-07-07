class Termometro():
    def __init__(self):
        self.__unidadM = 'C'
        self.__temperatura = 0
        
    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}º C".format((temperatura - 32) * 5/9)
        else:
            return "Unidad incorrecta"
        
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidadM)


    def unidadMedida(self, uniM = None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
                
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM = None):
        if uniM == None or uniM == self.__unidadM :
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__() 
        
#c = Termometro()
#c.conversor(0, 'C')
#c.conversor(32, 'F')
#print(c)
#t = Termometro()
#t.temp(32)
#t.unidadMedida('F')
#t.mide('C')
#t.temp(0)
#t.unidadMedida('C')
#t.mide('F')
#t1 = Termometro()
#t1.mide()
#t1.mide('C')
#t1.mide('F')