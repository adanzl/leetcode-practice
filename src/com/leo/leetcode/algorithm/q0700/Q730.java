package com.leo.leetcode.algorithm.q0700;

/**
 * 给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。
 * 通过从 s 中删除 0 个或多个字符来获得子序列。
 * 如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。
 * 如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。
 * 注意：结果可能很大，你需要对 109 + 7 取模 。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s[i] 仅包含 'a', 'b', 'c' 或 'd'
 * 链接：https://leetcode.cn/problems/count-different-palindromic-subsequences
 */
public class Q730 {

    public static void main(String[] args) {
        // 744991227
        System.out.println(new Q730().countPalindromicSubsequences("bddaabdbbccdcdcbbdbddccbaaccabbcacbadbdadbccddccdbdbdbdabdbddcccadddaaddbcbcbabdcaccaacabdbdaccbaacc"));
        // 117990582
        System.out.println(new Q730().countPalindromicSubsequences("bcbacbabdcbcbdcbddcaaccdcbbcdbcabbcdddadaadddbdbbbdacbabaabdddcaccccdccdbabcddbdcccabccbbcdbcdbdaada"));
        // 104860361
        System.out.println(new Q730().countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"));
        // 6
        System.out.println(new Q730().countPalindromicSubsequences("bccb"));
    }
    // 动态规划 https://leetcode.cn/problems/count-different-palindromic-subsequences/solution/zong-he-ji-da-ti-jie-de-li-jie-by-jincun-9glh/
    public int countPalindromicSubsequences(String s) {
        int n = s.length(), MOD = 1_000_000_007;
        long[][] dp = new long[n][n];
        for (int i = 0; i < n; i++) dp[i][i] = 1;
        for (int i = n - 2; i >= 0; i--) {
            int[] l = new int[]{MOD, MOD, MOD, MOD}, r = new int[]{-1, -1, -1, -1};
            for (int j = i + 1; j < n; j++) {
                char cl = s.charAt(i), cr = s.charAt(j);
                if (cl == cr) {
                    long v = dp[i + 1][j - 1] * 2 + 2;
                    if (l[cl - 'a'] == r[cr - 'a']) v--;
                    else if (l[cl - 'a'] < r[cr - 'a']) v -= 2 + dp[l[cl - 'a'] + 1][r[cr - 'a'] - 1];
                    dp[i][j] = (v + MOD) % MOD;
                } else {
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + MOD) % MOD;
                }
                l[cr - 'a'] = Math.min(l[cr - 'a'], j);
                r[cr - 'a'] = Math.max(r[cr - 'a'], j);
            }
        }
        return (int) dp[0][n - 1];
    }
}
