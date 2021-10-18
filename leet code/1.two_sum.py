# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        my_dict = {}
        for i, num in enumerate(nums):
            print(i , num)
            my_num = target - nums[i]
            if my_num in my_dict: 
                return [my_dict[my_num], i]
            else: my_dict[nums[i]] = i
        return []
        
def main():
    my_solution = Solution()
    print(my_solution.twoSum([-3,4,3,90], 0))

main()