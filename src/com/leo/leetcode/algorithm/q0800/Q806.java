package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，
 * 那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位，
 * widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。
 * 现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
 * 链接：https://leetcode-cn.com/problems/number-of-lines-to-write-string
 */
public class Q806 {

    public static void main(String[] args) {
        // [3, 60]
        System.out.println(Arrays.toString(new Q806().numberOfLines(
                stringToIntegerArray("[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]")
                , "abcdefghijklmnopqrstuvwxyz")));
        // [2, 4]
        System.out.println(Arrays.toString(new Q806().numberOfLines(
                stringToIntegerArray("[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]")
                , "bbbcccdddaaa")));
    }

    public int[] numberOfLines(int[] widths, String s) {
        int line = 1, width = 0;
        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 'a';
            int w = widths[index];
            if (width + w > 100) {
                line++;
                width = w;
            } else {
                width += w;
            }
        }
        return new int[]{line, width};
    }
}
