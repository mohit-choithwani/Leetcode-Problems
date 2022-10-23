#For all the indecies in the list
# Calculate sum of all elements on the left and sum of all the elements on the right
# If left sum == right sum, then return index else return -1
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        total = 0
        for i in range(n):
            #print(nums[i])
            total = total + nums[i]
            
        for i in range(n):
            leftsum = self.LeftSum(nums, i)
            rightsum = self.RightSum(nums, i)
            # print('leftsum-->{}'.format(leftsum))
            # print('righttsum-->{}'.format(rightsum))
            
            if leftsum == rightsum:
                return i
            
            # if leftsum == (total - nums[i] - leftsum):
            #     return i
            
        return -1
    #Helper to calculate sum of all elements on the left
    def LeftSum(self, nums, j):
        n = len(nums)
        if j == 0:
            return 0
        else:
            sum = 0
            for i in range(j):
                sum = sum + nums[i]
            return sum

    #Helper to calculate sum of all elements on the right
    def RightSum(self, nums, j):
        n = len(nums)
        if j == (n-1):
            return 0
        else:
            sum = 0
            for i in range(j+1, n):
                sum = sum + nums[i]
            return sum
        
