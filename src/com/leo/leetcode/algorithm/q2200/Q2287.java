package com.leo.leetcode.algorithm.q2200;

/**
 * 给你两个下标从 0 开始的字符串 s 和 target 。你可以从 s 取出一些字符并将其重排，得到若干新的字符串。
 * 从 s 中取出字符并重新排列，返回可以形成 target 的 最大 副本数。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、1 <= target.length <= 10
 * 3、s 和 target 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/rearrange-characters-to-make-target-string
 */
public class Q2287 {
    public static void main(String[] args) {
        // 2
        System.out.println(new Q2287().rearrangeCharacters("ilovecodingonleetcode", "code"));
        // 1
        System.out.println(new Q2287().rearrangeCharacters("abcba", "abc"));
        // 1
        System.out.println(new Q2287().rearrangeCharacters("abbaccaddaeea", "aaaaa"));
    }


    public int rearrangeCharacters(String s, String target) {
        int ret = Integer.MAX_VALUE;
        int[] cCountStr = new int[26], cCountTarget = new int[26];
        for (char c : s.toCharArray()) cCountStr[c - 'a']++;
        for (char c : target.toCharArray()) cCountTarget[c - 'a']++;
        for (int i = 0; i < 26; i++) {
            if (cCountTarget[i] == 0) continue;
            ret = Math.min(ret, cCountStr[i] / cCountTarget[i]);
        }
        return ret;
    }
}
