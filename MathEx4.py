import numpy as np
from numpy.linalg import norm #tính norm
import math
"""

Ex3: Vector, Matrix, Scalar



Câu 1:
Cho:
2a + b + c = 4
a + 3b + 2c = 5
a = 6
Quy về Ax = B. Sau đó giải tìm x
Câu 2:"""
def timx():
     A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
# define matrix B
    B = np.array([4, 5, 6])
# linalg.solve: solve a system of linear scalar equations
    print("Solutions [a, b, c]:\n",np.linalg.solve(A, B))
""""
Câu 2: Gợi ý
Tạo 1 array points có 1000 phần tử cách đều nhau với start = -5, end = 5, step = 0.01
Tạo ma trận điểm có 1000 điểm với x,y = points, point bằng np.meshgrid
Tính thông qua ma trận điểm
Biểu diễn z
z = (x
""""
def bieudien()
    points = np.arange(-5, 5, 0.01)
    points[:20]
    x, y = np.meshgrid(points, points)
    x[:10]
    y[:10]
    z = np.sqrt(x ** 2 + y ** 2)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,8))
    plt.imshow(z, cmap=plt.cm.Blues)
    plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
       
