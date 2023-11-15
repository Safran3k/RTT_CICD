""" Másodfokű egyenlet megoldása python-ban """

import math

class EgyenletMegoldo():
    """ Egyenlet megoldó osztály """
    def masodfoku_egyenlet(self, a, b, c):
        """ Másodfokú egyenlet megoldó metódus """
        if type(a) not in [int,float] or type(b) not in [int,float] or type(c) not in [int,float]:
            raise TypeError('Csak int, float típus fogadható el!')

        # Diszkrimináns kiszámítása
        d = math.pow(b, 2) - (4 * a * c)
        if d < 0:
            return None, None

        return (-b + math.sqrt(d)) / 2 * a, (-b - math.sqrt(d)) / 2 * a

    def feladat_megoldo(self, a, b, c):
        """ Feladat megoldó ami a másodfokó eredményét írja ki """
        egyenlet = EgyenletMegoldo()
        x1, x2 = egyenlet.masodfoku_egyenlet(a, b, c)

        print(f"{a}^2 {b}x + {c} = 0")

        if (x1 is None) and (x2 is None):
            print("Nincs megoldás.")
        elif x1 == x2:
            print(f"Egy megoldás van: {x1}")
        else:
            print(f"Kettő megoldásunk van: {x1} és {x2}")


e = EgyenletMegoldo()
e.feladat_megoldo(1, 2, 8)
e.feladat_megoldo(1, -14, 49)
e.feladat_megoldo(1, 6, 8)
# e.feladatMegoldo("alma", 1, "körte")