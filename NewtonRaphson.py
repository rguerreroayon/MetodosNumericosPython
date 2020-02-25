import math

def f(x):
    y = (   (9 * (math.pow(x,4))) + (18 * (math.pow(x,3))) + (38 * (math.pow(x,2))) - (57 * x) + (14) ) #Asignacion
    #y = (   (math.pow(x,3)) + (2 * (math.pow(x,2))) + (7 * x) - (20) ) #pruebas

    return float(y)

def fDerivada(x):

    y = (  (36 * (math.pow(x,3))) + (54 * (math.pow(x,2))) + (76 * x) - (57)   ) #Derivada asignacion
    #y = (   (3 * (math.pow(x,2)))  + (4 * x) + (7) )

    return float(y)



def newtonRaphson(xInicial, error):
    iteracion = 0
    FdX = 0
    FdXDerivada = 0
    continua = True

    while(continua):
        if(iteracion != 0):
            xInicial = xInicial - (FdX/FdXDerivada)


        FdX = f(xInicial)
        FdXDerivada = fDerivada(xInicial)

        print('Iteracion Numero:'+str(iteracion))    
        print('Valor de X'+str(iteracion)+': '+str(xInicial))
        print('Valor de F de X'+str(iteracion)+': '+str(FdX))
        print('Valor de F de X Derivada'+str(iteracion)+': '+str(FdXDerivada))
        print('------------------------------------------------------------------------------')

        if(abs(FdX) < error):
            print('Raiz encontrada en la iteracion '+str(iteracion)+' con el valor de '+str(FdX))
            continua = False    
            


        iteracion = iteracion + 1

def main():
    x = float(input('Ingrese el valor inicial de X: '))
    error = float(input('Ingrese el error: '))

    newtonRaphson(x,error)


main()

