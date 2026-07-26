# Simpson's 1/3 Rule

def f(x):
    return x**2  # Example function

# Input
a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter number of intervals (even): "))

# Check if n is even
if n % 2 != 0:
    print("Number of intervals must be even.")
else:
    h = (b - a) / n

    s = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)

    result = (h / 3) * s

    print("Approximate value of the integral =", result)

OUTPUt is
Enter lower limit (a): 0
Enter upper limit (b): 2
Enter even number of subintervals (n): 4

Approximate value of the integral = 2.6666666666666665
