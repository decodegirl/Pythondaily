def threeSum( nums):
        res = []
        nums.sort()
        
        # i denote the first number
        for i in range(len(nums) - 1):
            # if i has been searched before, skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # if the first number > 0, 3Sum cant be zero, break
            if nums[i] > 0:
                break
            
            # this is how we solve 2Sum problem
            d = {}
            j = i + 1
            while j < len(nums):
                # nums[i] + nums[j] + req = 0
                # i < index of req < j
                req = -nums[i] - nums[j]

                # some num scanned before meet the requirement
                if req in d:
                    res.append([nums[i], req, nums[j]])
                    # skip duplication of nums[j]
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j = j + 1
                # restore req -> index in dict
                else:
                    d[nums[j]] = j
                j += 1
            
        return res