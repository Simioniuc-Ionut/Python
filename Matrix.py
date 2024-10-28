#Write a Python class that simulates a matrix of size NxM, with N and M provided at
# initialization. The class should provide methods to access elements (get and set methods)
# and some mathematical functions such as transpose, matrix multiplication and a method that
# allows iterating through all elements from a matrix an apply a transformation over them
# (via a lambda function).
import numpy as np
class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.matrix=[[ 0 for j in range(cols)] for i in range(rows)]

    def get(self,i,j):
        return self.matrix[i][j]
    def set(self,new_val,i,j):
        self.matrix[i][j]=new_val
    def transpose(self):
        t_matrix=[[ 0 for i in range(self.rows)] for j in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                t_matrix[j][i]=self.matrix[i][j]
        return  t_matrix
    def dot_product(self,matrix):
        mat1 =np.array(self.matrix)
        mat2 = np.array(matrix)
        if mat1.shape[1] != mat2.shape[0]:
            return None
        mat3=mat1 @ mat2
        return mat3.tolist()
    def apply_fun(self,func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]=func(self.matrix[i][j])

if __name__ == "__main__":
    # Test initialization
    m = Matrix(3, 3)
    print("Initial matrix:", m.matrix)

    # Test set and get methods
    m.set(5, 1, 1)
    print("Set value at (1,1) to 5:", m.get(1, 1))

    # Test transpose method
    m.set(1, 0, 1)
    m.set(2, 1, 0)
    m.set(3, 2, 2)
    print("Matrix before transpose:", m.matrix)
    print("Transposed matrix:", m.transpose())

    # Test dot_product method
    m2 = Matrix(3, 3)
    m2.set(1, 0, 0)
    m2.set(2, 1, 1)
    m2.set(3, 2, 2)
    print("Matrix 1:", m.matrix)
    print("Matrix 2:", m2.matrix)
    print("Dot product:", m.dot_product(m2.matrix))

    # Test apply_fun method
    m.apply_fun(lambda x: x * 2)
    print("Matrix after applying function (x*2):", m.matrix)

