import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        result = 0
        while x:
            digit = int(math.fmod(x, 10))
            #if digit < 0: digit = digit * -1
            x = int(x / 10)

            if (result > MAX // 10 or
                (result == MAX // 10 and digit >= 7)):
                return 0
            
            if (result < MIN // 10 or
            (result == MIN // 10 and digit <= 8)):
                return 0

            result = (result * 10) + digit

        return result