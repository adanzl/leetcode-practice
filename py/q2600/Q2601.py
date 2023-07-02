"""
 * 给你一个下标从 0 开始的整数数组 nums ，数组长度为 n 。
 * 你可以执行无限次下述运算：选择一个之前未选过的下标 i ，并选择一个 严格小于 nums[i] 的质数 p ，从 nums[i] 中减去 p 。
 * 如果你能通过上述运算使得 nums 成为严格递增数组，则返回 true ；否则返回 false 。
 * 严格递增数组 中的每个元素都严格大于其前面的元素。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 1000
 * 3、nums.length == n
 * 链接：https://leetcode.cn/problems/prime-subtraction-operation
"""
from typing import List


class Solution:

    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        # 线性筛选质数
        LIMIT = 1000 + 5
        b_prime = [False] * LIMIT
        prime_list = []
        mn = LIMIT
        for i in range(2, LIMIT):
            if not b_prime[i]:
                if prime_list:
                    if i - prime_list[-1] < mn:
                        mn = i - prime_list[-1]
                prime_list.append(i)

            for prime in prime_list:
                nx = prime * i
                if nx < LIMIT:
                    b_prime[nx] = True
                else:
                    break
        mn = nums[-1]
        for i in range(n - 2, -1, -1):
            idx = 0
            while nums[i] >= mn and idx < len(prime_list):
                if nums[i] - prime_list[idx] < mn:
                    nums[i] -= prime_list[idx]
                idx += 1
            if nums[i] >= mn or nums[i] < 1:
                return False
            mn = nums[i]
        return True


if __name__ == '__main__':
    # True
    print(Solution().primeSubOperation([4, 9, 6, 10]))
    # True
    print(Solution().primeSubOperation([6, 8, 11, 12]))
    # False
    print(Solution().primeSubOperation([5, 8, 3]))
