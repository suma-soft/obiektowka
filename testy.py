import unittest

class TestPola(unittest.TestCase):
    def test_fA(self):
        matryca = [['empty', 'empty', 'empty'],
                   ['empty', 'empty', 'empty'],
                   ['empty', 'empty', 'empty']]
        fields.field_A = 'empty'
        Przyciski.pisana_nazwa_piona = 'red'
        Pola.fA(0, 0)
        self.assertEqual(matryca, [['red', 'empty', 'empty'],
                                    ['empty', 'empty', 'empty'],
                                    ['empty', 'empty', 'empty']])
        self.assertEqual(fields.field_A, 'red')
        
    def test_fA_occupied(self):
        matryca = [['red', 'empty', 'empty'],
                   ['empty', 'empty', 'empty'],
                   ['empty', 'empty', 'empty']]
        fields.field_A = 'red'
        Przyciski.pisana_nazwa_piona = 'red'
        Pola.fA(0, 0)
        self.assertEqual(matryca, [['red', 'empty', 'empty'],
                                    ['empty', 'empty', 'empty'],
                                    ['empty', 'empty', 'empty']])
        self.assertEqual(fields.field_A, 'red')
        
# Analogiczne testy dla pozostałych metod (fB, fC, itd.)

if __name__ == '__main__':
    unittest.main()
