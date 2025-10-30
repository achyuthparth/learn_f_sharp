# Chapter 1: Getting Started with F#

**Source**: The Haskell Road to Logic, Math and Programming - Chapter 1

## Learning Objectives
- Basic F# syntax and REPL usage
- Function definitions and recursion
- Pattern matching
- List operations
- Type inference

## Files
- `basics.fsx` - Basic F# syntax and functions
- `lists.fsx` - List operations and recursion
- `exercises.fsx` - Chapter 1 exercises converted from Haskell

## Running the Code
```bash
# Interactive F# REPL
dotnet fsi

# Load and run a script
dotnet fsi basics.fsx
```

## Key Conversions from Haskell to F#
- `::` (cons) → `::` (same in F#)
- `head`, `tail` → `List.head`, `List.tail`
- Pattern matching syntax is very similar
- Function composition `(.)` → `(>>)` or `(<<)`
