# Копирую свой же метод Гаусса
def MatrixLambda(n,m,A,i,l):
    for j in range(m):
        A[i][j] *= l

def MatrixTwoLines(n,m,A,i,j,l):
    for j_1 in range(m):
        A[i][j_1] += l*A[j][j_1]

def MatrixSwitch(n,m,A,i,j):
    A[i],A[j]=A[j],A[i]
    
def CheckZeroLine(n,m,A,i):
    t = 1
    for j in range(m-1):
        if A[i][j]!=0:
            t = 0
    return t
        


def gauss(n,A):
    #Прямой ход Гаусса
    for i0 in range(n):

        for i in range(i0,n):
            if A[i][i0]!=0:
                MatrixSwitch(n, n+1, A, i0, i)
                break
        for i in range(i0+1,n):
            if A[i0][i0]!=0:
                
                MatrixTwoLines(n, n+1, A, i, i0, -A[i][i0]/A[i0][i0])
            
    
    #Обратный ход Гаусса
    for j in range(n-1,-1,-1):
        j1=j
        while A[j1][j]==0:
            j1-=1
        MatrixLambda(n, n+1, A, j1, 1/A[j1][j])
        for i in range(j1):
            MatrixTwoLines(n, n+1, A, i, j1, -A[i][j])
            
    for i in range(n):
        if CheckZeroLine(n,n+1,A,i):
            return None
    sols = [A[i][n] for i in range(n)]
        
    return sols






def T(A):
    '''Транспонирует матрицу'''
    n = len(A)
    A1 = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A1[i][j]=A[j][i]
    return A1

def LU(A):
    n = len(A)
    L = [[0]*n for i in range(n)]
    
    for j in range(n):
        s = A[j][j]
        for i in range(j):
            s-=(L[j][i])**2
        L[j][j] = s**0.5
        
        for i in range(j+1,n):
            s = A[i][j]
            for k in range(j):
                s -= L[i][k]*L[j][k]
            L[i][j] = s/L[j][j]
    return L

def Matrix(A,b):
    '''Добавляет в матрицу правый столбец'''
    n = len(A)
    B = [list(i) for i in A]
    for i in range(n):
        B[i].append(b[i])
    return B

n = int(input('Введите размер матрицы\n'))
A = [0]*n
print('Вводите матрицу построчно')
for i in range(n):
    A[i] = list(map(float,input().split()))
b = list(map(float,input('Введите b\n').split()))

L = LU(A)

L_T = T(L)

n = len(A)

y = gauss(n,Matrix(L,b))
x = gauss(n,Matrix(L_T,y))

print(x)
