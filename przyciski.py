class Przyciski:        
    def set_pion(A,B):
            Przyciski.wlasciwy_pion.goto(A,B-25)
            Przyciski.piszacy_pion.clear()
            Przyciski.piszacy_pion.goto(A,B-35)
            Przyciski.piszacy_pion.write(Przyciski.pisana_nazwa_piona, align='center',font=('Arial', 12, 'bold'))

    def which_pion(Z,S,Y):
        sedzia = 'green'  
        tymczasowy_pion = None
        Przyciski.wlasciwy_pion = Z
        Przyciski.piszacy_pion = S
        Przyciski.pisana_nazwa_piona = Y
        if sedzia == 'red' and Przyciski.wlasciwy_pion == g1 or Przyciski.wlasciwy_pion == g2 or Przyciski.wlasciwy_pion == g3:
            print('Teraz kolej czerwonego')
        if sedzia == 'red' and Przyciski.wlasciwy_pion == r1 or Przyciski.wlasciwy_pion == r2 or Przyciski.wlasciwy_pion == r3:
            Przyciski.wlasciwy_pion = Z
            Przyciski.piszacy_pion = S
            Przyciski.pisana_nazwa_piona = Y
            tymczasowy_pion = Z
            sedzia = 'green'
            return
        if sedzia == 'green' and Przyciski.wlasciwy_pion == r1 or Przyciski.wlasciwy_pion == r2 or Przyciski.wlasciwy_pion == r3:
            print('Teraz kolej zielonego')
        if sedzia == 'green' and Przyciski.wlasciwy_pion == g1 or Przyciski.wlasciwy_pion == g2 or Przyciski.wlasciwy_pion == g3:
            Przyciski.wlasciwy_pion = Z
            Przyciski.piszacy_pion = S
            Przyciski.pisana_nazwa_piona = Y
            tymczasowy_pion = Z
            sedzia = 'red'
            return  
