class Combination:

    def __init__(self, n_max, mod=10**9+7):
        # O(n_max + log(mod))
        f = 1
        self.mod = mod
        self.factorials = factorials = [f]
        for i in range(1, n_max + 1):
            f *= i % mod
            factorials.append(f)
        f = pow(f, mod - 2, mod)
        self.invs = invs = [f]
        for i in range(n_max, 0, -1):
            f *= i % mod
            invs.append(f)
        invs.reverse()

    def nCr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.factorials[n] * self.invs[r] % self.mod * self.invs[n - r] % self.mod

    def nPr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.factorials[n] * self.invs[n - r] % self.mod

    def nHr(self, n, r):
        if (n == 0 and r > 0) or r < 0:
            return 0
        return self.factorials[n + r - 1] * self.invs[r] % self.mod * self.invs[n - 1] % self.mod

    def rising_factorial(self, n, r):
        return self.factorials[n + r - 1] * self.invs[n - 1] % self.mod
