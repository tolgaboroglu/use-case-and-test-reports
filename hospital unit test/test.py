import unittest 
import coverage
from numpy import testing

from hospitall import Hospital

cov = coverage.Coverage()
cov.start()

class hospTestInfo(unittest.TestCase):
     
     #isminin atu hospital olmasını test eder
    def test_non_hosp(self):
        h = Hospital("ATU HOSPİTAL",False,10000)
        self.assertEqual(h.test_H(),500)
     
    def test_hosp(self): 
        h=Hospital("ATU HOSPITAL",True)
        self.assertEqual(h.testing_h())
        unittest.main()
    #klinik isminin doğru olup olmadığını test eder
    def test_clinic_name(self):
        h=Hospital("Korona",True)
        unittest.main()
    def test_non_clinic_name(self): 
        h=Hospital("Korona",False)
        unittest.main()
    def test_clinic_name(self):
        h=Hospital("Dahiliye",True)
        unittest.main()
    def test_non_clinic_name(self):
        h=Hospital("Dahiliye",False) 
        unittest.main()
    def test_clinic_name(self):
        h=Hospital("Cildiye",True)
        unittest.main()
    def test_non_clinic_name(self):
        h=Hospital("Cildiye",False)
        unittest.main()
    def test_clinic_name(self):
        h=Hospital("Nöroloji",True)
        unittest.main()
    def test_non_clinic_name(self):
        h=Hospital("Nöroloji",False)
        unittest.main()
    def test_clinic_name(self):
        h=Hospital("Kulak Burun Boğaz",True)
        unittest.main()
    def test_non_clinic_name(self):
        h=Hospital("Kulak Burun Boğaz",False)
        unittest.main()
    #giris butonunu test eder
    
    def test_giris(self):
        h=Hospital("Giris",True)
        unittest.main()
    def test_giris(self):
        h=Hospital("Giris",False)
        unittest.main()
    

    
    if __name__ == '__main__':
        unittest.main()
    