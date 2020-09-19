import math

def prob(n, p):
    return (1-p)**(n-1)*p

def infoMeasure(n, p):
    return -math.log2(prob(n, p))

def sumProb(n, p):
    """
    Khi n càng lớn thì hàm sumProb sẽ trả về giá trị tăng dần tới 1
    """
    z = 0
    for i in range(1, n + 1):
        z += prob(i, p)
    return z

def approxEntropy(n, p):
    """
    Khi n càng lớn thì hàm approxEntropy sẽ trả về giá trị tăng dần tới entropy
    """
    z = 0
    for i in range(1, n + 1):
        z += prob(i, p) * infoMeasure(i, p)
    return z

"""
Thực nghiệm hàm approxEntropy với giá trị p = 1/2, kết quả tiến tới 2 khi n tăng
"""
print(approxEntropy(5, 0.5))
print(approxEntropy(10, 0.5))
print(approxEntropy(15, 0.5))
print(approxEntropy(20, 0.5))
print(approxEntropy(25, 0.5))
print(approxEntropy(30, 0.5))

