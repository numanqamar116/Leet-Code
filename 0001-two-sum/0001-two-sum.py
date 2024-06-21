class Solution(object):
    def twoSum(self,nums,target):
        length=len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]+nums[j]==target:
                    return [i,j]
if __name__ == "__main__":
    solution=Solution()
    print(solution.twoSum([1,2,3,4],5)) 