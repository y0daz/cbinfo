import turtle
'''
turtle.color("red")
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.color("blue")
turtle.penup()
turtle.forward(200)
turtle.pendown()

for i in range(2):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.speed(0)
turtle.color("green")
turtle.penup()
turtle.forward(200)
turtle.pendown()


for i in range(360):
    turtle.right(1)
    turtle.forward(1)

'''
'''turtle.speed(0)
turtle.pensize(10)
for i in range(4):
    for i in range(360):
        turtle.right(1)
        turtle.forward(1)
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
   '''

def szachy(x,y):
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(y):
        for i in range(2):
            for i in range(x):
                for i in range(4):
                    turtle.forward(50)
                    turtle.left(90)
                turtle.penup()
                turtle.forward(100)
                turtle.pendown()
            turtle.left(180)
            turtle.penup()
            turtle.pendown()
        turtle.right(90)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.left(90)
    turtle.end_fill()
    turtle.exitonclick()


x = input("Podaj os x:")
y = input("Podaj os y:")
x = int(x)
y = int(y)
szachy(x,y)

print("Poggers!")



# 2020.02.23 B.Kuka:
# 1. nie działa podawanie x i y (można podać literę i program wysypuje się)
# 2. po podanie np. 3 i 3, szachownica rysuje sie w większym rozmiarze
# 3. prosze usunąć komentarze (GIT będize to załatwiać za nas)
# 4. częśc komend w pętlach mozna przekształcić w funkcje i sparametryzować