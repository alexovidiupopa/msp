from z3 import *

# Define integer variables for positions
A = Int('A')  # Alice
B = Int('B')  # Bob
C = Int('C')  # Charlie

# Possible positions: 0 (left), 1 (middle), 2 (right)
positions = [A, B, C]

# Create a solver instance
solver = Solver()

# Each person must be in a distinct chair
solver.add(Distinct(A, B, C))

# Alice does not sit next to Charlie
solver.add(Abs(A - C) != 1)

# Alice does not sit on the leftmost chair
solver.add(A != 0)

# Bob does not sit to the right of Charlie
solver.add(B <= C)

# Valid chair positions
for p in positions:
    solver.add(p >= 0, p <= 2)

# Check for a solution
if solver.check() == sat:
    model = solver.model()
    print(f"Alice: {model[A]}, Bob: {model[B]}, Charlie: {model[C]}")
else:
    print("Unsat")
