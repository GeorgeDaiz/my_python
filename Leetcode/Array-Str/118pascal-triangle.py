"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    @staticmethod
    def generate(num_rows: int):
        if not num_rows:
            return []
        res = [[1]]
        for i in range(1, num_rows):
            res.append(list(map(lambda x, y: x+y, [0] + res[-1], res[-1] + [0])))
        return res[: num_rows]

        # while len(res) < numRows:
        #     res.append([a+b for a, b in zip([0]+res[-1], res[-1]+[0])])
        # return res

    # 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
    @staticmethod
    def get_row(row_index: int):
        # p = [1]
        # if not row_index:
        #     return p
        # for _ in range(row_index):
        #     p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
        # return p

        result = [1] + [0] * row_index
        for i in range(row_index):
            for j in range(i + 1, 0, -1):
                result[j] += result[j - 1]
        return result


if __name__ == '__main__':
    res = Solution().get_row(7)
    print(res)
