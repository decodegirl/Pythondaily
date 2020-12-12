class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left= 0 #initialize to 0
        curr = 0 
        right = len(nums)-1 #last digit in the array
        
        while curr <= right:
            if nums[curr] == 0:
                nums[left],nums[curr]= nums[curr],nums[left] #swap, the current with the left
                left += 1 #increment the left
                curr += 1  #increment the current
                
            elif nums[curr] == 2:
                nums[curr],nums[right]  = nums[right],nums[curr] #swap the current with the right
                right -= 1 #decrement the right
                
            else:
                curr += 1 #otherwise we just increment the current
        