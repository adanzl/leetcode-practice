package com.leo.leetcode.algorithm.q0400;

/**
 * 以字符串的形式给出 n , 以字符串的形式返回 n 的最小 好进制  。
 * 如果 n 的 k(k>=2) 进制数的所有数位全为1，则称 k(k>=2) 是 n 的一个 好进制 。
 * 提示：
 * 1、n 的取值范围是 [3, 10^18]
 * 2、n 没有前导 0
 * 链接：https://leetcode-cn.com/problems/smallest-good-base
 */
public class Q483 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q483().smallestGoodBase("13"));
        // 8
        System.out.println(new Q483().smallestGoodBase("4681"));
        // 999999999999999999
        System.out.println(new Q483().smallestGoodBase("1000000000000000000"));
    }

    public String smallestGoodBase(String n) {
        int sign = Math.max(64, n.length());
        long ln = Long.parseLong(n);
        long ans = ln - 1;
        for (int s = sign; s >= 2; s--) {
            int k = (int) Math.pow(ln, 1.0 / s);   // k 为 n^{1/s} 的整数部分
            if (k > 1) {    // 判断 k 是否是一个合法的进制
                long sum = 1, mul = 1;   // 计算 (11...11)k 对应的十进制值
                for (int i = 1; i <= s; ++i) {
                    mul *= k;
                    sum += mul;
                }
                if (sum == ln) {
                    ans = k;
                    break;
                }
            }
        }
        return String.valueOf(ans);
    }
}
