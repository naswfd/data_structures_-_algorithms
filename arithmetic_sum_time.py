import time


def sum_to_n(n):
    start = time.time()
    total = n * (n + 1) / 2
    end = time.time()
    return total, end - start


for i in range(5):
    print(sum_to_n(5))
