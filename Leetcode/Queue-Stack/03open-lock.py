"""
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

示例 1:

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
"""
from queue import Queue


class Solution:
    # def open_lock(deadends, target) -> int:
    #     deadends = set(deadends)
    #     if '0000' in deadends:
    #         return -1
    #
    #     # 初始化根节点
    #     q = Queue()
    #     q.put(('0000', 0))  # 当前节点，转动次数
    #     while not q.empty():
    #         # 取出一个节点
    #         node, step = q.get()
    #         # 放入周围节点
    #         for i in range(4):
    #             for add in (1, -1):
    #                 cur = node[:i] + str((int(node[i]) + add) % 10) + node[i+1:]
    #                 if cur == target:
    #                     return step + 1
    #                 if cur not in deadends:
    #                     q.put((cur, step + 1))
    #                     deadends.add(cur)
    #     return -1

    def open_lock(self, deadends, target) -> int:
        if '0000' in deadends:
            return -1

        def get_neighbor(node: str):
            for i in range(4):
                x = int(node[i])
                for j in [-1, 1]:
                    y = (x + j) % 10
                    yield node[:i] + str(y) + node[i+1:]

        deadends = set(deadends)
        # 双向bfs
        res = 0
        front_q, behind_q = set(), set()
        visited = set()
        front_q.add('0000')
        behind_q.add(target)
        while front_q and behind_q:
            if front_q and behind_q:
                return res
            if len(front_q) > len(behind_q):
                front_q, behind_q = behind_q, front_q
            temp = set()
            for cur_node in front_q:
                if cur_node in deadends:
                    continue
                visited.add(cur_node)
                for node in get_neighbor(cur_node):
                    if node not in visited:
                        temp.add(node)
            front_q = temp
            res += 1
        return -1
