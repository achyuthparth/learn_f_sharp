// Contemporary Abstract Algebra - Chapter 1: Integers in F#
// Modular arithmetic and integer operations

// Modular arithmetic operations
module ModularArithmetic =
    
    // Safe modulo operation (always positive result)
    let modulo a n = ((a % n) + n) % n
    
    // Modular addition
    let addMod a b n = modulo (a + b) n
    
    // Modular multiplication  
    let mulMod a b n = modulo (a * b) n
    
    // Modular exponentiation (fast)
    let rec powMod baseNum exp modulus =
        if exp = 0 then 1
        elif exp % 2 = 0 then
            let half = powMod baseNum (exp / 2) modulus
            mulMod half half modulus
        else
            mulMod baseNum (powMod baseNum (exp - 1) modulus) modulus

// Greatest Common Divisor using Euclidean algorithm
let rec gcd a b =
    if b = 0 then abs a
    else gcd b (a % b)

// Extended Euclidean algorithm: returns (gcd, x, y) where ax + by = gcd(a,b)
let extendedGcd a b =
    let rec extGcdRec a b x0 x1 y0 y1 =
        if b = 0 then (a, x0, y0)
        else
            let q = a / b
            extGcdRec b (a % b) x1 (x0 - q * x1) y1 (y0 - q * y1)
    extGcdRec a b 1 0 0 1

// Least Common Multiple
let lcm a b = abs (a * b) / gcd a b

// Modular inverse (if it exists)
let modInverse a n =
    let (g, x, _) = extendedGcd a n
    if g = 1 then Some (ModularArithmetic.modulo x n)
    else None

// Test the implementations
printfn "=== Modular Arithmetic Tests ==="
printfn "7 + 9 ≡ %d (mod 5)" (ModularArithmetic.addMod 7 9 5)
printfn "7 * 9 ≡ %d (mod 5)" (ModularArithmetic.mulMod 7 9 5)
printfn "2^10 ≡ %d (mod 7)" (ModularArithmetic.powMod 2 10 7)

printfn "\n=== GCD/LCM Tests ==="
printfn "gcd(48, 18) = %d" (gcd 48 18)
printfn "lcm(48, 18) = %d" (lcm 48 18)

let (g, x, y) = extendedGcd 48 18
printfn "Extended GCD: %d = 48*%d + 18*%d" g x y

printfn "\n=== Modular Inverse Tests ==="
match modInverse 7 12 with
| Some inv -> printfn "7^(-1) ≡ %d (mod 12)" inv
| None -> printfn "7 has no inverse mod 12"

match modInverse 5 12 with  
| Some inv -> printfn "5^(-1) ≡ %d (mod 12)" inv
| None -> printfn "5 has no inverse mod 12"
