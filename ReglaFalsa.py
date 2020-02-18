import math

def f(x):
    x = float(x)

    y = (   (9 * (math.pow(x,4))) + (18 * (math.pow(x,3))) + (38 * (math.pow(x,2))) - (57 * x) + (14) ) #EL BUENO DE LA ASIGNACION

    #y = ( (math.pow(x,3)) - (7.014 * (math.pow(x,2))) - (13.3247 * x) - 3.548 ) #PRUEBAS
    
    #y = (  (math.pow(x,3)) + (2 * (math.pow(x,2))) + (7 * x) - (20)    )    # x^3 +2x^2 +7x -20


    return float(y)

def reglafalsa(Xizq,Xder,error,iteracion):
    


    while(True):

        #Conseguimos el valor de y de x izquierda y derecha
        Yizq = f(Xizq) #Conseguimos F de X de X Izquierda
        Yder = f(Xder) #Conseguimos F de X de X Derecha




        Xm =    ((Xizq * Yder) - (Xder * Yizq)) / (Yder - Yizq)          #Conseguimos XM
        YdeXm = f(Xm)          #Conseguimos F de X de XM


        print('Iteración Numero: '+str(iteracion))
        print('X Izq : '+str(Xizq)+' , F de X Izq:    '+str(Yizq))
        print('X Der : '+str(Xder)  +' , Fde X Derecha: '+str(Yder))
        print('XM : '   +str(Xm)+        ' , F de XM: '+str(YdeXm))

        absYdeXm = abs(YdeXm)
        print('Valor absoluto de F de XM: '+str(absYdeXm))

        print('-------------------------------------------------------------------------------------------------------------------------------------')


        if(abs(YdeXm) < error):
            print('Se encontro la raiz en la iteracion '+str(iteracion))
            print('Valor de F de XM: '+str(YdeXm))
            exit()

        iteracion = iteracion + 1


        if(YdeXm >= 0 ):
            print('XM ES POSITIVO')
            nuevaDerecha = Xm
            reglafalsa(Xizq,nuevaDerecha,error,iteracion)
        elif(YdeXm < 0):
            print('XM ES NEGATIVO')

            nuevaIzquierda = Xm

            reglafalsa(nuevaIzquierda,Xder,error,iteracion)





def main():
    izq = float(input('Ingresa la x izquierda: '))
    der = float(input('Ingresa el x derecha: '))
    error = float(input('Ingresa el error: '))
    print('------------------------------------------')
    reglafalsa(izq,der,error,0)


main()