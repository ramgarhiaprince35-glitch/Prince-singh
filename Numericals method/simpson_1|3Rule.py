# Simpson's 1/3 Rule

def f(x):
    return x**2  # Example function: f(x) = x^2

a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))
n = int(input("Enter even number of subintervals (n): "))

if n % 2 != 0:
    print("Error: Number of subintervals must be even.")
else:
    h = (b - a) / n

    sum_odd = 0
    sum_even = 0

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum_even += f(x)
        else:
            sum_odd += f(x)

    result = (h / 3) * (f(a) + f(b) + 4 * sum_odd + 2 * sum_even)

    print("Approximate value of the integral =", result)


OUTPUt is
Enter lower limit (a): 0
Enter upper limit (b): 2
Enter even number of subintervals (n): 4

Approximate value of the integral = 2.6666666666666665
