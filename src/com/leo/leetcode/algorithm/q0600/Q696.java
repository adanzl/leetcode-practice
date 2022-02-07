package com.leo.leetcode.algorithm.q0600;

/**
 * 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
 * 重复出现的子串要计算它们出现的次数。
 * 注意：
 *  s.length 在1到50,000之间。
 *  s 只包含“0”或“1”字符。
 * 链接：https://leetcode-cn.com/problems/count-binary-substrings
 */
public class Q696 {

    public static void main(String[] args) {
        System.out.println(new Q696().countBinarySubstrings("00110011")); // 6
        System.out.println(new Q696().countBinarySubstrings("10101")); // 4
        System.out.println(new Q696().countBinarySubstrings("10")); // 1
        System.out.println(new Q696().countBinarySubstrings("00")); // 0
        System.out.println(new Q696().countBinarySubstrings("")); // 0
    }

    public int countBinarySubstrings(String s) {
        if (s.length() <= 1) return 0;
        char[] str = s.toCharArray();
        int index = 1, count = 0;
        while (index < str.length) {
            if (str[index - 1] != str[index]) {
                ++count;
                int offset = 1;
                while (index - 1 - offset >= 0 && index + offset < str.length && str[index + offset] == str[index + offset - 1]
                        && str[index - 1 - offset] == str[index - 1 - offset + 1]) {
                    ++offset;
                    ++count;
                }
            }
            ++index;
        }
        return count;
    }
}