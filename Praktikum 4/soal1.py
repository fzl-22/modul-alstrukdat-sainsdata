import numpy as np

M, N, x = tuple(map(int, input().split(' '))) # tuple unpacking

hutan_lindung = np.random.randint(1, 100, size=(M, N))

print("Hutan sebelum penebangan:\n", hutan_lindung)
for i in range(M):
    for j in range(N):
        if hutan_lindung[i][j] > x:
            hutan_lindung[i][j] = 0

print()

print("Hutan setelah penebangan:\n", hutan_lindung)