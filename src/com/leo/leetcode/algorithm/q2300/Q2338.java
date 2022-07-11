package com.leo.leetcode.algorithm.q2300;

import java.util.*;

/**
 * 给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。
 * 对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：
 * 1、每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。
 * 2、每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。
 * 返回长度为 n 的 不同 理想数组的数目。由于答案可能很大，返回对 109 + 7 取余的结果。
 * 提示：
 * 1、2 <= n <= 10^4
 * 2、1 <= maxValue <= 10^4
 * 链接：https://leetcode.cn/problems/count-the-number-of-ideal-arrays
 */
public class Q2338 {

    public static void main(String[] args) {
        // 805568701
        System.out.println(new Q2338().idealArrays(9559, 9581));
        // 465040898
        System.out.println(new Q2338().idealArrays(5878, 2900));
        // 10
        System.out.println(new Q2338().idealArrays(2, 5));
        // 11
        System.out.println(new Q2338().idealArrays(5, 3));
    }

    public int idealArrays(int n, int maxValue) {
        int MOD = 1_000_000_007;
        // 小-大 C[m][n]=C[m][n-1]+C[m-1][n-1] 组合数计算
        int[][] C = new int[14][maxValue + n];
        C[0][0] = 1;
        for (int i = 0; i <= 13; i++) {
            for (int j = 1; j < maxValue + n; j++) {
                if (i == 0) C[i][j] = 1;
                else C[i][j] = (C[i][j - 1] + C[i - 1][j - 1]) % MOD;
            }
        }
        // 分解质因数
        List<Map<Integer, Integer>> primeFactor = new ArrayList<>();
        for (int i = 0; i <= maxValue; i++) {
            int p = 2, num = i;
            Map<Integer, Integer> pMap = new HashMap<>();
            primeFactor.add(pMap);
            while (p * p <= num) {
                if (num % p == 0) {
                    int x = 0;
                    for (; num % p == 0; num /= p) x++;
                    pMap.put(p, pMap.getOrDefault(p, 0) + x);
                } else p++;
            }
            if (num > 1) pMap.put(num, 1);
        }
        long ret = 0;
        for (int i = 1; i <= maxValue; i++) {
            long v = 1;
            for (Map.Entry<Integer, Integer> entry : primeFactor.get(i).entrySet()) {
                int cnt = entry.getValue();
                v = (v * C[cnt][n + cnt - 1]) % MOD;
            }
            ret = (ret + v) % MOD;
        }
        return (int) ret;
    }

}
