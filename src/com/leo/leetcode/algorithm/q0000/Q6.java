package com.leo.leetcode.algorithm.q0000;

/**
 * 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
 * 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
 * L   C   I   R
 * E T O E S I I G
 * E   D   H   N
 * 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
 * 请你实现这个将字符串进行指定行数变换的函数：
 * string convert(string s, int numRows);
 * 链接：https://leetcode-cn.com/problems/zigzag-conversion
 */
public class Q6 {
    public static void main(String[] args) {
        System.out.println(new Q6().convert("LEETCODEISHIRING", 3)); // "LCIRETOESIIGEDHN"
        System.out.println(new Q6().convert("LEETCODEISHIRING", 4)); // "LDREOEIIECIHNTSG"
    }

    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        StringBuilder[] sbArr = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) sbArr[i] = new StringBuilder();
        int group = 2 * numRows - 2;
        for (int i = 0; i < s.length(); i++) {
            int index = i % group;
            if (index >= numRows) index = group - index;
            StringBuilder sb = sbArr[index];
            sb.append(s.charAt(i));
        }
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < numRows; i++) ret.append(sbArr[i]);
        return ret.toString();
    }
}
