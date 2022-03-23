package com.leo.leetcode.algorithm.q0400;

/**
 * 给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。
 * 提示: 1 <= k <= n <= 10^9
 * 链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/
 */
public class Q440 {
    // 以特定数字开头的数字
    public static void main(String[] args) {
        // 416126219
        System.out.println(new Q440().findKthNumber(681692778, 351251360));
        // 9
        System.out.println(new Q440().findKthNumber(100, 90));
        // 100000000
        System.out.println(new Q440().findKthNumber(1000000000, 9));
        // 10
        System.out.println(new Q440().findKthNumber(13, 2));
        // 100002
        System.out.println(new Q440().findKthNumber(1000000, 9));
        // 18997
        System.out.println(new Q440().findKthNumber(100000, 9999));
        // 1
        System.out.println(new Q440().findKthNumber(1, 1));
    }


    public int findKthNumber(int n, int k) {
        for (int base = 1; base <= n; ) {
            int count = getCount(base, n);
            if (k > count) {
                k -= count;
                base++;
            } else {
                k--;
                if (k == 0) return base;
                base *= 10;
            }
        }
        return 0;
    }

    int getCount(int pre, int limit) {
        int ret = 0;
        for (long h = pre, l = pre + 1; h <= limit; h *= 10, l *= 10) {
            // 区间内没有超过limit的数字，一位一位计算，例如20-10， 200-100
            ret += Math.min(limit + 1, l) - h;
        }
        return ret;
    }
}
