# Chapter 1: Composition

**Source**: Category Theory for Programmers - Chapter 1

## Learning Objectives
- Function composition in F#
- Identity functions
- Associativity of composition
- Programming challenges in F# and Python

## Files
- `composition.fsx` - F# function composition examples
- `challenges.py` - Python implementations of computational challenges
- `identity.fsx` - Identity function examples

## Key Concepts
- **Composition**: Combining functions to create new functions
- **Identity**: Functions that return their input unchanged
- **Associativity**: `(f ∘ g) ∘ h = f ∘ (g ∘ h)`

## Haskell to F# Conversions
- `(.)` → `(>>)` for left-to-right composition
- `id` → `id` (same function name)
- Function types: `a -> b` → `'a -> 'b`
