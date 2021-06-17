"""
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组counts。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于nums[i] 的元素的数量。

示例：
输入：nums = [5,2,6,1]
输出：[2,1,1,0]

解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

提示：
0 <= nums.length <= 10^5
-10^4<= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class BinaryIndexedTree:
    def __init__(self, length):
        self.c = [0] * length

    def low_bit(self, x):
        return x & (-x)

    def update(self, pos, value=1):
        while pos < len(self.c):
            self.c[pos] += value
            pos += self.low_bit(pos)

    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.low_bit(pos)
        return ans


class Solution:
    # 归并排序
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        res = [0] * len(nums)
        for idx, num in enumerate(nums):
            arr.append((idx, num))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(l, r):
            tmp = []
            i, j = 0, 0
            while i < len(l) or j < len(r):
                if j == len(r) or i < len(l) and l[i][1] <= r[j][1]:
                    tmp.append(l[i])
                    res[l[i][0]] += j
                    i += 1
                else:
                    tmp.append(r[j])
                    j += 1

            return tmp

        merge_sort(arr)
        return res

    # 树状数组
    def discretization(self, nums):
        a = sorted(set(nums))
        value2id = {v: i + 1 for i, v in enumerate(a)}
        return value2id, len(a)

    def countSmaller1(self, nums: List[int]) -> List[int]:
        value2id, length = self.discretization(nums)
        bit = BinaryIndexedTree(length + 1)
        ans = []
        for i in reversed(range(len(nums))):
            posid = value2id[nums[i]]
            ans.append(bit.query(posid - 1))
            bit.update(posid)
        return ans[::-1]
