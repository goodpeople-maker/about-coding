class persegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l  
    def luas(self):
        return self.p * self.l
        
    def keliling(self):
        print(f"Keliling = {2*(self.p + self.l)}")

    def hasil(self, p, l):
        print(f"Panjang  = {p}")
        print(f"Lebar    = {l}")
        print(f"Luas     = {p*l}")
        print(f"Keliling = {2*(p+l)}")


# terdapat 1 inisialisasi kelas, 1 fungsi dan 2 method
# Inisialisasi, yaitu __init__ yang merupakan kelas dijalankan pada saat proses inisialisasi. 
# Fungsi, yaitu luas(self) yang merupakan sebuah proses yang memiliki nilai keluaran (return). 
# Method, yaitu keliling(self) dan hasil(self,p,l) yang merupakan sebauh proses yang tidak memiliki nilai keluaran (return). 

a = persegiPanjang(10, 20)
print(f"Luas\t = {a.luas()}")
a.keliling()
a.hasil(15, 25)