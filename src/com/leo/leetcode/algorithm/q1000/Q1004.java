package com.leo.leetcode.algorithm.q1000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
 * 返回仅包含 1 的最长（连续）子数组的长度。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 20000
 * 2、0 <= K <= A.length
 * 3、A[i] 为 0 或 1
 * <p>
 * 链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii/
 */
public class Q1004 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q1004().longestOnes(stringToIntegerArray("[1,1,1,0,0,0,1,1,1,1,0]"), 2));
        // 4
        System.out.println(new Q1004().longestOnes(stringToIntegerArray("[1,1,1,0,0,0,1,1,1,1,0]"), 0));
        // 11
        System.out.println(new Q1004().longestOnes(stringToIntegerArray("[1,1,1,0,0,0,1,1,1,1,0]"), 11));
        // 10
        System.out.println(new Q1004().longestOnes(stringToIntegerArray("[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]"), 3));
    }

    public int longestOnes(int[] A, int K) {
        int l = 0, r = 0, ret = 0, zCount = 0;
        while (r < A.length) {
            if (A[r] == 0) {
                zCount++;
                if (zCount > K) {
                    while (A[l] != 0) l++;
                    l++;
                    zCount--;
                }
            }
            ret = Math.max(ret, r - l + 1);
            r++;
        }
        return ret;
    }
}
