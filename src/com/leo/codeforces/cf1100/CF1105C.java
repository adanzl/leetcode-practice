package com.leo.codeforces.cf1100;

import java.util.Arrays;

/**
 * Ayoub had an array 𝑎 of integers of size 𝑛 and this array had two interesting properties:
 * All the integers in the array were between 𝑙 and 𝑟 (inclusive).
 * The sum of all the elements was divisible by 3.
 * Unfortunately, Ayoub has lost his array, but he remembers the size of the array 𝑛 and the numbers 𝑙 and 𝑟, so he asked you to find the number of ways to restore the array.
 * Since the answer could be very large, print it modulo 10^9+7 (i.e. the remainder when dividing by 10^9+7). In case there are no satisfying arrays (Ayoub has a wrong memory), print 0.
 * Input
 * The first and only line contains three integers 𝑛, 𝑙 and 𝑟 (1≤𝑛≤2⋅105,1≤𝑙≤𝑟≤109) — the size of the lost array and the range of numbers in the array.
 * Output
 * Print the remainder when dividing by 10^9+7 the number of ways to restore the array.
 * 链接：https://codeforces.com/contest/1105/problem/C
 * 链接：https://www.luogu.com.cn/problem/CF1105C
 */
public class CF1105C {

    public static void main(String[] args) {
        // 69063912
        System.out.println(func(200_000, 1, 1_000_000_000));
        // 710038164
        System.out.println(func(1000, 562, 6782363));
        // 1
        System.out.println(func(3, 2, 2));
        // 3
        System.out.println(func(2, 1, 3));
        // 711426616
        System.out.println(func(9, 9, 99));
        /*
          Scanner sc = new Scanner(System.in);
          int n = sc.nextInt();
          int l = sc.nextInt();
          int r = sc.nextInt();
          System.out.println(func(n, l, r));
         */
    }

    static int func(int n, int l, int r) {
        int MOD = 1_000_000_007;
        int d = (r - l + 1) / 3, re = (r - l + 1) % 3, offset = l % 3;
        long[] mem = new long[]{d, d, d};
        for (int i = 0; i < re; i++) mem[(offset + i) % 3]++;
        long[] dp = Arrays.copyOf(mem, 3);
        for (int i = 0; i < n - 1; i++) {
            long[] newDp = new long[3];
            newDp[0] = (newDp[0] + dp[0] * mem[0] + dp[1] * mem[2] + dp[2] * mem[1]) % MOD;
            newDp[1] = (newDp[1] + dp[0] * mem[1] + dp[1] * mem[0] + dp[2] * mem[2]) % MOD;
            newDp[2] = (newDp[2] + dp[0] * mem[2] + dp[2] * mem[0] + dp[1] * mem[1]) % MOD;
            dp = newDp;
        }
        return (int) dp[0];
    }
}
