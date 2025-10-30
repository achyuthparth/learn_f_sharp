// The Haskell Road - Chapter 1: Basic F# Functions
// Converted from Haskell examples

// Simple arithmetic functions
let square x = x * x
let double x = 2 * x

// Factorial function (recursive)
let rec factorial n =
    if n <= 1 then 1
    else n * factorial (n - 1)

// Maximum of two numbers
let max2 (x: int) (y: int) = if x >= y then x else y

// Maximum of three numbers
let max3 x y z = max2 (max2 x y) z

// Test the functions
printfn "square 5 = %d" (square 5)
printfn "double 7 = %d" (double 7)
printfn "factorial 5 = %d" (factorial 5)
printfn "max3 10 5 8 = %d" (max3 10 5 8)

// Function composition examples
let squareAndDouble = square >> double
let doubleAndSquare = double >> square

printfn "squareAndDouble 3 = %d" (squareAndDouble 3)  // (3^2) * 2 = 18
printfn "doubleAndSquare 3 = %d" (doubleAndSquare 3)  // (3*2)^2 = 36
