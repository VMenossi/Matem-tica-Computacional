import math

#### valores para o seno ####
a1 = -1.666666666666667e-1      #-1/3!
a2 = 8.33333333333333e-3        #+1/5!   
a3 = -1.98412698412698e-4       #-1/7!
a4 = 2.75573192239859e-6        #+1/9!
a5 = -2.505210838544172e-08     #-1/11!
#a6 = 1.6059043836821613e-10     #1/13!
#a7 = - 7.647163731819816e-13    #-1/15!

#### valores para o coseno ####
b1 = -0.5                        #-1/2!
b2 =  0.041666666666666664       #+1/4!
b3 = -0.001388888888888889       #-1/6!
b4 =  2.48015873015873e-05       #+1/8!
b5 = -2.755731922398589e-07      #-1/10!
b6 =  2.08767569878681e-09       #+1/12!
#b7 = -1.1470745597729725e-11    #-1/14!


def seno(x):

    w = x*x

    return x *(1 + w *( a1 + w *(a2 + w *(a3 + w *(a4 + w*a5)))))

def coseno(x):

    w = x*x

    return 1 + w *( b1 + w *( b2 + w *( b3 + w *(b4 + w *(b5 + w *b6)))))
    
def main():    
    erroMax= 0
    angulo = -1
    for x in range(0,361,10):

        if(x <= 45):
            res = seno(math.radians(x))

        elif(x <= 135):
            res = coseno(math.radians(x-90))

        elif(x <= 225):
            res = -1*seno(math.radians(x-180))

        elif(x <= 315):
            res = -1*coseno(math.radians(x-270))

        elif(x <=360):
            res = seno(math.radians(x-360))

        senpy = math.sin(math.radians(x))
        erro = abs(res - senpy)
        if(erro > erroMax):
            erroMax = erro
            angulo = x
        print("nosso seno: ",res)
        print("math.sin(x):",senpy)
        print("erro:",erro)
        print("\n")

    print("Maior erro")
    print("\t Angulo:",angulo)
    print("\t ErroMax",erroMax)

main()

