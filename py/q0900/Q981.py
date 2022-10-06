"""
 * 设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。
 * 实现 TimeMap 类：
 * 1、TimeMap() 初始化数据结构对象
 * 2、void set(String key, String value, int timestamp) 存储键 key、值 value，以及给定的时间戳 timestamp。
 * 3、String get(String key, int timestamp)
 * - 返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp 。
 * - 如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
 * - 如果没有值，则返回空字符串（""）。
 * 提示：
 * 1、1 <= key.length, value.length <= 100
 * 2、key 和 value 由小写英文字母和数字组成
 * 3、1 <= timestamp <= 10^7
 * 4、set 操作中的时间戳 timestamp 都是严格递增的
 * 5、最多调用 set 和 get 操作 2 * 10^5 次
 * 链接：https://leetcode-cn.com/problems/time-based-key-value-store
"""
from bisect import *
from collections import defaultdict
from typing import *


class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        d = self.dic[key]
        i = bisect_left(d, timestamp, key=lambda x: x[0])
        if i < len(d) and d[i][0] == timestamp:
            d[i][1] = value
        else:
            insort(d, [timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        d = self.dic[key]
        if not d:
            return ""
        i = bisect_left(d, timestamp, key=lambda x: x[0])
        if i < len(d) and d[i][0] == timestamp:
            return d[i][1]
        else:
            return d[i - 1][1] if i > 0 else ""


if __name__ == '__main__':
    timeMap = TimeMap()
    print(timeMap.get('foo', 1))  # ""
    timeMap.set("foo", "bar", 1)  # 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1
    print(timeMap.get("foo", 0))  # 返回 ""
    print(timeMap.get("foo", 1))  # 返回 "bar"
    print(timeMap.get("foo", 3))  # 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
    timeMap.set("foo", "bar2", 4)  # 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4
    print(timeMap.get("foo", 4))  # 返回 "bar2"
    print(timeMap.get("foo", 5))  # 返回 "bar2"