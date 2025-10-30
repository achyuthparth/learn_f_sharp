"""
Contemporary Abstract Algebra - Chapter 1: Number Theory Algorithms
Python implementations for computational exploration
"""

import math
from typing import List, Tuple, Optional

def gcd(a: int, b: int) -> int:
    """Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return abs(a)

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean algorithm: returns (gcd, x, y) where ax + by = gcd(a,b)"""
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y

def lcm(a: int, b: int) -> int:
    """Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

def mod_inverse(a: int, n: int) -> Optional[int]:
    """Modular inverse of a modulo n, if it exists"""
    g, x, _ = extended_gcd(a, n)
    if g == 1:
        return x % n
    return None

def is_prime(n: int) -> bool:
    """Simple primality test"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Generate all primes up to limit using Sieve of Eratosthenes"""
    if limit < 2:
        return []
    
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_arr[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_arr[j] = False
    
    return [i for i in range(2, limit + 1) if is_prime_arr[i]]

def factorize(n: int) -> List[Tuple[int, int]]:
    """Prime factorization: returns list of (prime, exponent) pairs"""
    if n <= 1:
        return []
    
    factors = []
    d = 2
    
    while d * d <= n:
        exp = 0
        while n % d == 0:
            n //= d
            exp += 1
        if exp > 0:
            factors.append((d, exp))
        d += 1
    
    if n > 1:
        factors.append((n, 1))
    
    return factors

def euler_phi(n: int) -> int:
    """Euler's totient function - count of integers ≤ n that are coprime to n"""
    if n == 1:
        return 1
    
    factors = factorize(n)
    result = n
    
    for prime, _ in factors:
        result = result * (prime - 1) // prime
    
    return result

# Testing the implementations
if __name__ == "__main__":
    print("=== Number Theory Algorithm Tests ===")
    
    # GCD and LCM tests
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"lcm(48, 18) = {lcm(48, 18)}")
    
    # Extended GCD test
    g, x, y = extended_gcd(48, 18)
    print(f"Extended GCD: {g} = 48*{x} + 18*{y}")
    print(f"Verification: 48*{x} + 18*{y} = {48*x + 18*y}")
    
    # Modular inverse tests
    inv = mod_inverse(7, 12)
    print(f"7^(-1) mod 12 = {inv}")
    
    inv = mod_inverse(5, 12)
    print(f"5^(-1) mod 12 = {inv}")
    
    # Prime testing
    test_numbers = [17, 25, 29, 35, 37]
    print(f"\nPrimality tests: {[(n, is_prime(n)) for n in test_numbers]}")
    
    # Prime generation
    primes = sieve_of_eratosthenes(30)
    print(f"Primes up to 30: {primes}")
    
    # Factorization
    test_factor = 60
    factors = factorize(test_factor)
    print(f"Prime factorization of {test_factor}: {factors}")
    
    # Euler's totient function
    for n in [1, 6, 9, 10, 12]:
        print(f"φ({n}) = {euler_phi(n)}")
