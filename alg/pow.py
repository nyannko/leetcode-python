class Solution(object):

    def check_pow_loop(self, base, exp):
        if exp < 0:
            return 1 / self.pow_loop(base, -exp)
        else:
            return self.pow_loop(base, exp)

    def pow_loop(self, base, exp):
        result = 1
        for i in range(exp):
            result *= base
        return result

    def check_recursive(self, base, exp):
        if exp < 0:
            return 1 / self.recursive(base, -exp)
        else:
            return self.recursive(base, exp)

    def recursive(self, base, exp):
        if exp == 0:
            return 1
        else:
            return base * self.recursive(base, exp - 1)

    def check_power_recursive(self, base, exp):
        if exp < 0:
            return 1 / self.power(base, -exp)
        else:
            return self.power(base, exp)

    def power(self, base, exp):
        if exp == 0:
            return 1

        if exp == 1:
            return base

        v = self.power(base, exp >> 1)
        res = v * v
        if exp & 1 == 1:
            res = v * v * base
        return res

    def check_power_recorsive2(self, base, exp):
        if exp < 0:
            return 1 / self.power2(base, -exp)
        else:
            return self.power2(base, exp)

    def power2(self, base, exp):
        if exp == 0:
            return 1

        if exp == 1:
            return base

        # long number in python3 maximum recursion depth exceeded in comparison
        v = self.power2(base, exp // 2)
        if exp % 2 == 0:
            return v * v
        else:
            return v * v * base
