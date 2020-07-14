package com.leo.leetcode.algorithm;

/**
 * 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
 * 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/
 */
public class Q96 {
    public static void main(String[] args) {
        new Q96().TestOJ();
    }

    public void TestOJ() {
        System.out.println(numTrees(3)); // 5
        System.out.println(numTrees(0)); // 1
        System.out.println(numTrees1(1)); // 1
        System.out.println(numTrees(2)); // 2
    }


    public int numTrees1(int n) {
        if (n == 0) return 1;
        if (n == 1) return 1;
        int ret = 0;
        for (int i = 0; i < n; i++) {
            ret += numTrees(i) * numTrees(n - 1 - i);
        }
        return ret;
    }

    public int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < n + 1; i++)
            for (int j = 1; j < i + 1; j++)
                dp[i] += dp[j - 1] * dp[i - j];
        return dp[n];
    }

}
