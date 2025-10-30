"""
Category Theory for Programmers - Chapter 1: Challenges
Converted from C++ examples to Python
"""

def identity(x):
    """Identity function - returns its argument unchanged"""
    return x

def compose(f, g):
    """Function composition: returns a function that applies g then f"""
    return lambda x: f(g(x))

def increment(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x * x

# Challenge 1: Implement identity function
print("Challenge 1: Identity function")
test_val = 42
print(f"identity({test_val}) = {identity(test_val)}")

# Challenge 2: Implement composition function
print("\nChallenge 2: Function composition")
inc_then_double = compose(double, increment)
double_then_square = compose(square, double)

print(f"increment then double: {inc_then_double(3)}")  # (3+1)*2 = 8
print(f"double then square: {double_then_square(3)}")  # (3*2)^2 = 36

# Challenge 3: Test associativity
print("\nChallenge 3: Associativity test")
# (square ∘ double) ∘ increment vs square ∘ (double ∘ increment)
left_assoc = compose(compose(square, double), increment)
right_assoc = compose(square, compose(double, increment))

test_val = 5
left_result = left_assoc(test_val)
right_result = right_assoc(test_val)

print(f"Left associative: {left_result}")
print(f"Right associative: {right_result}")
print(f"Associativity holds: {left_result == right_result}")

# Challenge 4: Test identity laws
print("\nChallenge 4: Identity laws")
f = increment

# f ∘ id = f
left_identity = compose(f, identity)
# id ∘ f = f  
right_identity = compose(identity, f)

test_val = 10
original = f(test_val)
left_id_result = left_identity(test_val)
right_id_result = right_identity(test_val)

print(f"f({test_val}) = {original}")
print(f"(f ∘ id)({test_val}) = {left_id_result}")
print(f"(id ∘ f)({test_val}) = {right_id_result}")
print(f"Left identity law holds: {original == left_id_result}")
print(f"Right identity law holds: {original == right_id_result}")

# Bonus: Chain multiple compositions
print("\nBonus: Multiple compositions")
complex_function = compose(compose(square, double), increment)
print(f"((x+1)*2)^2 where x=3: {complex_function(3)}")  # ((3+1)*2)^2 = 64
