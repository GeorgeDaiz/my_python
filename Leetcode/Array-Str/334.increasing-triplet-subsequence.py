"""
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的i, j, k,且满足0 ≤ i < j < k ≤ n-1，
使得arr[i] < arr[j] < arr[k] ，返回 true ;否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:
输入: [1,2,3,4,5]
输出: true

示例 2:
输入: [5,4,3,2,1]
输出: false
"""


class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        if len(nums) < 3:
            return False
        res = False
        i = 1
        while i < len(nums) - 1:
            for left in range(0, i):
                if nums[left] < nums[i]:
                    res = True
            if res:
                for right in range(i+1, len(nums)):
                    if nums[right] > nums[i]:
                        return True
                res = False
            i += 1
        return res

    def increasingTriplet1(self, nums: list) -> bool:
        """
        用两个变量 r1, r2 分别记录第一小和第二小的数。然后遍历 nums。
        只要碰到比 r1 小的数我们就替换掉 r1，碰到比 r1 大但比 r2 小的数就替换 r2。
        只要碰到比 r2 大的数就已经满足题意了。\
        假如当前的 small 和 mid 为 [3, 5]，这时又来了个 1。假如我们不将 small 替换为 1，那么，当下一个数字是 2，后面再接上一个 3 的时候，
        我们就没有办法发现这个 [1,2,3] 的递增数组了！也就是说，我们替换最小值，是为了后续能够更好地更新中间值！
        另外，即使我们更新了 small ，这个 small 在 mid 后面，没有严格遵守递增顺序，但它隐含着的真相是，有一个比 small 大比 mid 小的前·
        最小值出现在 mid 之前。因此，当后续出现比 mid 大的值的时候，我们一样可以通过当前 small 和 mid 推断的确存在着长度为 3 的递增序列。 所以，这样的替换并不会干扰我们后续的计算！
        """
        n = len(nums)
        if n < 3:
            return False
        small, mid = float('inf'), float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False


if __name__ == '__main__':
    ret = Solution().increasingTriplet([1, 3, 2, 4])
    print(ret)
