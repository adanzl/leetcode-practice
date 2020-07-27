package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

/**
 * 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
 * 设计一个算法使得这 m 个子数组各自和的最大值最小。 
 * 注意:
 *     数组长度 n 满足以下条件: 1 ≤ n ≤ 1000 1 ≤ m ≤ min(50, n) 
 * 链接：https://leetcode-cn.com/problems/split-array-largest-sum
 */
class Q410 {

    public static void main(String[] args) {
        System.out.println(new Q410().splitArray(LCUtil.stringToIntegerArray("[2,3,1,1,1,1,1]"), 5)); // 3
        System.out.println(new Q410().splitArray(LCUtil.stringToIntegerArray("[1,2147483647]"), 2)); // 2147483647
        System.out.println(new Q410().splitArray(LCUtil.stringToIntegerArray("[1,2147483646]"), 1)); // 2147483647
        System.out.println(new Q410().splitArray(LCUtil.stringToIntegerArray("[1,2,3,4,5]"), 2)); // 9
        System.out.println(new Q410().splitArray(LCUtil.stringToIntegerArray("[7,2,5,10,8]"), 2)); // 18
    }

    public int splitArray(int[] nums, int m) {
        long l = 0, r = 0;
        int out = 0;
        for (int i : nums) {
            l = Math.max(l, i);
            r += i;
        }
        while (l <= r) {
            long mid = l + ((r - l) >> 1), count = 1, tmp = 0;
            for (int i : nums) {
                if (tmp + i <= mid) {
                    tmp += i;
                } else {
                    tmp = i;
                    count++;
                    if (count > m) break;
                }
            }
            if (count <= m) out = (int) mid;
            if (count > m) l = mid + 1;
            else r = mid - 1;
        }
        return out;
    }
}