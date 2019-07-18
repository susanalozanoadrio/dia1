class Objeto():
    __atributoPrivado = None
    atributoPrivado = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPrivado = "Me lo ha pedido Jorge"
        
    def atributoPrivado(self, valor = None):
        if valor == None:
            return self.__atributoPrivado
            print("No has metido nada")
        else:
            self.__atributoPrivado = valor
            print("Has escrito " + valor)
            