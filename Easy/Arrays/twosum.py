# [2,7,11,15], target = 9
# 2, 9 - 2 = 7. store index. ok, now go to next
# 7 - 7 = 0. store index. check and return index array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the things already seen
        # iterate through the array,
        # checking things already seen + current thing to see if = target

        seen_values = {}
        i = 0
        while i < len(nums):
            number = nums[i]
            number_needed = target - number
            if number_needed in seen_values:
                return [i, seen_values[number_needed]]
            seen_values[number] = i
            i += 1
