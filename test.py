import unittest
from main import EgyenletMegoldo

class Testing(unittest.TestCase):
    def setUp(self):
        print("setting up")
        self.tester = EgyenletMegoldo()

    def test_nincsMegoldas(self):
        print("Teszt 1: Nincs megoldás")
        self.assertEqual(self.tester.masodfoku_egyenlet(1, 2, 8), (None, None), "Nem szabad lennie megoldásnak!")

    def test_egyMegoldas(self):
        print("Teszt 2: Egy darab megoldás")
        self.assertEqual(self.tester.masodfoku_egyenlet(1, -14, 49), (7, 7), "Egy megoldása kell legyen!")

    def test_kettoMegoldas(self):
        print("Teszt 3: Egy darab megoldás")
        self.assertEqual(self.tester.masodfoku_egyenlet(1, 6, 8), (-2, -4), "Kettő megoldása kell legyen!")

    def test_TypeError(self):
        print("Teszt 4: Típus hiba")
        with self.assertRaises(TypeError):
            result = self.tester.masodfoku_egyenlet(True, False, False)


    def tearDown(self):
        print("tearing down")

if __name__ == '__main__':
    unittest.main()
