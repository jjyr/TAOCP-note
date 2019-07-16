def euclid_common_divisor(m, n):
    while True:
        if m < n:
            m, n = n, m
        r = m % n
        if r == 0:
            return n
        else:
            m, n = n, r

if __name__ == "__main__":
    print(euclid_common_divisor(119, 544))