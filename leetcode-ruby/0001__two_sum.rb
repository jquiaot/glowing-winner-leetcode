# 1. Two Sum
#
# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# - 2 <= nums.length <= 10^4
# - -10^9 <= nums[i] <= 10^9
# - -10^9 <= target <= 10^9
# - Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n^2)
# time complexity?

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  return two_sum_2(nums, target)
end

# Naive two-loop version.
#
# Time: O(n^2)
# Space: O(1)
#
def two_sum_1(nums, target)
  i = 0
  while i < nums.length do
    j = i + 1
    while j < nums.length do
      if nums[i] + nums[j] == target
        return [i, j]
      end
      j += 1
    end
    i += 1
  end
end

# Same as above, but using Ranges instead of incrementing indexs.
#
def two_sum_1_1(nums, target)
  for i in (0 .. nums.length - 1).to_a
    for j in ((i + 1) .. (nums.length - 1)).to_a
      if nums[i] + nums[j] == target
        return [i, j]
      end
    end
  end
end

# Map of nums[i] => i for all i in nums.
#
# Time: O(n) - at most once through nums
# Space: O(n) - at most storing a value for each num in nums
#
def two_sum_2(nums, target)
  diffs = {}
  for i in (0 .. nums.length - 1).to_a
    found = diffs[nums[i]]
    if found != nil
      return [i, found]
    end
    diffs[target - nums[i]] = i
  end
end
