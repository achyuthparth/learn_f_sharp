// Category Theory for Programmers - Chapter 1: Composition in F#
// Converted from Haskell examples

// Identity function
let id x = x

// Basic functions for composition examples
let increment x = x + 1
let double x = x * 2
let square x = x * x

// Function composition using >> (left-to-right)
let incrementThenDouble = increment >> double
let doubleThenSquare = double >> square
let incrementThenDoubleThenSquare = increment >> double >> square

// Function composition using << (right-to-left, like Haskell's .)
let doubleComposeIncrement = double << increment
let squareComposeDouble = square << double

// Demonstrating associativity: (f ∘ g) ∘ h = f ∘ (g ∘ h)
let leftAssoc = (square << double) << increment
let rightAssoc = square << (double << increment)

// Test associativity
let testValue = 3
printfn "Testing associativity with value %d:" testValue
printfn "leftAssoc %d = %d" testValue (leftAssoc testValue)
printfn "rightAssoc %d = %d" testValue (rightAssoc testValue)
printfn "Are they equal? %b" (leftAssoc testValue = rightAssoc testValue)

// Identity laws: f ∘ id = f and id ∘ f = f
let f = increment
let leftIdentity = f << id
let rightIdentity = id << f

printfn "\nTesting identity laws with value %d:" testValue
printfn "f %d = %d" testValue (f testValue)
printfn "leftIdentity %d = %d" testValue (leftIdentity testValue)
printfn "rightIdentity %d = %d" testValue (rightIdentity testValue)

// More complex composition example
let pipeline = 
    List.map increment 
    >> List.filter (fun x -> x % 2 = 0)
    >> List.map square
    >> List.sum

let numbers = [1; 2; 3; 4; 5]
printfn "\nPipeline example:"
printfn "Input: %A" numbers
printfn "Result: %d" (pipeline numbers)
