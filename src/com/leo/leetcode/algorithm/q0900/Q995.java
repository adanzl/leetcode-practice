package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。
 * 返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 30000
 * 2、1 <= K <= A.length
 * <p>
 * 链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips
 */
public class Q995 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q995().minKBitFlips(stringToIntegerArray("[1,1,1]"), 2));
        // 3
        System.out.println(new Q995().minKBitFlips(stringToIntegerArray("[0,0,0,1,0,1,1,0]"), 3));
        // 2
        System.out.println(new Q995().minKBitFlips(stringToIntegerArray("[0,1,0]"), 1));
        // -1
        System.out.println(new Q995().minKBitFlips(stringToIntegerArray("[1,1,0]"), 2));
    }

    public int minKBitFlips(int[] A, int K) {
        int l = 0, r = 0, ret = 0;
        while (r < A.length) {
            while (l <= r && A[l] == 1) l++;
            if (r - l + 1 == K) {
                for (int i = l; i <= r; i++) A[i] ^= 1;
                ret++;
            }
            r++;
        }
        while (l < r && A[l] == 1) l++;
        return l != r ? -1 : ret;
    }
}
