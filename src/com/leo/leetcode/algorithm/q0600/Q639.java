package com.leo.leetcode.algorithm.q0600;

/**
 * 一条包含字母 A-Z 的消息通过以下的方式进行了 编码 ：
 * 'A' -> "1"
 * 'B' -> "2"
 * ...
 * 'Z' -> "26"
 * 要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：
 * "AAJF" 对应分组 (1 1 10 6)
 * "KJF" 对应分组 (11 10 6)
 * 注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。
 * 除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串 "1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息。
 * 给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。
 * 由于答案数目可能非常大，返回 10^9 + 7 的 模 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 是 0 - 9 中的一位数字或字符 '*'
 * 链接：https://leetcode.cn/problems/decode-ways-ii
 */
public class Q639 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q639().numDecodings("0"));
        // 404
        System.out.println(new Q639().numDecodings("*1*1*0"));
        // 999
        System.out.println(new Q639().numDecodings("***"));
        // 96
        System.out.println(new Q639().numDecodings("**"));
        // 632933259
        System.out.println(new Q639().numDecodings("*1***********************************"));
        // 18
        System.out.println(new Q639().numDecodings("1*"));
        // 15
        System.out.println(new Q639().numDecodings("2*"));
        // 11
        System.out.println(new Q639().numDecodings("*1"));
        // 9
        System.out.println(new Q639().numDecodings("*"));
    }

    public int numDecodings(String s) {
        int n = s.length(), MOD = 1_000_000_007;
        long[] dp = new long[n + 1];
        char pre = s.charAt(0);
        dp[0] = 1;
        dp[1] = pre == '*' ? 9 : (pre == '0' ? 0 : 1);
        for (int i = 1; i < n; i++) {
            char c = s.charAt(i);
            int c1, c2 = 0;
            if (c == '*') {
                c1 = 9;
                if (pre == '1') c2 = 9;
                else if (pre == '2') c2 = 6;
                else if (pre == '*') c2 = 15;
            } else {
                c1 = c == '0' ? 0 : 1;
                if (pre == '*') {
                    if (c >= '0' && c <= '6') c2 = 2;
                    else c2 = 1;
                } else if (pre == '1') c2 = 1;
                else if (pre == '2') c2 = (c >= '0' && c <= '6') ? 1 : 0;
            }
            dp[i + 1] = (c1 * dp[i] % MOD + c2 * dp[i - 1] % MOD) % MOD;
            pre = c;
        }
        return (int) dp[n];
    }
}
