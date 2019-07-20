#las funciones de nivel superior son funciones que toman como parametros otras funciones
def suma(limitTo):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += i
        
    return sumatorio

def sumaCuadrado(limitTO):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += i*i
    return sumatorio

def sumaf(limitTo, f):#funcion de nivel superior
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += f(i)
        
    return sumatorio

def cuadrado(x):
    return x*x

def cuadradoE(x, y):
    retur x*x
    
    

#poner en la consola
#sumaf(4, cuadrado)
#esto va a fallar por que se esperan dos argumentos pero ninguno es una función
#sumaf(4, cuadradoE)       