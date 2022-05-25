package com.leo.leetcode.algorithm.q0400;

/**
 * 把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：
 * "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." .
 * 现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。
 * 提示:
 * 1、1 <= p.length <= 10^5
 * 2、p 由小写英文字母构成
 * 链接：https://leetcode.cn/problems/unique-substrings-in-wraparound-string
 */
public class Q467 {

    public static void main(String[] args) {
        // 339
        System.out.println(new Q467().findSubstringInWrapRoundString("cdefghefghijklmnopqrstuvwxmnijklmnopqrstuvbcdefghijklmnopqrstuvwabcddefghijklfghijklmabcdefghijklmnopqrstuvwxymnopqrstuvwxyz"));
        // 11
        System.out.println(new Q467().findSubstringInWrapRoundString("nihptuavvw"));
        // 6
        System.out.println(new Q467().findSubstringInWrapRoundString("zaba"));
        // 2
        System.out.println(new Q467().findSubstringInWrapRoundString("cac"));
        // 351
        System.out.println(new Q467().findSubstringInWrapRoundString("abcdefghijklmnopqrstuvwxyz"));
        // 377
        System.out.println(new Q467().findSubstringInWrapRoundString("abcdefghijklmnopqrstuvwxyza"));
        // 6
        System.out.println(new Q467().findSubstringInWrapRoundString("zab"));
        // 1
        System.out.println(new Q467().findSubstringInWrapRoundString("a"));
    }

    public int findSubstringInWrapRoundString(String p) {
        char[] str = p.toCharArray();
        int count = 1, ret = 0;
        int[] map = new int[26];
        for (int i = 0; i < str.length; i++) {
            if (i != 0 && (str[i] - 'a') == (str[i - 1] + 1 - 'a') % 26) count++;
            else count = 1;
            map[str[i] - 'a'] = Math.max(map[str[i] - 'a'], count);
        }
        for (int c : map) ret += c;
        return ret;
    }

}
