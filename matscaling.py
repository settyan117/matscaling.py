from copy import deepcopy


def matscaling_x_once(A, r, x, y):
    x = deepcopy(x)
    for i in range(len(x)):
        x[i] = r[i]/sum(A[i][j]*y[j] for j in range(len(y)))
    return x


def matscaling_y_once(A, c, x, y):
    y = deepcopy(y)
    for j in range(len(y)):
        y[j] = c[j]/sum(A[i][j]*x[i] for i in range(len(x)))
    return y


def matscaling_xy(A, r, c, n):
    x = [1]*len(r)
    y = [1]*len(c)
    for i in range(n):
        for i in range(len(x)):
            x[i] = r[i]/sum(A[i][j]*y[j] for j in range(len(y)))
        for j in range(len(y)):
            y[j] = c[j]/sum(A[i][j]*x[i] for i in range(len(x)))
    return x, y


def matscaling_Arow_once(A, r):
    A1 = deepcopy(A)
    Arowsum = [sum(A[i][j] for j in range(len(A[0]))) for i in range(len(r))]
    for i in range(len(r)):
        for j in range(len(A[0])):
            A1[i][j] = A[i][j]*r[i]/Arowsum[i]
    return A1


def matscaling_Acol_once(A, c):
    A1 = deepcopy(A)
    Acolsum = [sum(A[i][j] for i in range(len(A))) for j in range(len(c))]
    for i in range(len(c)):
        for j in range(len(A)):
            A1[j][i] = A[j][i]*c[i]/Acolsum[i]
    return A1


def matscaling_A(A, r, c, n):
    for i in range(n):
        A = matscaling_Arow_once(A, r)
        A = matscaling_Acol_once(A, c)
    return A
