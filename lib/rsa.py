import math, random, time


first_primes_list = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103,
    107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179,
    181, 191, 193, 197, 199, 211, 223,
    227, 229, 233, 239, 241, 251, 257,
    263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349
]
'''prime awal yang akan ditest untuk pembagian'''
 

def get_shallow_tested_prime(n: int) -> int:
    '''tes kandidat prima dengan first_prime_list'''

    while True:
        prime_candidate = generate_large_n_size_number(n)
        for prime_divisor in first_primes_list:
            divisable = prime_candidate % prime_divisor == 0
            if divisable:
                break
        return prime_candidate


def generate_large_n_size_number(n: int) -> int:
    '''menghasilkan random number diantara (2^n-1 + 2^n-2) dan 2^n'''

    upper_bound = (2**n)
    lower_bound = 2**(n-1) + 2**(n-2) + 1 # 3/4 dari upper bound
    step = 2 # skip angka genap
    return random.randrange(lower_bound, upper_bound, step)


def generate_rsa_keys(p: int, q: int, length: int = 256):
    '''menghasilkan key rsa (n, e, d) dari bilangan prima p dan q. d dan e besarnya length bit'''

    n = p * q
    totient_n = (p - 1) * (q - 1)
    
    return ()