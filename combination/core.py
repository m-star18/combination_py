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

    def C(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.factorials[n] * self.invs[r] % self.mod * self.invs[n - r] % self.mod
