package com.leo.leetcode.algorithm.q0600;

/**
 * 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
 * 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
 * 注意：
 * 1、m 和 n 的范围在 [1, 30000] 之间。
 * 2、k 的范围在 [1, m * n] 之间。
 * 链接：https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table
 */
public class Q668 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q668().findKthNumber(3, 3, 6));
        // 3
        System.out.println(new Q668().findKthNumber(3, 3, 5));
        // 6
        System.out.println(new Q668().findKthNumber(2, 3, 6));
    }

    public int findKthNumber(int m, int n, int k) {
        int l = 1, r = m * n, min = Math.min(m, n), max = Math.max(m, n);
        // 让l尽可能小，l最小的时候，一定一个乘法表中的值
        while (l <= r) {
            int mid = l + (r - l) / 2, sum = 0;
            for (int i = 1; i <= min; i++) {
                sum += Math.min(mid / i, max);
                if (sum >= k) break;
            }
            if (sum < k) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}
