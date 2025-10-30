// The Haskell Road - Chapter 1: List Operations in F#
// Converted from Haskell list examples

// Basic list operations
let numbers = [1; 2; 3; 4; 5]
let empty_list = []

// List construction
let cons_example = 0 :: numbers  // [0; 1; 2; 3; 4; 5]

// Head and tail (with safety)
let safe_head lst =
    match lst with
    | [] -> None
    | h :: _ -> Some h

let safe_tail lst =
    match lst with
    | [] -> None
    | _ :: t -> Some t

// Length function (recursive)
let rec length lst =
    match lst with
    | [] -> 0
    | _ :: tail -> 1 + length tail

// Sum function
let rec sum lst =
    match lst with
    | [] -> 0
    | head :: tail -> head + sum tail

// Append function
let rec append lst1 lst2 =
    match lst1 with
    | [] -> lst2
    | head :: tail -> head :: append tail lst2

// Reverse function
let rec reverse lst =
    match lst with
    | [] -> []
    | head :: tail -> append (reverse tail) [head]

// More efficient reverse using accumulator
let reverse_acc lst =
    let rec rev_helper acc = function
        | [] -> acc
        | head :: tail -> rev_helper (head :: acc) tail
    rev_helper [] lst

// Test the functions
printfn "numbers = %A" numbers
printfn "cons_example = %A" cons_example
printfn "length numbers = %d" (length numbers)
printfn "sum numbers = %d" (sum numbers)
printfn "reverse numbers = %A" (reverse numbers)
printfn "reverse_acc numbers = %A" (reverse_acc numbers)

// Using built-in F# List functions for comparison
printfn "\nUsing F# List module:"
printfn "List.length numbers = %d" (List.length numbers)
printfn "List.sum numbers = %d" (List.sum numbers)
printfn "List.rev numbers = %A" (List.rev numbers)
