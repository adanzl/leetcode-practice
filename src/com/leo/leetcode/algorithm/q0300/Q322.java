package com.leo.leetcode.algorithm.q0300;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q322 {

    public static void main(String[] args) {
        new Q322().TestOJ();
    }

    public void TestOJ() {
        System.out.println(coinChange(LCUtil.stringToIntegerArray("[1, 2, 5]"), 100)); // 20
        System.out.println(coinChange(LCUtil.stringToIntegerArray("[1, 2, 5]"), 11)); // 3
        System.out.println(coinChange(LCUtil.stringToIntegerArray("[2]"), 3)); // -1
    }

    public int coinChange(int[] coins, int amount) {
        int[] m = new int[amount];
        Arrays.fill(m, -2);
        return dfs(coins, amount, m);
    }

//    int count(int[] coins, int amount, int[] m) {
//        if (amount == 0) return 0;
//        if (amount < 0) return -1;
//        if (m[amount - 1] != -2) {
//            return m[amount - 1];
//        }
//        int ret = Integer.MAX_VALUE;
//        boolean found = false;
//        for (int coin : coins) {
//            int v = count(coins, amount - coin, m);
//            if (v >= 0) {
//                ret = Math.min(ret, v);
//                found = true;
//            }
//        }
//        if (!found) {
//            ret = -1;
//        } else {
//            ret++;
//        }
//        m[amount - 1] = ret;
//        return ret;
//    }

    int dfs(int[] coins, int amount, int[] m) {
        if (amount < 0) return -1;
        if (amount == 0) return 0;
        if (m[amount - 1] != -2) return m[amount - 1];
        int out = Integer.MAX_VALUE;
        boolean found = false;
        for (int coin : coins) {
            int ret = dfs(coins, amount - coin, m) + 1;
            if (ret > 0 && ret < out) {
                out = ret;
                found = true;
            }
        }
        int r = found ? out : -1;
        m[amount - 1] = r;
        return r;
    }
}
