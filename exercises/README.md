# Programming Exercises from Mathematical Textbooks

This directory contains programming exercises and implementations from three mathematical textbooks, converted to F# and Python as appropriate.

## 📚 Textbook Sources

### The Haskell Road to Logic, Math and Programming
**Conversion**: Haskell → F#  
**Focus**: Functional programming, logic, mathematical reasoning  
**Directories**: `haskell-road/ch01-getting-started/`, `haskell-road/ch02-mathematical-objects/`, etc.

### Category Theory for Programmers  
**Conversion**: Haskell → F#, C++ → Python  
**Focus**: Category theory concepts through programming  
**Directories**: `category-theory/ch01-composition/`, `category-theory/ch02-types-functions/`, etc.

### Contemporary Abstract Algebra
**Conversion**: Mathematical concepts → F# and Python implementations  
**Focus**: Algebraic structures, computational algebra  
**Directories**: `abstract-algebra/ch01-integers/`, `abstract-algebra/ch02-groups/`, etc.

## 🎯 Conversion Strategy

| Source Language | Target Language | Rationale |
|-----------------|----------------|-----------|
| Haskell | F# | Similar functional paradigms, strong type systems |
| C++ | Python | Computational exercises benefit from Python's expressiveness |
| Mathematical concepts | F# + Python | F# for type safety, Python for algorithms |

## 🚀 Getting Started

### Prerequisites
- **.NET SDK** (for F# scripts)
- **Python 3.x** (for computational exercises)
- **VS Code** (recommended editor)

### Running Examples
```bash
# F# scripts
dotnet fsi script.fsx

# Python files  
python script.py
```

## 📁 Structure

Each chapter directory contains:
- `README.md` - Chapter overview and learning objectives
- `*.fsx` - F# script files (converted from Haskell)
- `*.py` - Python files (converted from C++, or computational algorithms)
- Comments linking back to original textbook sections

## 🎓 Learning Approach

1. **Read the textbook chapters first** - these implementations are companions, not replacements
2. **Run the code** - see the concepts in action
3. **Modify and experiment** - change parameters, try edge cases
4. **Extend the implementations** - add your own functions and tests

The goal is to make abstract mathematical concepts concrete through executable code.
