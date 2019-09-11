import numpy as np
from numpy.linalg import norm #tính norm
import math
"""
Câu 1:
Viết function cal_vectors(op, u, v) với op là một trong các toán tử +, -, *, /, "dot"; u và v là vector
(numpy array). Hãy thực hiện việc tính toán theo toán tử và hai vector được truyền vào. Kết
quả trả về là một vector/giá trị tương ứng.
Gọi function này với các toán tử khác nhau để xem kết quả
"""
def cal_vectors(op, u, v):
    result = None
    if op == "+":
        result = u + v
    elif op == "-":
        result = u - v
    elif op == "*":
        result = u * v
    elif op == "/":
        result = u / v
    elif op=="dot":
        result = u.dot(v)
    else:
        result = None
    return result
"""
Câu 2: Vector Norm
Viết function cal_vector_norm(t, v) với t là một trong các loại L1, L2, Max; v là vector. Hãy thực
hiện việc tính toán theo loại và vector được truyền vào. Kết quả trả về là một giá trị tương ứng.
Gọi function này với các loại khác nhau để xem kết quả
""""
def cal_vector_norm(t, v):
    result = None
    if t == "L1":
        result = norm(v,1) # lấy tổng
    elif t =="L2":
        result = norm(v) #lấy căn tông bình phương
    elif t == "Max":
        result = norm(v, math.inf) # lay max giá trị 
    else:
        result = None
    return result

"""
Ex2: Matrices
Câu 1:
Viết function cal_matrices(op, m1, m2) với op là một trong các toán tử +, -, *, /; m1 và m2 là ma
trận (numpy array). Hãy thực hiện việc tính toán theo toán tử và hai ma trận được truyền vào.
Kết quả trả về là một ma trận/giá trị tương ứng.
Gọi function này với các toán tử khác nhau để xem kết quả
"""
def cal_matrices(op, m1, m2):
    result = None
    if op == "+":
        result = m1 + m2
    elif op == "-":
        result = m1 - m2
    elif op == "*":
        result = m1 * m2
    elif op == "/":
        result = m1 / m2
    else:
        result = None
    return result

"""
Câu 2:
Cho ma trận A = [[1, 3, 3], [4, 5, 6], [7, 8, 9]] và ma trận B = [[2, 3], [6, 8], [5, 7]]
Thực hiện dot product cho A.B bằng dot và @
"""
def cal_dot():
    A = np.matrix([[1, 3, 3], [4, 5, 6], [7, 8, 9]])
    B = np.matrix( [[2, 3], [6, 8], [5, 7]])
    A_dot_B = A.dot(B)
    print ("A.dot(B)")
    print (A_dot_B)
    print ("A@B")
    print (A@B)
