package com.leo.leetcode.algorithm.q6000;

import java.util.Arrays;

/**
 * 给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。
 * 你不必使用 s 中的全部字符。
 * 返回 字典序最大的 repeatLimitedString 。
 * 如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。
 * 如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。
 * 提示：
 * 1、1 <= repeatLimit <= s.length <= 10^5
 * 2、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/construct-string-with-repeat-limit
 */
public class Q2182 {

    public static void main(String[] args) {
        // zzcccac
        System.out.println(new Q2182().repeatLimitedString("cczazcc", 3));
        // bbabaa
        System.out.println(new Q2182().repeatLimitedString("aababab", 2));
    }

    public String repeatLimitedString(String s, int repeatLimit) {
        char[] str = s.toCharArray();
        int n = str.length, cnt = 1, maxCnt = 0;
        char preChar = ' ', maxChar = ' ';
        Arrays.sort(str);
        StringBuilder sb = new StringBuilder();
        for (int i = n - 1; i >= 0; i--) {
            char c = str[i];
            if (maxCnt > 0) {
                if (c != maxChar) {
                    sb.append(c);
                    int len = Math.min(maxCnt, repeatLimit);
                    for (int j = 0; j < len; j++) sb.append(maxChar);
                    maxCnt -= len;
                    preChar = maxChar;
                    cnt = len;
                } else {
                    maxCnt++;
                }
            } else {
                if (c != preChar) {
                    sb.append(c);
                    preChar = c;
                    cnt = 1;
                } else {
                    if (cnt == repeatLimit) {
                        maxChar = c;
                        maxCnt = 1;
                    } else {
                        sb.append(c);
                        cnt++;
                    }
                }
            }
        }
        return sb.toString();
    }
}
