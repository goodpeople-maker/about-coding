class Buku:
    def __init__(self,nama_buku,jenis, tahun_terbit, penerbit, penulis, jumlah_halaman):
        self.__nama_buku = nama_buku #.__ adalah private
        self.jenis = jenis
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    #buat fungsi untuk mencetak semua informasi buku tersebut
    def cetak(self):
        print(f"Nama Buku\t: {self.__nama_buku} \nJenis Buku\t: {self.jenis} \nTahun Terbit\t: {self.tahun_terbit} \nPenerbit\t: {self.penerbit} \nPenulis\t\t: {self.penulis} \nJumlah Halaman\t: {self.jumlah_halaman}")

buku = Buku("Harry Potter And The Cursed Child", "Fiksi", 2016, "Gramedia", "J.K. Rowling", 384)
buku.cetak()

#                                            >>>>> SOAL <<<<<

# Pada sebuah perpustakaan “Home Learning is Best” terdapat berbagai jenis buku yang berbeda-beda. 
# Pada suatu hari seorang pegawai perpus diminta oleh bosnya untuk mendaftarkan setiap buku yang ada diperpustakaan. 
# Tentunya pada daftar tersebut harus dapat memuat nama buku, jenis, tahun terbit, penerbit, penulis serta jumlah halaman dari buku tersebut.  
# Setelah itu, bosnya juga mau untuk nama buku hanya bisa diakses pada pendataan saja dan tidak boleh diketahui sama orang lain. Hal ini dilakukan supaya menjaga kerahasiaan dari buku tersebut. 


#                                           ===== SOLUSI =====
# Pada buku tersebut nantinya terdapat nama buku, jenis, tahun terbit, penerbit, penulis serta jumlah halaman. 
# Itu semua merupakan atribut dari buku tersebut. Namun, ada 1  atribut yang harus menggunakan private yaitu atribut nama buku.