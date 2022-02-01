package com.leo.leetcode.algorithm.q2000;

/**
 * 给你一个下标从 0 开始的字符串 word 和一个字符 ch 。找出 ch 第一次出现的下标 i ，
 * 反转 word 中从下标 0 开始、直到下标 i 结束（含下标 i ）的那段字符。如果 word 中不存在字符 ch ，则无需进行任何操作。
 * 例如，如果 word = "abcdefd" 且 ch = "d" ，那么你应该 反转 从下标 0 开始、直到下标 3 结束（含下标 3 ）。
 * 结果字符串将会是 "dcbaefd" 。
 * 返回 结果字符串 。
 * 提示：
 * 1、1 <= word.length <= 250
 * 2、word 由小写英文字母组成
 * 3、ch 是一个小写英文字母
 * <p>
 * 链接：https://leetcode-cn.com/problems/reverse-prefix-of-word
 */
public class Q2000 {

    public static void main(String[] args) {
        // dcbaefd
        System.out.println(new Q2000().reversePrefix("abcdefd", 'd'));
        // zxyxxe
        System.out.println(new Q2000().reversePrefix("xyxzxe", 'z'));
        // abcd
        System.out.println(new Q2000().reversePrefix("abcd", 'z'));
    }

    public String reversePrefix(String word, char ch) {
        char[] chars = word.toCharArray();
        int idx = -1;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == ch) {
                idx = i;
                break;
            }
        }
        for (int i = 0; i <= idx >> 1; i++) {
            char t = chars[i];
            chars[i] = chars[idx - i];
            chars[idx - i] = t;
        }
        return String.valueOf(chars);
    }
}
