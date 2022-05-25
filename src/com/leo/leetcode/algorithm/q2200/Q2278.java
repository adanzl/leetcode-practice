package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、s 由小写英文字母组成
 * 3、letter 是一个小写英文字母
 * 链接：https://leetcode.cn/problems/percentage-of-letter-in-string/
 */
public class Q2278 {

    public static void main(String[] args) {
        // 33
        System.out.println(new Q2278().percentageLetter("foobar", 'o'));
        // 0
        System.out.println(new Q2278().percentageLetter("foo", 'z'));
    }

    public int percentageLetter(String s, char letter) {
        char[] str = s.toCharArray();
        int count = 0;
        for (char c : str) {
            if (c == letter) count++;
        }
        return count * 100 / str.length;
    }

}
