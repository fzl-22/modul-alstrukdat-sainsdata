def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] >= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    print("partition :", A)
    return i + 1

def quickSort(A, low, high):
    if low < high:
        pivot_index = partition(A, low, high)
        print("pivot\t  :", A[pivot_index])
        quickSort(A, low, pivot_index - 1)
        quickSort(A, pivot_index + 1, high)

A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
print("A\t  :", A)
print()
quickSort(A, 0, len(A) - 1)
print()
print("result\t  :", A)