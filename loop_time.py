import time


def sum_to_n(n):
    start = time.time()
    total = 0
    for i in range(1, n + 1):
        total += i
    end = time.time()

    return total, end - start


for i in range(5):
    print(sum_to_n(5))
