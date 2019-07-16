def gcd(m, n):
    while True:
        if m < n:
            m, n = n, m
        r = m % n
        if r == 0:
            return n
        else:
            m, n = n, r

if __name__ == "__main__":
    print(gcd(119, 544))