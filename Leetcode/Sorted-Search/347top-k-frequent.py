"""
给定一个非空的整数数组，返回其中出现频率前k高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]


提示：
你可以假设给定的k总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) ,n是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
"""
from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        return [e[0] for e in collections.Counter(nums).most_common(k)]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        def shift_up(arr, child):
            # 上浮log(k)，如果新加入的节点<父节点就一直上浮
            val = arr[child]
            while child >> 1 > 0 and val[1] < arr[child >> 1][1]:
                arr[child] = arr[child >> 1]
                child >>= 1
            arr[child] = val

        def shift_down(arr, root, k):
            # 下沉log(k)，如果新的根节点>子节点就一直下沉
            val = arr[root]
            while root << 1 < k:
                # 选取左右孩子中小的与父节点交换
                child = root << 1
                if child | 1 < k and arr[child | 1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点，交换，如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0, 0)]
        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            shift_up(heap, len(heap) - 1)
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                shift_down(heap, 1, k + 1)
        return [item[0] for item in heap[1:]]
