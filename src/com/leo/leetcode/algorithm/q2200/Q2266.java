package com.leo.leetcode.algorithm.q2200;

/**
 * Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。
 * 为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。
 * 1、比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
 * 2、注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
 * 但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。
 * 1、比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
 * 给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。
 * 由于答案可能很大，将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= pressedKeys.length <= 10^5
 * 2、pressedKeys 只包含数字 '2' 到 '9' 。
 * 链接：https://leetcode-cn.com/problems/count-number-of-texts
 */
public class Q2266 {

    public static void main(String[] args) {
        // 1568
        System.out.println(new Q2266().countTexts("4444799995555888"));
        // 29
        System.out.println(new Q2266().countTexts("999999"));
        // 82876089
        System.out.println(new Q2266().countTexts("222222222222222222222222222222222222"));
        // 8
        System.out.println(new Q2266().countTexts("9999"));
        // 4
        System.out.println(new Q2266().countTexts("222"));
        // 8
        System.out.println(new Q2266().countTexts("22233"));
        // 7
        System.out.println(new Q2266().countTexts("2222"));
    }

    // 利用斐波那契额数列求划分的可能性
    public int countTexts(String pressedKeys) {
        char[] str = pressedKeys.toCharArray();
        int count = 1, n = str.length, MOD = 1_000_000_007, LEN = 1000001;
        long[] dp3 = new long[LEN], dp4 = new long[LEN];
        dp3[0] = dp4[0] = 1;
        dp3[1] = dp4[1] = 1;
        dp3[2] = dp4[2] = 2;
        dp3[3] = dp4[3] = 4;
        for (int i = 4; i < LEN; i++) {
            dp3[i] = (dp3[i - 1] + dp3[i - 2] + dp3[i - 3]) % MOD;
            dp4[i] = (dp4[i - 1] + dp4[i - 2] + dp4[i - 3] + dp4[i - 4]) % MOD;
        }
        char c = str[0];
        long ret = 1;
        for (int i = 1; i < n; i++) {
            if (str[i] == c) count++;
            else {
                long[] dp = (c == '7' || c == '9') ? dp4 : dp3;
                ret = (ret * dp[count]) % MOD;
                c = str[i];
                count = 1;
            }
        }
        long[] dp = (c == '7' || c == '9') ? dp4 : dp3;
        ret = (ret * dp[count]) % MOD;
        return (int) ret;
    }

}
