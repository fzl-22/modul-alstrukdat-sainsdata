def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = int((high + low) / 2)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

start = int(input("Nilai Awal: "))
stop = int(input("Nilai Akhir: "))
step = int(input("Lompatan: "))
find = int(input("Bilangan yang dicari: "))

myList = [i for i in range(start, stop, step)]
resultIndex = binary_search(myList, find)
print(f"Bilangan {find} ada di index ke-{resultIndex}") if resultIndex != -1 else print("Bilangan tidak ditemukan")
