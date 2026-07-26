# Bisection Method in Python

def f(x):
    return x**3 - x - 2

a = 1
b = 2
tol = 0.0001

if f(a) * f(b) >= 0:
    print("Invalid Interval")
else:
    step = 1

    while (b - a) >= tol:
        c = (a + b) / 2

        print(f"Step {step}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {f(c):.4f}")

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        step += 1

    print("\nApproximate Root =", round(c, 4))

OUTPUT is
Step 1: a = 1.0000, b = 2.0000, c = 1.5000, f(c) = -0.1250
Step 2: a = 1.5000, b = 2.0000, c = 1.7500, f(c) = 1.6094
Step 3: a = 1.5000, b = 1.7500, c = 1.6250, f(c) = 0.6660
Step 4: a = 1.5000, b = 1.6250, c = 1.5625, f(c) = 0.2522
Step 5: a = 1.5000, b = 1.5625, c = 1.5312, f(c) = 0.0591
Step 6: a = 1.5000, b = 1.5312, c = 1.5156, f(c) = -0.0341
Step 7: a = 1.5156, b = 1.5312, c = 1.5234, f(c) = 0.0123
Step 8: a = 1.5156, b = 1.5234, c = 1.5195, f(c) = -0.0109
Step 9: a = 1.5195, b = 1.5234, c = 1.5215, f(c) = 0.0006
Step 10: a = 1.5195, b = 1.5215, c = 1.5205, f(c) = -0.0052
...

Approximate Root = 1.5214
