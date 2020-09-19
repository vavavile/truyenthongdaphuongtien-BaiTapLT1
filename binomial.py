import math

def binom(n, k):
    if n < k:
        return 0
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def prob(n, p, N):
    return (p**n)*((1-p)**(N-n))*binom(N, n)

def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))

def sumProb(n, p, N):
    """
    Khi n càng lớn thì hàm sumProb sẽ trả về giá trị tăng dần tới 1
    """
    z = 0
    for i in range(1, n + 1):
        z += prob(i, p, N)
    return z

def approxEntropy(n, p, N):
    """
    Khi n càng lớn thì hàm approxEntropy sẽ trả về giá trị tăng dần tới entropy
    """
    z = 0
    for i in range(1, n + 1):
        z += prob(i, p, N) * infoMeasure(i, p, N)
    return z

"""
Thực nghiệm hàm approxEntropy với giá trị p = 1/2
"""
print(approxEntropy(5, 0.5, 20))
print(approxEntropy(10, 0.5, 20))
print(approxEntropy(15, 0.5, 20))
print(approxEntropy(20, 0.5, 20))

