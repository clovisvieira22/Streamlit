import turtle
def desenhar_estrela(tamanho, pontas):
    angulo = float(180 - (180 / pontas))
    for _ in range(pontas):
        turtle.forward(tamanho)
        if(pontas == 8):
            turtle.right(135)
        else:
            turtle.right(angulo)

turtle.reset() 
turtle.pensize(5)
pontas = 7
turtle.color("red")      
desenhar_estrela(100,pontas)
