import math

def reduzArgumento(n):
    expoente = 0
    if(n >=2):    
        while n >= 2:
            n = n/2
            expoente +=1
        f = n - 1
    elif (n >=1):
        f = n - 1
    else:
        while n <= 1:
            n = n*2
            expoente -= 1
        f = n - 1
    return expoente, f
    
def raizQuadrada(Xn,A):
    return 0.5*(Xn + A/Xn)

def raizInversa(Xn,A):
    return Xn*(0.5*(3 - A*Xn*Xn))

def main():

    n = float(input("insira o numero que deseja calcular a raiz inversa: "))
    
    exp, f = reduzArgumento(n)
    esperado = 1/math.sqrt(n)
    total = (f+1)*2**exp

    print("fração: ", f)
    print("expoente: ", exp)
    print("Chute: ", 1+f/2)
    print("Numero: ", total)
    
    Xn = 1 + f/2
    Kn = 1/(1 + f/2)
    raizQuadrada2 = math.pow(2,0.5)
    

    for i in range(0,6):

        if (exp % 2):
            convencional = 1/(2**(exp/2)*Xn)
            inversa = Kn/(2**(exp/2))
        else:
            convencional = 1/ (2**((exp-1)/2) * raizQuadrada2 * Xn) 
            inversa = Kn/((2**((exp-1)/2)) * raizQuadrada2)

        print("\n==========iteração ", i,"==========")
        print("\nMetodo convecional: ", convencional)
        print("              Erro: ", abs(convencional - esperado))
        print("\n     Metodo Direto: ", inversa)
        print("              Erro: ", abs(inversa - esperado))
        print("\nValor Esperado:", esperado)
        Xn = raizQuadrada(Xn,f+1)
        Kn = raizInversa(Kn,f+1)


main()