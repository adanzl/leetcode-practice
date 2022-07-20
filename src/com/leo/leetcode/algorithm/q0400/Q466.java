package com.leo.leetcode.algorithm.q0400;

/**
 * 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。
 * 例如，str == ["abc", 3] =="abcabcabc" 。
 * 如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。
 * 例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。
 * 现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, n2] 。
 * 请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。
 * 提示：
 * 1、1 <= s1.length, s2.length <= 100
 * 2、s1 和 s2 由小写英文字母组成
 * 3、1 <= n1, n2 <= 10^6
 * 链接：https://leetcode.cn/problems/count-the-repetitions
 */
public class Q466 {

    public static void main(String[] args) {
        // 9
        System.out.println(new Q466().getMaxRepetitions("aaa", 3, "a", 1));
        // 4
        System.out.println(new Q466().getMaxRepetitions("aaa", 3, "aa", 1));
        // 2
        System.out.println(new Q466().getMaxRepetitions("acb", 4, "ab", 2));
        // 1
        System.out.println(new Q466().getMaxRepetitions1("acb", 1, "acb", 1));
    }

    // 双指针
    public int getMaxRepetitions1(String s1, int n1, String s2, int n2) {
        char[] str1 = s1.toCharArray(), str2 = s2.toCharArray();
        int ret = 0, i1 = 0, size = str1.length * n1, i2 = 0;
        while (i1 < size) {
            char c = str2[i2];
            while (i1 < size && str1[i1 % str1.length] != c) i1++;
            if (i1 < size && str1[i1 % str1.length] == c) {
                i1++;
                i2++;
                if (i2 == str2.length) {
                    ret++;
                    i2 = 0;
                }
            }
        }
        return ret / n2;
    }

    // DP 状态优化
    public int getMaxRepetitions(String s1, int n1, String s2, int n2) {
        char[] str1 = s1.toCharArray(), str2 = s2.toCharArray();
        int ret = 0, count = 0, offset = 0;
        int[][] dp = new int[str1.length][];
        while (count < n1) {
            if (dp[offset] == null) {
                int i1 = offset, count1 = 0;
                for (char c : str2) {
                    int len = 0;
                    while (len < str1.length && str1[i1] != c) {
                        i1++;
                        if (i1 >= str1.length) count1++;
                        i1 %= str1.length;
                        len++;
                    }
                    if (str1[i1] != c) return 0;
                    i1++;
                    if (i1 >= str1.length) count1++;
                    i1 %= str1.length;
                }
                dp[offset] = new int[]{count1, i1};
            }
            int[] cur = dp[offset];
            count += cur[0];
            offset = cur[1];
            ret++;
        }
        if (offset != 0) ret--;
        return ret / n2;
    }


}
