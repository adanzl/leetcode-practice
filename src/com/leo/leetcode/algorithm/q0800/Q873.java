package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
 * 1、n >= 3
 * 2、对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
 * 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
 * （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
 * 提示：
 * 1、3 <= arr.length <= 1000
 * 2、1 <= arr[i] < arr[i + 1] <= 10^9
 * 链接：https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence
 */
public class Q873 {

    public static void main(String[] args) {
        //
        System.out.println(new Q873().lenLongestFibSubSeq(stringToIntegerArray("[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]")));
        // 5
        System.out.println(new Q873().lenLongestFibSubSeq(stringToIntegerArray("[1,2,3,4,5,6,7,8]")));
        // 3
        System.out.println(new Q873().lenLongestFibSubSeq(stringToIntegerArray("[1,2,3]")));
        // 3
        System.out.println(new Q873().lenLongestFibSubSeq(stringToIntegerArray("[1,3,7,11,12,14,18]")));
    }

    public int lenLongestFibSubSeq(int[] arr) {
        int n = arr.length, ret = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                ret = Math.max(ret, fibCount(arr, j + 1, 0, arr[i], arr[j]));
            }
        }
        return ret == 0 ? ret : ret + 2;
    }

    int fibCount(int[] arr, int offset, int count, long v1, long v2) {
        long v = v1 + v2;
        if (offset >= arr.length) return count;
        if (v > 1_000_000_007) return count;
        int idx = Arrays.binarySearch(arr, offset, arr.length, (int) v);
        if (idx < 0) return count;
        return fibCount(arr, idx + 1, count + 1, v2, v);
    }
}
