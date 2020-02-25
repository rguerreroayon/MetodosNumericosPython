import math

def f(x):
    x = float(x)

    #y = (   (9 * (math.pow(x,4))) + (18 * (math.pow(x,3))) + (38 * (math.pow(x,2))) - (57 * x) + (14) ) #EL BUENO DE LA ASIGNACION
    y =   math.pow(x,3) -  (2*(math.sin(x))) 
    #y = ((math.pow(x,3)) - (2 * math.sin(x)))            
    #y = ( (math.pow(x,3)) - (7.014 * (math.pow(x,2))) - (13.3247 * x) - 3.548 ) #PRUEBAS
    #y = (  (math.pow(x,3)) + (2 * (math.pow(x,2))) + (7 * x) - (20)    )    # x^3 +2x^2 +7x -20

    return float(y)

def secante(x,xmenos1,error,iteracion):

    fx = f(x)
    fxmenos1 = f(xmenos1)
    
    nuevaX = ((x) - ((fx* (xmenos1 - x))/(fxmenos1 - fx)))
    
    errorRelativo =    abs(nuevaX - x)/abs(nuevaX)

    print('----------------------------------------------------------')
    print('Iteración Número: '+str(iteracion))
    print('Valor de X: '+str(x))
    print('Valor de F de X: '+str(fx))
    print('Valor de X-1: '+str(xmenos1))
    print('Valor de F de X-1: '+str(fxmenos1))
    print('Valor de Nueva X: '+str(nuevaX))
    print('Error Relativo: '+str(errorRelativo))


    if(errorRelativo > error):
        iteracion = iteracion + 1
        secante(nuevaX,x,error,iteracion)
    else:
        print('Raiz encontrada en la iteración '+str(iteracion))
        print('Valor: '+str(fx))


def main():
    x0 = float(input('Ingresa la x0: '))
    x1 = float(input('Ingresa el x1: '))
    error = float(input('Ingresa el error: '))
    print('------------------------------------------')
    secante(x1,x0,error,0)

main()