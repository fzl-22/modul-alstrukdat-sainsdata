def insertionSort(A):
    for step in range(1, len(A)):
        key = A[step]
        j = step - 1
        
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j = j - 1
        
        A[j + 1] = key
        print(A)

A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
print("A\t  :", A)
print()
insertionSort(A)
print()
print("result\t  :", A)