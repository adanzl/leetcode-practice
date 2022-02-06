package com.leo.leetcode.algorithm.q1400;

import java.util.Arrays;

/**
 * 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
 * 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
 * s 是一个尽可能长的快乐字符串。
 * s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
 * s 中只含有 'a'、'b' 、'c' 三种字母。
 * 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
 * 提示：
 * 1、0 <= a, b, c <= 100
 * 2、a + b + c > 0
 * 链接：https://leetcode-cn.com/problems/longest-happy-string
 */
public class Q1405 {
    public static void main(String[] args) {
        // ccaccbcc
        System.out.println(new Q1405().longestDiverseString(1, 1, 7));
        // aabbc
        System.out.println(new Q1405().longestDiverseString(2, 2, 1));
        // aabaa
        System.out.println(new Q1405().longestDiverseString(7, 1, 0));
        // ""
        System.out.println(new Q1405().longestDiverseString(0, 0, 0));
        // aa
        System.out.println(new Q1405().longestDiverseString(7, 0, 0));
    }

    public String longestDiverseString(int a, int b, int c) {
        StringBuilder sb = new StringBuilder();
        Char[] charArr = new Char[]{new Char('a', a), new Char('b', b), new Char('c', c)};
        Char lastChar = null;
        int lastCount = 0;
        while (true) {
            Arrays.sort(charArr, (o1, o2) -> o2.count - o1.count);
            Char theChar;
            if (lastCount < 2 || charArr[0] != lastChar) theChar = charArr[0];
            else theChar = charArr[1];
            if (theChar.count <= 0) break;
            --theChar.count;
            sb.append(theChar.c);
            if (lastChar == theChar) {
                ++lastCount;
            } else {
                lastChar = theChar;
                lastCount = 1;
            }
        }
        return sb.toString();
    }

    static class Char {
        char c;
        int count;

        Char(char c, int count) {
            this.c = c;
            this.count = count;
        }
    }

}
