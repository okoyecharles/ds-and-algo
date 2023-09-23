# Math Helper Functions

# returns the prime factors of a number (sorted)
def factors(num):
        if num == 1: return [1]

        divisors = []
        divisor = 2

        while num != 1:
                if num % divisor == 0:
                        divisors.append(divisor)
                        num = num / divisor
                else:
                        divisor = divisor + 1

        return divisors
