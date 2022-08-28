package com.leo.leetcode.algorithm.q0700;

/**
 * f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。
 * 例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
 * 给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。
 * 提示: 0 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function
 */
public class Q793 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q793().preimageSizeFZF(1000000000));
        // 0
        System.out.println(new Q793().preimageSizeFZF(36));
        // 0
        System.out.println(new Q793().preimageSizeFZF(80502705));
        // 5
        System.out.println(new Q793().preimageSizeFZF(3));
        // 5
        System.out.println(new Q793().preimageSizeFZF(0));
    }

    // 阶乘结尾0
    public int preimageSizeFZF(int k) {
        if (k == 0) return 5;
        long l = 0, r = Long.MAX_VALUE;
        while (l <= r) {
            long mid = l + (r - l) / 2, v = getTailZero(mid);
            if (k == v) return 5;
            if (k < v) r = mid - 1;
            else l = mid + 1;
        }
        return 0;
    }

    long getTailZero(long num) {
        long ans = 0;
        while (num >= 5) {
            ans += num / 5;
            num /= 5;
        }
        return ans;
    }


}
