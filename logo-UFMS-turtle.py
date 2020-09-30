import turtle
tela = turtle.getscreen()
caneta = turtle.Turtle()

#fundo da tela branco
#https://medium.com/reflex%C3%A3o-computacional/m%C3%B3dulo-turtle-d8949db55008
tela = turtle.Screen()
tela.bgcolor("white")

#quadrado fundo UFMS
caneta1 = turtle.Turtle()
caneta1.pen(pencolor="blue",fillcolor="blue",pensize="4",speed=50)
caneta1.penup()
caneta1.goto(110,-110)
caneta1.pendown()
i=1
ifd=[350,220,350,220]
for i in range(4):
    caneta1.left(90)
    caneta1.forward(ifd[i])

#eclipse - circulo deitado UFMS
#codigo retirado do site abaixo - dia 09/09/20 as 20:30
#https://stackoverflow.com/questions/29465666/how-do-you-draw-an-ellipse-oval-in-turtle-graphics-python
caneta.shape("circle")
caneta.shapesize(3,10,7)
caneta.fillcolor("white")
caneta.pencolor("blue")

#criando uma nova caneta para desenhar linhas e nome UFMS
caneta2 = turtle.Turtle()

#linhas
def linhasempe(x, y, e):
    #primeira linha central - azul
    caneta2.penup()
    caneta2.pen(pencolor="blue",fillcolor="blue",pensize="4",speed=50)
    caneta2.pendown()
    caneta2.left(90)
    caneta2.forward(196)
    
    for j in range(x):#3
        #linhas azuis fina
        xazulfina = [-8,8,16]
        fdazulfinas = [193,199,202]
        caneta2.pen(pencolor="blue",fillcolor="blue",pensize="4",speed=50)
        caneta2.penup()
        caneta2.goto(xazulfina[j],0)
        caneta2.pendown()
        caneta2.forward(fdazulfinas[j])

    for k in range(y):#5
        #linhas - azuis larga
        xazullarga = [25,35,-17,-27,-37]
        caneta2.pen(pencolor="blue",fillcolor="blue",pensize="6",speed=50)
        caneta2.penup()
        caneta2.goto(xazullarga[k],0)
        caneta2.pendown()
        caneta2.forward(190)

    for i in range(e):#8
        #linhas brancas pequenas entre as azuis
        xbranca = [4,12,20,30,-4,-12,-22,-32]
        caneta2.pen(pencolor="white",fillcolor="white",pensize="4",speed=1000)
        caneta2.penup()   
        caneta2.goto(xbranca[i],0)
        caneta2.pendown()
        caneta2.forward(35)

linhasempe(3,5,8)#chama a funcao que define a quantidade de linhas para cada for, a linha do meio nao faz parte

#linhas dentro do circulo do lado left
caneta2.pen(pencolor="blue",fillcolor="blue",pensize="2",speed=500)
#bugzinho :)
caneta2.penup()
caneta2.goto(-8,0)
caneta2.right(245)
caneta2.pendown()
caneta2.forward(52)

x=1
xgoto=[-17,-27,-37]
for x in range(3):
    caneta2.penup()
    caneta2.goto(xgoto[x],0)
    caneta2.left(355)
    caneta2.pendown()
    caneta2.forward(55)   

#linhas dentro circulo atrás left
i=1
ii=[60,53,50,45]
ileft=[345,355,355,355]
for i in range(4):
    caneta2.penup()
    caneta2.goto(-37,i)
    caneta2.left(ileft[i])
    caneta2.pendown()
    caneta2.forward(ii[i])


#linhas dentro do circulo frente rigth
k=1
kgoto=[16,25,25,35]
kright=[190,355,350,355]
kfd=[45,45,60,55]

for k in range (4):
    caneta2.penup()
    caneta2.goto(kgoto[k],0)
    caneta2.right(kright[k])
    caneta2.pendown()
    caneta2.forward(kfd[k])

#linhas dentro circulo atrás right
j=1
jright=[350,355,355,355]
jfd=[60,60,53,45]
for j in range(4):
    caneta2.penup()
    caneta2.goto(35,j)
    caneta2.right(jright[j])
    caneta2.pendown()
    caneta2.forward(jfd[j])
    
 
#nome UFMS
#https://medium.com/reflex%C3%A3o-computacional/m%C3%B3dulo-turtle-d8949db55008
caneta2.penup()
caneta2.goto(0,-100)
caneta2.pendown()

fonte1 = ("arial", 45, "bold")
caneta2.write("UFMS", False, "center", fonte1)
caneta2.penup()
caneta2.pen(pencolor="white",fillcolor="white",pensize="4",speed=1000)


