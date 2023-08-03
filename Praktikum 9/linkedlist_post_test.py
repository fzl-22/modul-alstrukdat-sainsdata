class Bus:
    def __init__(self, nomor_identifikasi, tujuan):
        self.nomor_identifikasi = nomor_identifikasi
        self.tujuan = tujuan
        self.next = None

class AntrianBus:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, nomor_identifikasi, tujuan):
        new_bus = Bus(nomor_identifikasi, tujuan)
        if self.tail:
            self.tail.next = new_bus
        else:
            self.head = new_bus
        self.tail = new_bus

    def dequeue(self):
        if self.head:
            nomor_identifikasi = self.head.nomor_identifikasi
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return nomor_identifikasi
        else:
            return "Antrian kosong."

    def display(self):
        if self.head:
            current = self.head
            bus_list = []
            while current:
                bus_list.append("B" + current.nomor_identifikasi + " (tujuan: " + current.tujuan + ")")
                current = current.next
            return ", ".join(bus_list)
        else:
            return "Antrian kosong."

antrian_bus = AntrianBus()

while True:
    print("Pilih perintah:")
    print("1. enqueue [nomor_identifikasi] [tujuan]")
    print("2. dequeue")
    print("3. display")
    print("4. Keluar")
    print()

    perintah = input("Masukkan nomor perintah: ")

    if perintah == "1":
        print()
        nomor_identifikasi = input("Masukkan nomor identifikasi bus: ")
        tujuan = input("Masukkan tujuan bus: ")
        print()
        antrian_bus.enqueue(nomor_identifikasi, tujuan)
        print("Bus B" + nomor_identifikasi + " dengan tujuan " + tujuan + " telah ditambahkan ke dalam antrian.")
    elif perintah == "2":
        print()
        nomor_identifikasi = antrian_bus.dequeue()
        if nomor_identifikasi == "Antrian kosong.":
            print(nomor_identifikasi)
        else:
            print("Bus B" + nomor_identifikasi + " telah dikeluarkan dari antrian.")
    elif perintah == "3":
        print()
        bus_antrian = antrian_bus.display()
        print("Bus yang sedang dalam antrian:", bus_antrian)
    elif perintah == "4":
        break
    else:
        print("Perintah tidak valid. Silakan masukkan nomor perintah yang valid.")
    print()
