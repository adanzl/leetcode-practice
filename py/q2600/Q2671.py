"""
 * 请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对频率相关查询进行应答。
 * 实现 FrequencyTracker 类：
 * 1、FrequencyTracker()：使用一个空数组初始化 FrequencyTracker 对象。
 * 2、void add(int number)：添加一个 number 到数据结构中。
 * 3、void deleteOne(int number)：从数据结构中删除一个 number 。数据结构 可能不包含 number ，在这种情况下不删除任何内容。
 * 4、bool hasFrequency(int frequency): 如果数据结构中存在出现 frequency 次的数字，则返回 true，否则返回 false。
 * 提示：
 * 1、1 <= number <= 10^5
 * 2、1 <= frequency <= 10^5
 * 3、最多调用 add、deleteOne 和 hasFrequency 共计 2 * 10^5 次
 * 链接：https://leetcode.cn/problems/frequency-tracker/
"""
from collections import Counter


class FrequencyTracker:

    def __init__(self):
        self.nums = Counter()
        self.fre = Counter()

    def add(self, number: int) -> None:
        if self.nums[number] > 0:
            self.fre[self.nums[number]] -= 1
        self.nums[number] += 1
        self.fre[self.nums[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.nums:
            c = self.nums[number]
            self.fre[c] -= 1
            self.fre[c - 1] += 1
            self.nums[number] -= 1
            if self.nums[number] == 0:
                del self.nums[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.fre[frequency] > 0


if __name__ == '__main__':
    frequencyTracker = FrequencyTracker()
    frequencyTracker.add(3)  # 数据结构现在包含 [3]
    frequencyTracker.add(3)  # 数据结构现在包含 [3, 3]
    print(frequencyTracker.hasFrequency(2))  # 返回 true ，因为 3 出现 2 次

    frequencyTracker = FrequencyTracker()
    frequencyTracker.add(1)  # 数据结构现在包含 [1]
    frequencyTracker.deleteOne(1)  # 数据结构现在为空 []
    print(frequencyTracker.hasFrequency(1))  # 返回 false ，因为数据结构为空

    frequencyTracker = FrequencyTracker()
    print(frequencyTracker.hasFrequency(2))  # 返回 false ，因为数据结构为空
    frequencyTracker.add(3)  #  数据结构现在包含 [3]
    print(frequencyTracker.hasFrequency(1))  # 返回 true ，因为 3 出现 1 次
