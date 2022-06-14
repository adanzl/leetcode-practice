package com.leo.leetcode.algorithm.q2100;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为 n 的整数数组 nums 和一个整数 numSlots ，满足2 * numSlots >= n 。总共有 numSlots 个篮子，编号为 1 到 numSlots 。
 * 你需要把所有 n 个整数分到这些篮子中，且每个篮子 至多 有 2 个整数。一种分配方案的 与和 定义为每个数与它所在篮子编号的 按位与运算 结果之和。
 * 比方说，将数字 [1, 3] 放入篮子 1 中，[4, 6] 放入篮子 2 中，这个方案的与和为 (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4 。
 * 请你返回将 nums 中所有数放入 numSlots 个篮子中的最大与和。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= numSlots <= 9
 * 3、1 <= n <= 2 * numSlots
 * 4、1 <= nums[i] <= 15
 * 链接：https://leetcode.cn/problems/maximum-and-sum-of-array
 */
public class Q2172 {

    public static void main(String[] args) {
        // 9
        System.out.println(new Q2172().maximumANDSum(stringToIntegerArray("[1,2,3,4,5,6]"), 3));
        // 24
        System.out.println(new Q2172().maximumANDSum(stringToIntegerArray("[1,3,10,4,7,1]"), 9));
    }

    // https://leetcode.cn/problems/maximum-and-sum-of-array/solution/zhuang-tai-ya-suo-dp-by-endlesscheng-5eqn/
    public int maximumANDSum(int[] nums, int numSlots) {
        int cnt = numSlots * 2;
        int[] f = new int[1 << cnt + 1];
        Set<Integer> set = new HashSet<>();
        set.add(0);
        for (int num : nums) {
            Set<Integer> nextSet = new HashSet<>();
            for (int v : set) {
                for (int j = 0; j < cnt; j++) {
                    if ((v & (1 << j)) != 0) continue;
                    int idx = v | (1 << j);
                    f[idx] = Math.max(f[idx], f[v] + (num & (j / 2 + 1)));
                    nextSet.add(idx);
                }
            }
            set = nextSet;
        }
        int ret = 0;
        for (int c : f) ret = Math.max(ret, c);
        return ret;
    }
}
