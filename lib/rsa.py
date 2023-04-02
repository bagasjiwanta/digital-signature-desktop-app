import math, random, time

def generate_keys(p: int = 0, q: int = 0, length: int = 512):
    n = p * q
    totient_n = (p - 1) * (q - 1)
    return ()