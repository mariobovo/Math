import numpy as np
from numpy.linalg import norm #tính norm
import math
import random

"""

Ex3: Vector, Matrix, Scalar



Câu 1:
Viết function cal_scalar_mult(v, b) với v là vector hoặc ma trận (numpy array) và b là scalar.
Hãy thực hiện việc tính toán theo vector/hai ma trận và scalar được truyền vào. Kết quả trả về
là một vector/ma trận tương ứng.
Gọi function này với các vector/ma trận và scalar khác nhau để xem kết quả
"""
def cal_scalar_mult(v, b):
    return v * b
"""
Câu 2: Gợi ý
Hãy viết function cho phép người dùng nhập vào 1 ma trận [mxn].
Hãy viết function cho phép người dùng nhập vào 1 vector [n]
Thực hiện phép nhân ma trận với vector trên
"""
def create_matrix(m, n):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            s= "M[" + str(i+1) + "," + str(j+1) + "]:"
            x = eval(input(s))
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)
def create_vector(n):
    lst = []
    for i in range(n):
        s= "v[" + str(i+1) + "]:"
        x = eval(input(s))
        lst.append(x)
    return np.array(lst)
def create_matrix_random(m, n, start, end):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            x = random.randint(start,end+1)
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)
def create_vector_random(n, start, end):
    lst = []
    for i in range(n):
        x = random.randint(start,end+1)
        lst.append(x)
    return np.array(lst)
"""
Câu 4: Gợi ý
Tạo matrix X(3x4) có giá trị trong khoảng 0-11
Tìm ma trận chuyển vị của matrix X
"""
def chuyenvi():
    X=np.arange(12).reshape((3, 4))
    return X.transpose()
"""
Câu 5: Gợi ý
Tạo ma trận A(2,2) với các giá trị số ngẫu nhiên từ 1 đến 4
Tạo ma trận nghịch đảo B từ ma trận A
Tìm I
"""
def ngichdao():
    A = create_matrix_random(2, 2, 1, 4)
    from numpy.linalg import inv
    B = inv(A)
    I = A.dot(B)
    return I
"""
Câu 6:
Tạo ma trận C(5,5) với các giá trị số ngẫu nhiên từ 5 đến 10
Tính tổng các phần tử trên đường chéo chính (trace)
Tính định thức (determinant) của C
Tìm hạng (rank) của ma trận C
"""
def hangmatran():
    A = create_matrix_random(5, 5, 5, 10)
    trA = np.trace(A)
    print ("tong phan tu tren duong treo" ,trA)
    from numpy.linalg import det
    detA = det(A)
    print ("dinh thuc " ,detA)
    from numpy.linalg import matrix_rank
    mrA = matrix_rank(A)
    print ("hang ma tran " ,mrA)

"""

Câu 7: Cho Ax = B (Gợi ý)
Tạo ma trận A(3x3) với các giá trị ngẫu nhiên từ 1 đến 6
Tạo vector b với 3 giá trị ngẫu nhiên tử 1 đển 3
Tìm vector x của Ax = b
"""
def timvector():
    A = create_matrix_random(3, 3, 1, 6)
    b = create_vector_random(3, 1, 3)
    A_1 = inv(A)
    x = A_1.dot(b)
