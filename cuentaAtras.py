def retroContador(e):
    print(" {},".format(e),end="")
    if e != 0:
        retroContador(e-1)
    
retroContador(10)
#recursividad