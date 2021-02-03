package com.leo.leetcode.algorithm.q0200;

/**
 * 统计所有小于非负整数 n 的质数的数量。
 * <p>
 * 提示： 0 <= n <= 5 * 10^6
 * <p>
 * 链接：https://leetcode-cn.com/problems/count-primes/
 */
public class Q204 {

    public static void main(String[] args) {
        // 114155
        System.out.println(new Q204().countPrimes(1500000));
        // 41537
        System.out.println(new Q204().countPrimes(499979));
        // 4
        System.out.println(new Q204().countPrimes(10));
        // 4
        System.out.println(new Q204().countPrimes(10));
        // 0
        System.out.println(new Q204().countPrimes(0));
        // 0
        System.out.println(new Q204().countPrimes(1));
    }

    public int countPrimes(int n) {
        if (n < 2) return 0;
        int count = 0;
        boolean[] primes = new boolean[5000001];
        l:
        for (int i = 2; i < n; i++) {
            double limit = 1.0 / sqrt(i);
            for (int j = 2; j <= limit; j++) {
                if (!primes[j]) continue;
                if (i % j == 0) continue l;
            }
            primes[i] = true;
            count++;
        }
        return count;
    }

    double sqrt(double x) {
        double x_half = 0.5d * x;
        long i = Double.doubleToLongBits(x);
        i = 0x5fe6ec85e7de30daL - (i >> 1);
        x = Double.longBitsToDouble(i);
        x *= (1.5d - x_half * x * x);
        return x;
    }
}
