"""
 * 给你一个 n 个视频的上传序列，每个视频编号为 1 到 n 之间的 不同 数字，你需要依次将这些视频上传到服务器。请你实现一个数据结构，在上传的过程中计算 最长上传前缀 。
 * 如果 闭区间 1 到 i 之间的视频全部都已经被上传到服务器，那么我们称 i 是上传前缀。最长上传前缀指的是符合定义的 i 中的 最大值 。
 * 请你实现 LUPrefix 类：
 * 1、LUPrefix(int n) 初始化一个 n 个视频的流对象。
 * 2、void upload(int video) 上传 video 到服务器。
 * 3、int longest() 返回上述定义的 最长上传前缀 的长度。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= video <= 10^5
 * 3、video 中所有值 互不相同 。
 * 4、upload 和 longest 总调用 次数至多不超过 2 * 10^5 次。
 * 5、至少会调用 longest 一次。
 * 链接：https://leetcode.cn/problems/longest-uploaded-prefix/
"""
from typing import *
from math import *
from collections import *


class LUPrefix:

    def __init__(self, n: int):
        self.arr = [0] * (n + 1)
        self.l = 0

    def upload(self, video: int) -> None:
        self.arr[video - 1] = 1
        while self.l < len(self.arr) and self.arr[self.l] == 1:
            self.l += 1

    def longest(self) -> int:
        return self.l


if __name__ == '__main__':
    server = LUPrefix(4)
    # 0
    print(server.longest())
    server.upload(1)
    print(server.longest())
    server.upload(2)
    print(server.longest())
