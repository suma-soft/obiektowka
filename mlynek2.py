import turtle
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=600)
    canvas.pack(side=tk.RIGHT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("beige")
    button = tk.Button(root, text="Press me")
    button.pack()
    
plansza = turtle.RawTurtle(screen, visible=False)
plansza.speed(0)

plansza.fd(150)
plansza.bk(300)
plansza.fd(150)
plansza.right(90)
plansza.fd(150)
plansza.bk(300)
plansza.right(90)
plansza.fd(150)
plansza.left(90)
plansza.fd(300)
plansza.left(90)
plansza.fd(300)
plansza.left(90)
plansza.fd(300)
plansza.left(90)
plansza.fd(150)

def pole():
    plansza.color('white')
    plansza.begin_fill()
    plansza.circle(25)
    plansza.end_fill()
    plansza.color('black')
    plansza.circle(25)

def rysujPole(X,Y):
    plansza.up()
    plansza.goto(X,Y)
    plansza.down()
    pole()
    plansza.up()
    plansza.goto(X,Y-25)
    plamsz
   
def kolorZolwia(turtname,turtcol):
    turtname.color(turtcol)
    turtname.shape('circle')
    turtname.shapesize(2)

def pozycjaPiona(nazwapiona,X,Y):
    nazwapiona.up()
    nazwapiona.goto(X,Y)

def rysujPole(X,Y,nazwa_pola):
    plansza.up()
    plansza.goto(X,Y)
    plansza.down()
    pole()
    plansza.up()
    plansza.goto(X-12,Y)
    plansza.write(nazwa_pola, font=("Arial", 10, "bold"))
   
def kolorZolwia(turtname,turtcol):
    turtname.color(turtcol)
    turtname.shape('circle')
    turtname.shapesize(2)

rysujPole(0,25,'E')
rysujPole(0,175,'B')
rysujPole(-150,175,'A')
rysujPole(-150,25,'D')
rysujPole(-150,-125,'G')
rysujPole(0,-125,'H')
rysujPole(150,-125,'I')
rysujPole(150,25,'F')
rysujPole(150,175,'C')

g1 = turtle.RawTurtle(screen)

kolorZolwia(g1,'green')
pozycjaPiona(g1,-270,270)

g2 = turtle.RawTurtle(screen)
kolorZolwia(g2,'green')
pozycjaPiona(g2,-225,270)

g3 = turtle.RawTurtle(screen)
kolorZolwia(g3,'green')
pozycjaPiona(g3,-180,270)

r1 = turtle.RawTurtle(screen)
kolorZolwia(r1,'red')
pozycjaPiona(r1,270,-270)

r2 = turtle.RawTurtle(screen)
kolorZolwia(r2,'red')
pozycjaPiona(r2,225,-270)

r3 = turtle.RawTurtle(screen)
kolorZolwia(r3,'red')
pozycjaPiona(r3,180,-270)



ng1 = turtle.RawTurtle(screen, visible=False) #ng1 jest żółwiem, który pisze nazwę na g1
ng2 = turtle.RawTurtle(screen, visible=False)
ng3 = turtle.RawTurtle(screen, visible=False)

nr1 = turtle.RawTurtle(screen, visible=False)
nr2 = turtle.RawTurtle(screen, visible=False)
nr3 = turtle.RawTurtle(screen, visible=False)



def nazwaPiona(nazwa_piszacego_zolwia,nazwa_pionka,X,Y): #funkcja podpisuje piony
    nazwa_piszacego_zolwia.color('white')
    nazwa_piszacego_zolwia.up()
    nazwa_piszacego_zolwia.goto(X,Y-10)
    nazwa_piszacego_zolwia.write(nazwa_pionka, align='center', font=('Arial', 12, 'bold'))

def ruszPionaG1(X,Y):
    g1.up()
    g1.goto(X,Y-25)
    ng1.up()
    ng1.goto(X,Y-35)
    ng1.write('G1', align='center', font=('Arial', 12, 'bold'))

nazwaPiona(ng1,'G1',-270,270)
nazwaPiona(ng2,'G2',-225,270)
nazwaPiona(ng3,'G3',-180,270)

nazwaPiona(nr1,'R1',270,-270)
nazwaPiona(nr2,'R2',225,-270)
nazwaPiona(nr3,'R3',180,-270)






