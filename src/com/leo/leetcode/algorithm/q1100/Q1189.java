package com.leo.leetcode.algorithm.q1100;

/**
 * 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
 * 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
 * 提示：
 * 1、1 <= text.length <= 10^4
 * 2、text 全部由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/maximum-number-of-balloons
 */
public class Q1189 {
    public static void main(String[] args) {
        // 1
        System.out.println(new Q1189().maxNumberOfBalloons("nlaebolko"));
        // 2
        System.out.println(new Q1189().maxNumberOfBalloons("loonbalxballpoon"));
        // 0
        System.out.println(new Q1189().maxNumberOfBalloons("leetcode"));
        // 0
        System.out.println(new Q1189().maxNumberOfBalloons("balon"));

    }

    public int maxNumberOfBalloons(String text) {
        char[] c = new char[]{'b', 'a', 'l', 'o', 'n'};
        int[] s = new int[]{1, 1, 2, 2, 1};
        int[] count = new int[s.length];
        int ret = Integer.MAX_VALUE;
        for (char ch : text.toCharArray()) {
            for (int i = 0; i < c.length; i++) {
                if (c[i] == ch) {
                    count[i]++;
                    break;
                }
            }
        }
        for (int i = 0; i < count.length; i++) {
            ret = Math.min(ret, count[i] / s[i]);
        }
        return ret;
    }
}
