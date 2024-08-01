def generate_fibonacci_up_to_1000():
    a, b = 0, 1
    fib_list = []
    while b <= 1000:
        fib_list.append(b)
        a, b = b, a + b
    return fib_list

print(generate_fibonacci_up_to_1000())
