"""
给定一个正整数 n（1 ≤n≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1

描述前一项，这个数是 1 即 “一个 1 ”，记作 11

描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

示例1:
输入: 1
输出: "1"
解释：这是一个基本样例。

示例 2:
输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
"""
import re


class Solution:
    def countAndSay(self, n: int) -> str:
        # 递归
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        p, q = 0, 1
        res = []
        while q <= len(s):
            if q == len(s):
                res.extend([str(q - p), s[p]])
            elif s[p] != s[q]:
                res.extend([str(q - p), s[p]])
                p = q
            q += 1
        return "".join(res)

    def countAndSay1(self, n: int) -> str:
        # 双指针
        res = ['1']
        r = 1
        while r < n:
            r += 1
            p, q = 0, 1
            temp = []
            while q <= len(res):
                if q == len(res):
                    temp.extend([str(q - p), res[p]])
                elif res[q] != res[p]:
                    temp.extend([str(q - p), res[p]])
                    p = q
                q += 1
            res += q
        return ''.join(res)

    def countAndSay2(self, n: int) -> str:
        # 迭代
        res = ['1']
        for _ in range(n-1):
            p, q = 0, 1
            tmp = []
            while q <= len(res):
                if q == len(res):
                    tmp.extend([str(q - p), res[p]])
                elif res[p] != res[q]:
                    tmp.extend([str(q - p), res[p]])
                q += 1
            res = tmp
        return ''.join(res)

    def countAndSay3(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)

        # 字符串 (\d)\1* 可以用来匹配结果。这里用来提取连在一块的元素， 如 '111221'，提取出的元素
        # 是 res = ['111', '22', '1']。
        # (\d)\1*解释：
        # \1 是为了引用前面的 \d，表明 \1 是与 \d 匹配到相同的数字。
        # 只有 \d 添加了（），才能被引用，在正则里面称之为捕获组。
        # * 表示重复匹配前面字符 0 次或多次。所以可以匹配的到像 1 、111、11 这样连在一起并相同的数字。

        pattern = re.compile(r'(\d)\1*')
        res = []
        for _ in pattern.finditer(s):
            res.append(_.group())
        # 可简写为：
        # pattern = re.compile(r'(\d)\1*')
        # res = [_.group() for _ in pattern.finditer(s)]

        tmp = []
        for c in res:
            tmp.append(str(len(c)) + c[0])
        return "".join(tmp)
        # 可简写为：
        # return ''.join(str(len(c)) + c[0] for c in res)


if __name__ == '__main__':
    ret = Solution().countAndSay(10)
    print(ret)
