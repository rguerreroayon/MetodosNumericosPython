import math

def f(x):

    y =   math.pow(x,3) -  (2*(math.sin(x))) 

    return float(y)

def reglaFalsa(Xizq,Xder,error,iteracion):
    #Conseguimos el valor de y de x izquierda y derecha
    Yizq = f(Xizq) #Conseguimos F de X de X Izquierda
    Yder = f(Xder) #Conseguimos F de X de X Derecha

    Xm =    ((Xizq * Yder) - (Xder * Yizq)) / (Yder - Yizq)       
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
        if(Yder >= 0):
            reglaFalsa(Xizq,Xm,error,iteracion)
        elif(Yizq >=0):
            reglaFalsa(Xm,Xder,error,iteracion)
            
    elif(YdeXm < 0):
        if(Yder < 0):
            reglaFalsa(Xizq,Xm,error,iteracion)
        elif(Yizq < 0):
            reglaFalsa(Xm,Xder,error,iteracion)



def main():
    izq = float(input('Ingresa la x izquierda: '))
    der = float(input('Ingresa el x derecha: '))
    error = float(input('Ingresa el error: '))
    print('-------------------------------------------------------------------------------------------------------------------------------------')

    reglaFalsa(izq,der,error,0)


main()




