"""
2024. 10. 26
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