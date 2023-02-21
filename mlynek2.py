import turtle
import tkinter as tk



if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=600)
    canvas.pack(side=tk.RIGHT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("light green")

tymczasowy_pion = None
sedzia = 'green'
matryca = [[0,0,0],
           [0,0,0],
           [0,0,0]]

class Przyciski:
    blokada_set_pion = False
    
    @classmethod
    def set_pion(cls, A, B):
        if cls.blokada_set_pion:
            return
        
        Przyciski.wlasciwy_pion.goto(A, B - 25)
        Przyciski.piszacy_pion.clear()
        Przyciski.piszacy_pion.goto(A, B - 35)
        Przyciski.piszacy_pion.write(Przyciski.pisana_nazwa_piona, align='center', font=('Arial', 12, 'bold'))
        
    @classmethod
    def which_pion(cls, Z, S, Y):
        global sedzia
        Przyciski.wlasciwy_pion = Z
        Przyciski.piszacy_pion = S
        Przyciski.pisana_nazwa_piona = Y
        
        if sedzia == 'red' and Przyciski.wlasciwy_pion in (g1, g2, g3):
            print('Teraz kolej czerwonego')
            cls.blokada_set_pion = True
            
        elif sedzia == 'red' and Przyciski.wlasciwy_pion in (r1, r2, r3):
            sedzia = 'green'
            cls.blokada_set_pion = False
        
        elif sedzia == 'green' and Przyciski.wlasciwy_pion in (r1, r2, r3):
            print('Teraz kolej zielonego')
            cls.blokada_set_pion = True
            
        elif sedzia == 'green' and Przyciski.wlasciwy_pion in (g1, g2, g3):
            sedzia = 'red'
            cls.blokada_set_pion = False

            
class Checker:
    def __init__(self, matryca):
        self.matryca = matryca

    def check_line(self, line, player):
        return line.count(player) == 3

    def check_diagonal(self, player):
        if self.matryca[0][0] == self.matryca[1][1] == self.matryca[2][2] == player:
            return True
        if self.matryca[0][2] == self.matryca[1][1] == self.matryca[2][0] == player:
            return True
        return False

    def check_win(self):
        for i in range(3):
            if self.check_line(self.matryca[i], 'g') or self.check_line([row[i] for row in self.matryca], 'g'):
                return "Wygrał gracz zielony!"
            elif self.check_line(self.matryca[i], 'r') or self.check_line([row[i] for row in self.matryca], 'r'):
                return "Wygrał gracz czerwony!"
        if self.check_diagonal('g'):
            return "Wygrał gracz zielony!"
        elif self.check_diagonal('r'):
            return "Wygrał gracz czerwony!"
        return "Gra toczy się dalej."
    


class Pola:
    global matryca
    def fA(X,Y):
        if fields.field_A == 'empty' and Przyciski.blokada_set_pion == False:
           matryca[X][Y]=Przyciski.pisana_nazwa_piona
           Przyciski.set_pion(-150,175)
           print(matryca)
        elif fields.field_A != 'empty':
            print ('To pole jest zajęte')
            

    def fB(X,Y):
        if fields.field_B == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(0,175)
        else:
            print ('To pole jest zajęte')

    def fC(X,Y):
        if fields.field_C == 'empty' and Przyciski.blokada_set_pion == False:
           matryca[X][Y]=Przyciski.pisana_nazwa_piona
           Przyciski.set_pion(150,175)
        else:
            print ('To pole jest zajęte')

    def fD(X,Y):
        if fields.field_D == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(-150,25)
        else:
            print ('To pole jest zajęte')

    def fE(X,Y):
        if fields.field_E == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(0,25)
        else:
            print ('To pole jest zajęte')

    def fF(X,Y):
        if fields.field_F == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(150,25)
        else:
            print ('To pole jest zajęte')

    def fG(X,Y):
        if fields.field_G == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(-150,-125)
        else:
            print ('To pole jest zajęte')

    def fH(X,Y):
        if fields.field_H == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(0,-125)
        else:
            print ('To pole jest zajęte')
            
    def fI(X,Y): 
        if fields.field_I == 'empty' and Przyciski.blokada_set_pion == False:
            matryca[X][Y]=Przyciski.pisana_nazwa_piona
            Przyciski.set_pion(150,-125)
        else:
            print ('To pole jest zajęte')

class sweeper:
    global matryca
    def unload():
        for i in range(len(matryca)):
            for j in range(len(matryca[i])):
                if matryca[i][j] == Przyciski.pisana_nazwa_piona:
                    matryca[i][j] = 0
                    print(matryca)
            
    def load():
        if matryca[0][0]!=0:
            fields.field_A = 'busy'
        if matryca[0][1]!=0:
            fields.field_B = 'busy'
        if matryca[0][2]!=0:
            fields.field_C = 'busy'
        if matryca[1][0]!=0:
            fields.field_D = 'busy'
        if matryca[1][1]!=0:
            fields.field_E = 'busy'
        if matryca[1][2]!=0:
            fields.field_F = 'busy'
        if matryca[2][0]!=0:
            fields.field_G = 'busy'
        if matryca[2][1]!=0:
            fields.field_H = 'busy'
        if matryca[2][2]!=0:
            fields.field_I = 'busy'
        return
        print(matryca)


class fields:          
        field_A = 'empty'
        field_B = 'empty'
        field_C = 'empty'
        field_D = 'empty'
        field_E = 'empty'
        field_F = 'empty'
        field_G = 'empty'
        field_H = 'empty'
        field_I = 'empty'


checker = Checker(matryca)


b1 = tk.Button(root, background='dark grey', text="G1", command=lambda: [Przyciski.which_pion(g1,ng1,'G1'), sweeper.unload()])
b2 = tk.Button(root, background='dark grey', text="G2", command=lambda: [Przyciski.which_pion(g2,ng2,'G2'), sweeper.unload()])
b3 = tk.Button(root, background='dark grey', text="G3", command=lambda: [Przyciski.which_pion(g3,ng3,'G3'), sweeper.unload()])
b4 = tk.Button(root, background='dark grey', text="R1", command=lambda: [Przyciski.which_pion(r1,nr1,'R1'), sweeper.unload()])
b5 = tk.Button(root, background='dark grey', text="R2", command=lambda: [Przyciski.which_pion(r2,nr2,'R2'), sweeper.unload()])
b6 = tk.Button(root, background='dark grey', text="R3", command=lambda: [Przyciski.which_pion(r3,nr3,'R3'), sweeper.unload()])

b7 = tk.Button(root, text="A", command=lambda: [Pola.fA(0,0), sweeper.load(), checker.check_win()])
b8 = tk.Button(root, text="B", command=lambda: [Pola.fB(0,1), sweeper.load(), checker.check_win()])
b9 = tk.Button(root, text="C", command=lambda: [Pola.fC(0,2), sweeper.load(), checker.check_win()])
b10 = tk.Button(root, text="D", command=lambda: [Pola.fD(1,0), sweeper.load(), checker.check_win()])
b11 = tk.Button(root, text="E", command=lambda: [Pola.fE(1,1), sweeper.load(), checker.check_win()])
b12 = tk.Button(root, text="F", command=lambda: [Pola.fF(1,2), sweeper.load(), checker.check_win()])
b13 = tk.Button(root, text="G", command=lambda: [Pola.fG(2,0), sweeper.load(), checker.check_win()])
b14 = tk.Button(root, text="H", command=lambda: [Pola.fH(2,1), sweeper.load(), checker.check_win()])
b15 = tk.Button(root, text="I", command=lambda: [Pola.fI(2,2), sweeper.load(), checker.check_win()])

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



ng1 = turtle.RawTurtle(screen, visible=False)
ng2 = turtle.RawTurtle(screen, visible=False)
ng3 = turtle.RawTurtle(screen, visible=False)

nr1 = turtle.RawTurtle(screen, visible=False)
nr2 = turtle.RawTurtle(screen, visible=False)
nr3 = turtle.RawTurtle(screen, visible=False)



def nazwaPiona(nazwa_piszacego_zolwia,nazwa_pionka,X,Y):
    nazwa_piszacego_zolwia.color('white')
    nazwa_piszacego_zolwia.up()
    nazwa_piszacego_zolwia.goto(X,Y-10)
    nazwa_piszacego_zolwia.write(nazwa_pionka, align='center', font=('Arial', 12, 'bold'))

nazwaPiona(ng1,'G1',-270,270)
nazwaPiona(ng2,'G2',-225,270)
nazwaPiona(ng3,'G3',-180,270)

nazwaPiona(nr1,'R1',270,-270)
nazwaPiona(nr2,'R2',225,-270)
nazwaPiona(nr3,'R3',180,-270)



