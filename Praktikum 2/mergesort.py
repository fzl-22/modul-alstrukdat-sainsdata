def mergeSort(A):
    if len(A) > 1:
        mid = int(len(A)/2) # cari pembagi array (median index)
        L = A[:mid] # inisiasikan subarray dari 0 hingga mid - 1
        R = A[mid:] # inisiasikan subarray dari mid hingga len(A) - 1
        
        mergeSort(L) # urutkan subarray di kiri dengan recursive call
        mergeSort(R) # urutkan subarray di kiri dengan recursive call
 
        i = j = k = 0
 
        # proses sorting setiap subarray
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1
 
        # proses merging dari subarray kiri dan kanan ke array A
        while i < len(L):
            A[k] = L[i]
            i = i + 1
            k = k + 1
 
        while j < len(R):
            A[k] = R[j]
            j = j + 1
            k = k + 1
            
A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
mergeSort(A)
print(A)
 