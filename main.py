def twoSum(self, nums: List[int], target: int) -> List[int]:

    a = b = 0

    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
           if (nums[i]+nums[j] == target):
               return (i,j)
    return (0,0)
