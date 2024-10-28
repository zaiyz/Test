"""
2024. 10. 28
이지느히
utils.py
코딩연습
"""


def factorial(x) :
    if x == 1 :
        return 1
    return x * factorial(x-1)


def ggd(x):
    for i in range(9) :
        print ((i+1) * x)

def hanoi(n, f, t, via):
    if n == 1:
        print(str(f) + "->" + str(t))
    else:
        hanoi(n - 1, f, via, t)
        print(str(f) + "->" + str(t))
        hanoi(n - 1, via, t, f)
