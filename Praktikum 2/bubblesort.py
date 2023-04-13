def bubbleSort(A):
    for i in range(len(A)):
        swapped = False
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break
  
A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
bubbleSort(A)
print(A)