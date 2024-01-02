import numpy as np

def pendulum(m, l, state):
    n = len(m)
    A,B = np.zeros((n, n))
    E = np.ones(n)
    
    for i in range(n):
        for j in range(n):
            for k in range(max(i,j),n):
                A[i][j] += m[k]
                B[i][j] += m[k]
            if i == j:
                A[i][j] *= l[j]
                B[i][j] *= g * np.sin(state[2 * i])
            else:
                A[i][j] *= l[j] * np.cos(state[2 * i] - state[2 * j])
                B[i][j] *= l[j] * state[2 * j + 1] ** 2 * np.sin(state[2 * i] - state[2 * j])
    
    return -np.linalg.inv(A) @ B @ E

print(np.array([[1, 1 ,1],[1, 1, 1],[1, 1, 1]]) @ np.ones(3))
