import numpy as np
from numpy.linalg import norm #tính norm
import math
from scipy.sparse import csr_matrix
from MathEx1_2 import create_matrix_random
"""

Ex5: Sparse Matrix
Câu 1:
Tạo ma trận A(5,5) với các giá trị ngẫu nhiên từ -10 đến 5
Thay thế tất cả các phần tử <0 bằng 0 trong ma trận A
Tạo sparse matrix S từ A
Tính sparsity của sparse matrix
    
"""
def matranthuthot():
    A = create_matrix_random(5, 5, -10, 5)
    A[A < 0] = 0
    S = csr_matrix(A)
    sparsity = 1.0 - np.count_nonzero(A)/A.size
""""
Câu 2: Gợi ý
Một trong những ứng dụng thực sự của ma trận thưa thớt là giảm không gian rất lớn để lưu trữ
ma trận thưa thớt.
Hãy tạo ra một ma trận BigA(1000, 1000) phần tử ngẫu nhiên tử -10 đến 5.
Thay thế tất cả các phần tử <0 bằng 0 trong ma trận BigA
Tính kích thước của ma trận BigA
Tạo sparse matrix BigS từ BigA
Tích kích thước của BigS
Tính sparsity của sparse matrix
Trực quan hóa BigS
"""
def trucquan():
    BigA = create_matrix_random(1000, 1000, -10, 5)
    BigA[BigA < 0] = 0
    BigA.nbytes
    BigA_size = BigA.nbytes/(1024**2)
    print('Size of full matrix with zeros:', BigA_size ,'MB')
    BigS = csr_matrix(BigA)
    BigS.data.nbytes
    plt.figure(figsize=(10,10))
    plt.spy(BigS, markersize=0.1)
    BigS_size = BigS.data.nbytes/(1024**2)
    print('Size of sparse csr_matrix:', BigS_size ,'MB')
"""
Tạo ma trận thưa thớt ngẫu nhiên S(5,5) với mật độ cụ thể density = 0.25.
Ghi chú:
Giá trị mật độ (Density value) có nghĩa là ma trận được tạo là một full matrix với density =
0 có nghĩa là ma trận được tạo ra không có các item khác 0. Tương tự, density = 0.5 có
nghĩa là ma trận có 50% số item khác 0.
Chuyển S thành full matrix A
Tạo ma trận thưa thớt ngẫu nhiên S1(5,5) với mật độ cụ thể density = 0.25 và item khác 0 sẽ
bằng 1
Chuyển S1 thành full matrix A1
Trực quan hóa S, S1
"""
def trucquanthuathot():
    import scipy.sparse as sparse
    import scipy.stats as stats
    import numpy as np
    import matplotlib.pyplot as plt
    np.random.seed(42)
    # create sparse matrix with density 0.25
    S = sparse.random(5, 5, density=0.25)
    A = S.toarray()
    plt.spy(S)
    S1 = sparse.random(5, 5, density=0.25, data_rvs=np.ones) 
    A1=S1.toarray()
    plt.spy(S1)
