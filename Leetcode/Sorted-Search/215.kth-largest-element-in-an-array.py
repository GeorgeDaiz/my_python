"""
215.数组中的第k个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        # 库函数
        nums.sort()
        return nums[len(nums)-k]

    def findKthLargest1(self, nums: list, k: int) -> int or None:
        # 快排
        n = len(nums)
        if k > n:
            return None
        index = self.quick_sort(nums, 0, n-1, k)
        return nums[index]

    def quick_sort(self, nums, l, r, k):
        if l > r:
            return l
        p = self.partition(nums, l, r)
        if p+1 == k:
            return p
        if p+1 > k:
            return self.quick_sort(nums, l, p-1, k)
        else:
            return self.quick_sort(nums, p+1, r, k)

    def partition(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] > v:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 最小堆
        def shift_up(child):
            # 构建堆，新加入的叶子节点<父节点就上浮
            val = heap[child]
            while child > 0 and val < heap[child >> 1]:
                heap[child] = heap[child >> 1]
                child = child >> 1
            heap[child] = val
            print(heap)

        def shift_down(root, k):
            # 维护k+1的堆，新加入的根节点>子节点就下沉
            val = heap[root]
            while root << 1 <= k:
                # 找出较小的子节点
                child = root << 1
                if child | 1 <= k and heap[child | 1] < heap[child]:
                    child = child | 1
                # 新加入的根节点和子节点比较
                if heap[child] < val:
                    heap[root] = heap[child]
                    root = child
                else:
                    break
            heap[root] = val
            print(heap)

        heap = []
        # 上浮式建堆
        for i in range(min(len(nums), k)):
            heap.append(nums[i])
            shift_up(i)

        # 下沉式维护堆
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                shift_down(0, k-1)
        return heap[0]


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        for i in range(k//2-1, -1, -1):
            self.shift_down(heap, i, k - 1)
        for j in range(k, len(nums)):
            if nums[j] > heap[0]:
                heap[0] = nums[j]
                self.shift_down(heap, 0, k - 1)
        return heap[0]

    def shift_down(self, heap, l, r):
        val = heap[l]
        i = l
        j = i * 2 + 1
        while j <= r:
            if j+1 <= r and heap[j+1] < heap[j]:
                j = j + 1
            if heap[j] < val:
                heap[i] = heap[j]
                i = j
                j = i * 2 + 1
            else:
                break
        heap[i] = val


if __name__ == '__main__':
    ret = Solution().findKthLargest2([7, 6, 5, 4, 3, 2, 1], 4)
    print(ret)
