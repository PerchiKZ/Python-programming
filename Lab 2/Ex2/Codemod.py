def calculate_product(n):
    result = 1
    for i in range(1, n + 1):
        result *= 2 * i
    return result
