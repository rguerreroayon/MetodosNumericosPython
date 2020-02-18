import math

def f(x):
    x = float(x)

    ordenada = float(9 * (math.pow(x,4)) + 18 * (math.pow(x,3)) + 38 * (math.pow(x,2)) + 14)
    
    return ordenada

def tabula(inferior,superior,incremento):

    while(inferior<=superior):
        ordenada = f(inferior)

        print(str('x: '+str(inferior)+', ordenada: '+str(ordenada)))
        inferior = inferior + incremento






def main():
    inferior = input('Ingresa el limite inferior: ')
    superior = input('Ingresa el limite superior: ')
    incremento = input('Ingresa el incremento ')
    print('------------------------------------------')
    tabula(int(inferior),
        int(superior),
        float(incremento))


main()