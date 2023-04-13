def bubbleSort(A):
    for i in range(len(A)):
        swapped = False
        for j in range(0, len(A) - i - 1):
            if A[j][1] < A[j + 1][1]:  # coba ganti tandanya menjadi <, apa yang terjadi?
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break


kalimat = input()
huruf = []

for i in kalimat:
    if([i, kalimat.count(i)] not in huruf):
        huruf.append([i, kalimat.count(i)])

bubbleSort(huruf)
for i in range(0, 3):
    print(huruf[i])
