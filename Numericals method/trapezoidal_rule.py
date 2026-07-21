# ==========================================
# Numerical Integration using Trapezoidal Rule
# ==========================================

def f(x):
    return x**2 + 2*x + 1

# Input
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter number of intervals (n): "))

h = (b - a) / n

result = f(a) + f(b)

print("\nIteration Table")
print("-" * 35)
print("i\t x\t\t f(x)")
print("-" * 35)

for i in range(n + 1):
    x = a + i * h
    print(f"{i}\t{x:.2f}\t\t{f(x):.2f}")

for i in range(1, n):
    x = a + i * h
    result += 2 * f(x)

integral = (h / 2) * result

print("-" * 35)
print(f"Step Size (h) = {h:.4f}")
print(f"Approximate Integral = {integral:.4f}")
print("-" * 35)

OUTPUT is
Enter lower limit (a): 0
Enter upper limit (b): 4
Enter number of intervals (n): 4

Iteration Table
-----------------------------------
i       x               f(x)
-----------------------------------
0       0.00            1.00
1       1.00            4.00
2       2.00            9.00
3       3.00            16.00
4       4.00            25.00
-----------------------------------
Step Size (h) = 1.0000
Approximate Integral = 42.0000
-----------------------------------
