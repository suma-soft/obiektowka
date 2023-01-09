import turtle
import tkinter as tk









if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=600)
    canvas.pack(side=tk.RIGHT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("blue")



class Przyciski:        

    def set_pion(A,B):
        Przyciski.wlasciwy_pion.goto(A,B-25)
        Przyciski.piszacy_pion.clear()
        Przyciski.piszacy_pion.goto(A,B-35)
        Przyciski.piszacy_pion.write(Przyciski.pisana_nazwa_piona, align='center', font=('Arial', 12, 'bold'))

    def which_pion(Z,S,Y):
        Przyciski.wlasciwy_pion = Z
        Przyciski.piszacy_pion = S
        Przyciski.pisana_nazwa_piona = Y
        
        print (Przyciski.wlasciwy_pion)
        return Przyciski.wlasciwy_pion
        return Przyciski.piszacy_pion
        



b1 = tk.Button(root, relief="sunken", text="G1", command=lambda: Przyciski.which_pion(g1,ng1,'G1'))
b2 = tk.Button(root, relief="sunken", text="G2", command=lambda: Przyciski.which_pion(g2,ng2,'G2'))
b3 = tk.Button(root, relief="sunken", text="G3", command=lambda: Przyciski.which_pion(g3,ng3,'G3'))
b4 = tk.Button(root, relief="sunken", text="R1", command=lambda: Przyciski.which_pion(r1,nr1,'R1'))
b5 = tk.Button(root, relief="sunken", text="R2", command=lambda: Przyciski.which_pion(r2,nr2,'R2'))
b6 = tk.Button(root, relief="sunken", text="R3", command=lambda: Przyciski.which_pion(r3,nr3,'R3'))

b7 = tk.Button(root, text="A", command=lambda: Przyciski.set_pion(-150,175))
b8 = tk.Button(root, text="B", command=lambda: Przyciski.set_pion(0,175))
b9 = tk.Button(root, text="C", command=lambda: Przyciski.set_pion(150,175))
b10 = tk.Button(root, text="D", command=lambda: Przyciski.set_pion(-150,25))
b11 = tk.Button(root, text="E", command=lambda: Przyciski.set_pion(0,25))
b12 = tk.Button(root, text="F", command=lambda: Przyciski.set_pion(150,25))
b13 = tk.Button(root, text="G", command=lambda: Przyciski.set_pion(-150,-125))
b14 = tk.Button(root, text="H", command=lambda: Przyciski.set_pion(0,-125))
b15 = tk.Button(root, text="I", command=lambda: Przyciski.set_pion(150,-125))

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()
b10.pack()
b11.pack()
b12.pack()
b13.pack()
b14.pack()
b15.pack()


    
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






