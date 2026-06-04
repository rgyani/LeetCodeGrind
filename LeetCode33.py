"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Intuition: if the array was sorted but not rotated, we could have 2 pointers i and j, and keep comparing middle and switching i or j with middle to reach the target

Consider [0, 1, 2, 4, 5, 6, 7]
c = l+ (h-l)//2,    l,h,c = 0, 6, 3,
since s[c] < target l,h,c = 0, 3, 2
since s[c] < target l,h,c = 0, 2, 1,
since s[c] < target l,h,c = 0, 1, 1
since s[c] < target l,h,c = 0, 0, 0 <- we found the target


Consider [4,5,6,7,0,1,2], target = 0
c = l+ (h-l)//2,    l,h,c = 0, 6, 3
if we were using standard binary search, we wud hv seems target < s]3] and moved left
but that is obviously wrong, so we ask
1. is the left array sorted -> YES
2. AND is the target between l and c -> NO
so the target must be in right, and we can do the same search as above there

Consider [6,7,0,1,2,4,5], target = 0
c = l+ (h-l)//2,    l,h,c = 0, 6, 3
1. is the left array sorted -> NO, that means right must be sorted
2. AND is the target between c and r -> NO
so that target must be in left and we can do the same search as above there

So the rule is
Is the Zone Sorted
  Target is inside Zone -> search this zone
                    else-> search other zone

"""


def search(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    l, r = 0, len(nums) - 1
    while l <= r:
        c = l + (r- l) // 2

        if nums[c] == target:
            return c

        if nums[l] <= nums[c]:
            # if target is between l and c
            if nums[l] <= target < nums[c]:
                r = c - 1 # do left
            else:
                l = c + 1 # do right
        else:
            # if target is between c and r
            if nums[c] < target <= nums[r]:
                l = c + 1 # do right
            else:
                r = c - 1 # do left

    return -1


if __name__ == "__main__":
    assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert search(nums=[1], target=0) == -1
    assert search(nums=[5,1,3], target=3) == 2
