# def queen(A, cur=0):
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 break
#         if flag:
#             queen(A, cur+1)
#
#
# queen([None]*8)


from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def shift_down(arr, root, k):
            # 下沉log(k)，如果新的根节点>子节点就一直下沉
            val = arr[root]
            while root << 1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child | 1 < k and arr[child | 1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点，交换，如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def shift_up(arr, child):
            # 上浮log(k)，如果新加入的节点<父节点就一直上浮
            val = arr[child]
            while child >> 1 > 0 and val[1] < arr[child >> 1][1]:
                arr[child] = arr[child >> 1]
                child >>= 1
            arr[child] = val

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

    def findKthLargest(self, nums: List[int], k: int) -> int:
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
        for i in range(min(len(nums), k)):
            heap.append(nums[i])
            shift_up(i)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                shift_down(0, k-1)
        return heap[0]


if __name__ == '__main__':
    ret = Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
    print(ret)

