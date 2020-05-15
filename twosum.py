#Given an array of integers, return indices of two numbers that add to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#For example:
#Given nums = [2, 8, 12, 15], target = 20,
#Because nums [1] + nums [2] = 8 + 12= 20,
#return [1,2]

#Brute Force solution

def two_sum(nums,target):
    if not nums:
        return None
    else:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
# print(two_sum([],14))

#hashtable

def two_sum(nums,target):
    if not nums:
        return None
    else:
        hash_map = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in hash_map:
                return [ hash_map[complement],i]
            else:
                hash_map[n] = i

print(two_sum([],31))




