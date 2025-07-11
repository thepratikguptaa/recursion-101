class Solution:
    MOD = 10**9 + 7

    @staticmethod
    def power(x, n, mod):
        if n == 0:
            return 1
        half = Solution.power(x, n//2, mod)
        result = (half * half) % mod
        if n % 2 == 1:
            result = (result * x) % mod
        return result

    def countGoodNumbers(self, n: int) -> int:
        even_count = (n+1) // 2
        odd_count = n // 2

        return (self.power(5, even_count, self.MOD) * self.power(4, odd_count, self.MOD)) % self.MOD