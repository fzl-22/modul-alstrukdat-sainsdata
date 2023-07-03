# Modul 9 : Linked List

## Terminologi

Sebelum masuk ke definisi, ada baiknya kita mengenal terlebih dahulu istilah-istilah yang akan sering digunakan di dalam modul ini.

- Node : Sebuah node merepresentasikan satu elemen data yang dapat memiliki nilai/data serta memiliki _link_/_reference_ ke node lain.
- Head : Node pertama dari sebuah linked list.

## Definisi

Linked list merupakan salah satu struktur data yang menyimpan data dalam bentuk linear, yang mana tiap-tiap data direpresentasikan oleh node-node yang membentuk sekuens/barisan secara terurut. Dalam sebuah linked list, satu node terdiri dari:

- Data yang disimpan, dan
- Reference/link/pointer kepada node selanjutnya (reference ini berisi alamat memory dari node yang ditunjuk).

Contoh ilustrasi node:

![](images/node.jpeg)

Dengan ini, linked list digambarkan sebagai rangkaian node yang terhubung secara terurut. Misalkan, terdapat sebuah linkedlist `A = ["a", "b", "c", "d"]`. Maka linked list tersebut dapat digambarkan seperti gambar di bawah ini:

![](images/linkedlist.png)

Walaupun digambarkan secara terurut, sebenarnya data di dalam memory tidaklah terurut, melainkan terpencar-pencar (bisa dilihat dari alamat memory setiap node). Link/reference dari sebuah node tersebutlah yang berperan penting agar node-node dalam linked list tetap terhubung.

## Operasi Dasar

Berikut adalah operasi-operasi dasar dari linked list:

### 1. Representasi Node

Node direpresentasikan menggunakan class, perhatikan kode berikut:

```Python
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
```

### 2. Representasi Linked List

![](images/linkedlist.png)

Linked list direpresentasikan oleh node `head`. Node `head` ini nantinya yang akan memegang 'kendali' untuk node-node lainnya pada linked list:

```Python
class LinkedList:
    def __init__(self):
        self.head = None
```
Method-method di bawah ini adalah operasi-operasi dasar dari linkedlist.

#### 2.1 is_empty()

Method ini adalah method untuk mencari tahu apakah linked list kosong atau tidak:

```Python
def is_empty(self):
    return self.head is None
```

#### 2.2 push_back()

Method ini berfungsi untuk menambahkan data baru di bagian paling belakang linked list:

```Python
def push_back(self, data):
    # buat node baru
    new_node = Node(data);
    
    # jika linked list kosong, maka data baru terletak di node head
    if self.is_empty():
        self.head = new_node
        return
      
    # jika tidak kosong, telusuri hingga node paling akhir
    current_node = self.head
    while current_node.next:
        current_node = current_node.next

    # Arahkan pointer dari node paling akhir ke node baru.
    current_node.next = new_node
```

####  2.3 push_front()

![](images/push_front.png)

Method ini berfungsi untuk menambahkan data baru di bagian paling depan linked list:

```Python
def push_front(self, data):
    # buat node baru
    new_node = Node(data)
    
    # jika linked list kosong, node head adalah node baru
    if self.is_empty():
        self.head = new_node
        return
    
    # jika linked list tidak kosong, arahkan pointer dari 
    # node baru ke node head, kemudian ganti node head menjadi node
    # yang baru
    new_node.next = self.head
    self.head = new_node
```

#### 2.4 delete()

![](./images/delete.png)

Method ini berfungsi untuk menghapus data yang ingin dihapus dalam sebuah linked list:

```Python
def delete(self, data):
    # jika list kosong, jangan lakukan apa-apa
    if self.is_empty():
        return
    
    # jika data yang dihapus adalah head, pindahkan status head ke node selanjutnya
    if self.head.data == data:
        self.head = self.head.next
        return
    
    # siapkan node saat ini dan node sebelumnya untuk penelusuran
    current_node = self.head
    prev_node = None
    
    # lakukan penelusuran
    while current_node:
        # bila node saat ini sama dengan yang dicari,
        # hubungkan node sebelumnya ke node selanjutnya
        if current_node.data == data:
            prev_node.next = current_node.next
            return
        # iterasikan node
        prev_node = current_node
        current_node = current_node.next
```

### 3. Implementasi Penuh

```Python
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push_back(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def push_front(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    
    def delete(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        prev_node = None
        
        while current_node:
            if current_node.data == data:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node =  current_node.next
        print("None")

def main():
    linked_list = LinkedList()
    
    linked_list.push_front(0)
    linked_list.push_front(3)
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_front(0)
    linked_list.push_back(3)
    linked_list.delete(2)
    linked_list.print_list()

if __name__ == "__main__":
    main()
```