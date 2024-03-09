import numpy as np

def DecompositionLU(A):
    n = len(A)
    L = np.eye(n)
    U = np.copy(A)
    
    for k in range(n-1):
        for i in range(k+1, n):
            L[i, k] = U[i, k] / U[k, k]
            for j in range(k, n):
                U[i, j] = U[i, j] - L[i, k] * U[k, j]
    
    return L, U

def ResolutionSysteme(L, U, b):
    n = len(L)
    y = np.zeros(n) #Initialiser un vecteur y et de taille n pour stocker les résultats de la substitution avant.
    x = np.zeros(n) #Initialiser le vecteur solution x de taille n.
    
    # Etape de substitution avant (Ly = b)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] = y[i] - L[i, j] * y[j]
    
    # Etape de substitution arrière (Ux = y)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] = x[i] - U[i, j] * x[j]
        x[i] = x[i] / U[i, i]
    
    return x

def fill_matrix_A():
    n = int(input("Enter the size of the square matrix A: "))
    A = np.zeros((n, n))
    print("Enter the elements of the matrix A row-wise:")
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"A[{i+1},{j+1}]: "))
    return A

# Main program
A = fill_matrix_A()
print("Matrix A:")
print(A)

det = np.linalg.det(A)
print("le determinant est : ",det)
if (det !=0):
 L, U = DecompositionLU(A)
 print("\nLower Triangular Matrix L:")
 print(L)
 print("\nUpper Triangular Matrix U:")
 print(U)
 num_elements = len(A)


 b = np.array([float(input(f"Enter the value of b[{i+1}]: ")) for i in range(len(A))])
 b_column = b.reshape(num_elements, 1)
 print("\nVector b:")
 print(b_column)

 x = ResolutionSysteme(L, U, b)
 x_column = x.reshape(num_elements, 1)
 print("\nSolution Vector x:")
 print(x_column)
else :
     print("cette matrice n'avez pas de resolution.")