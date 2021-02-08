package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
 * （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
 * 返回 A 中好子数组的数目。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 20000
 * 2、1 <= A[i] <= A.length
 * 3、1 <= K <= A.length
 * <p>
 * 链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
 */
public class Q992 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q992().subarraysWithKDistinct(stringToIntegerArray("[1,2,1,2,3]"), 2));
        // 3
        System.out.println(new Q992().subarraysWithKDistinct(stringToIntegerArray("[1,2,1,3,4]"), 3));
    }

    public int subarraysWithKDistinct(int[] A, int K) {
        return atMostKDistinct(A, K) - atMostKDistinct(A, K - 1);
    }

    private int atMostKDistinct(int[] A, int K) {
        int ret = 0, l = 0, r = 0, count = 0;
        int[] marks = new int[A.length + 1];
        while (r < A.length) {
            if (marks[A[r]] == 0) count++;
            marks[A[r]]++;
            r++;
            while (count > K) {
                marks[A[l]]--;
                if (marks[A[l]] == 0) count--;
                l++;
            }
            ret += r - l;
        }
        return ret;
    }
}
