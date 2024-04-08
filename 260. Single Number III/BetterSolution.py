class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        number = 0
        for num in nums:
            number ^= num
        set_bit = 1
        while True:
            if number & set_bit:
                break        
            set_bit <<= 1

        first_answer = 0
        for num in nums:
            if num & set_bit:
                first_answer ^= num
        
        second_answer = number ^ first_answer
        return [first_answer, second_answer]
        
