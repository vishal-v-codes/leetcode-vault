class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        negative = (dividend < 0) != (divisor < 0)

        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        while a >= b:
            temp = b
            count = 1
            while a >= temp + temp:
                temp += temp
                count += count
            a -= temp
            quotient += count
            
        return -quotient if negative else quotient