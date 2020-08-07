"""
移除K个数字(leetcode402)

题目：已知一个使用字符串表示非负整数num，将num中的k个数字移除，求移除k个数字后，可以获得的最小的可能的新数字(num不会以0开头，num长度小于10002)

例如：输入：num = “1432219”,k=3
在去掉3个数字后得到的很多可能里，如1432，4322，2219，1219。。。。；去掉数字4、3、2、得到的1219最小

思考与分析：

一个长度为n的数字，去掉k个数字，可以有多少种可能？C(k,n)=n!/(n−k)!∗k!C(k,n)=n!/(n−k)!∗k!种可能
所以用枚举法肯定是不可能的。
若去掉某一位数字，为了使得到的新数字最小，需要尽可能让得到的新数字优先最高位最小，其次次位最小，再其次第三位最小。。。。

例如：一个四位数 “1。。。”，一定比任何“9.。。。”小。
一个四位数若最高位确定，如“51。。”一定比任何“59。。”、“57。。”小。

贪心规律：

从高位向地位遍历，如果对应的数字大于下一位数字，则把该位数字去掉，得到的数字最小。

算法设计：
使用栈存储最终结果或删除工作，从高位向低位遍历num，如果遍历的数字大于栈顶元素，则将该数字push入栈，如果小于栈顶元素则进行pop弹栈，直到栈为空或不能再删除数字(k==0)或栈顶小于当前元素为止。最终栈中从栈底到栈顶存储的数字，即为结果。
"""


class Solution:
    @staticmethod
    def remove_k_nums(nums, k):
        s = []
        nums = list(map(int, nums))
        for i in range(len(nums)):
            while len(s) != 0 and s[len(s) - 1] > nums[i] and k > 0:
                s.pop(-1)
                k -= 1
            if nums[i] != 0 or len(s) != 0:
                s.append(nums[i])
        while len(s) != 0 and k > 0:
            s.pop(-1)
            k -= 1
        result = ''.join(str(i) for i in s)
        return result


if __name__ == "__main__":
    S = Solution()
    print(S.remove_k_nums("1430219", 3))
