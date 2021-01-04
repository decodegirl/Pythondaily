class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(num):
            result = 0
            while num > 0:
                rem = num % 10
                result = result + rem * rem
                num = num // 10
            return result
        
        seen = set()
        while square_sum(n)  not in seen:
            sum_one = square_sum(n)
            if sum_one == 1:
                return True
            else:
                seen.add(sum_one)
                n = sum_one
        return False
  

