class Mahasiswa:
    nim = None
    nama = None
    jenis_kelamin = None
    berkebutuhan_khusus = None
    
    def __init__(self, nim, nama, jenis_kelamin, berkebutuhan_khusus):
        self.nim = nim
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.berkebutuhan_khusus = berkebutuhan_khusus
        
    def showMahasiswa(self):
        is_berkebutuhan_khusus = "YES" if self.berkebutuhan_khusus == True else "NO" 
        nim = f"NIM\t\t\t: {self.nim}\n"
        nama = f"Nama\t\t\t: {self.nama}\n"
        jenis_kelamin = f"Jenis Kelamin\t\t: {self.jenis_kelamin}\n"
        berkebutuhan_khusus = f"Berkebutuhan Khusus\t: {is_berkebutuhan_khusus}\n"
        print(nim + nama + jenis_kelamin + berkebutuhan_khusus)
        

class DaftarMahasiswa:
    daftar = None
    
    def __init__(self):
        self.daftar = []
    
    def addMahasiswa(self, mahasiswa):
        self.daftar.append(mahasiswa)
    
    def deleteMahasiswa(self, nim):
        isAnyDeleted = False
        for i in range(len(self.daftar)):
            if(self.daftar[i].nim == nim):
                temp = self.daftar[i]
                self.daftar.remove(temp);
                print(f"Data mahasiswa dengan NIM {nim} telah berhasil dihapus.")
                isAnyDeleted = True
        if(isAnyDeleted == False):
            print("Mahasiswa tidak ditemukan...")

    def showDisabled(self):
        isAnyDisabled = False
        print("Daftar Mahasiswa Penyandang Disabilitas:")
        for i in range(len(self.daftar)):
            if(self.daftar[i].berkebutuhan_khusus):
                self.daftar[i].showMahasiswa()
                isAnyDisabled = True
        
        if isAnyDisabled == False:
            print('Tidak ada mahasiswa penyandang disabilitas')
    
    def printDaftar(self):
        print("Daftar Semua Mahasiswa")
        if len(self.daftar) == 0:
            print("Belum ada mahasiswa yang didaftarkan...")
            return
        for i in range(len(self.daftar)):
            self.daftar[i].showMahasiswa()
            

daftar = DaftarMahasiswa()

while True:
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Semua Data")
    print("4. Tampilkan Hanya Penyandang Disabilitas")
    option = input("Masukkan Pilihanmu: ")
    print()
    
    if option == "1":
        nim = int(input("Masukkan NIM: "))
        nama = input("Masukkan Nama: ")
        jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")
        berkebutuhan_khusus = eval(input("Masukkan Status Berkebutuhan Khusus (True/False): "))
        mahasiswa = Mahasiswa(nim, nama, jenis_kelamin, berkebutuhan_khusus)
        daftar.addMahasiswa(mahasiswa)
    elif option == "2":
        nim = int(input("Masukkan NIM: "))
        daftar.deleteMahasiswa(nim)
    elif option == "3":
        daftar.printDaftar()
    elif option == "4":
        daftar.showDisabled()
    elif option == "0":
        break
    else:
        print("Pilihan tidak valid!")
    print()

