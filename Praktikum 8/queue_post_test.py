class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
    
    def check(self):
        print(self.items)
        
    
N = input("Masukkan N: ")

mahasiswa = input("Masukkan Mahasiswa: ")
geprek = input("Masukkan geprek: ")

mahasiswa_list = mahasiswa.split(" ")
geprek_list = geprek.split(" ")

mahasiswa_queue = Queue()
geprek_queue = Queue()

for element in mahasiswa_list:
    mahasiswa_queue.enqueue(element)

for element in geprek_list:
    geprek_queue.enqueue(element)

mahasiswa_queue.check()
geprek_queue.check()

sizeMahasiswa = mahasiswa_queue.size()
counter = 0
while not mahasiswa_queue.is_empty():
    if mahasiswa_queue.peek() == geprek_queue.peek():
        mahasiswa_queue.dequeue()
        geprek_queue.dequeue()
        sizeMahasiswa = mahasiswa_queue.size()
        counter = 0
        continue
    
    counter += 1
    
    sizeMahasiswa = mahasiswa_queue.size()
    temp = mahasiswa_queue.peek()
    mahasiswa_queue.dequeue()
    mahasiswa_queue.enqueue(temp)
    
    if counter == sizeMahasiswa:
        break

mahasiswa_queue.check()
print(sizeMahasiswa)
    







