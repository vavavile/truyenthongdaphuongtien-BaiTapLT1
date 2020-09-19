import math

def binom(n, k):
    if n < k:
        return 0
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def prob(n, p, N, r):
    return (p**r)*((1-p)**(n-r))*binom(n - 1, r - 1)

def infoMeasure(n, p, N, r):
    return -math.log2(prob(n, p, N, r))

def sumProb(n, p, N, r):
    """
    Khi n càng lớn thì hàm sumProb sẽ trả về giá trị tăng dần tới 1
    """
    z = 0
    for i in range(r, n + 1):
        z += prob(i, p, N, r)
    return z

def approxEntropy(n, p, N, r):
    """
    Khi n càng lớn thì hàm approxEntropy sẽ trả về giá trị tăng dần tới entropy
    """
    z = 0
    for i in range(r, n + 1):
        z += prob(i, p, N, r) * infoMeasure(i, p, N, r)
    return z

"""
Thực nghiệm hàm approxEntropy với giá trị p = 1/2
"""
print(approxEntropy(5, 0.5, 0, 5))
print(approxEntropy(10, 0.5, 0, 5))
print(approxEntropy(15, 0.5, 0, 5))
print(approxEntropy(20, 0.5, 0, 5))
print(approxEntropy(25, 0.5, 0, 5))
print(approxEntropy(30, 0.5, 0, 5))

