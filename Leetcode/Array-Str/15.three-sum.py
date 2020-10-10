"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums: list) -> list:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        res = list()
        # 枚举a
        for first in range(n):
            if nums[first] > 0:
                break
            # 需要和上次枚举的数不同
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # c对应的指针初始指向数组右端
            third = n - 1
            target = -nums[first]
            # 枚举b
            for second in range(first+1, n):
                # 需要和上次枚举的数不同
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                # 需要保证b的指针在c指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着b增加就不会有满足a+b+c=0且b<c的c了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res


if __name__ == '__main__':
    ret = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print(ret)
