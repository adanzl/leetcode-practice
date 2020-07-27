package com.leo.leetcode.lcci;

import java.util.Arrays;

import com.leo.utils.LCUtil;
import com.leo.utils.TestCase;

/**
 * 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
 * 像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
 * 在处理标点符号和大小写之前，你得先把它断成词语。
 * 当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
 * 假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
 * 提示：
 * 0 <= len(sentence) <= 1000 dictionary中总字符数不超过 150000。
 * 你可以认为dictionary和sentence中只包含小写字母。
 * 链接：https://leetcode-cn.com/problems/re-space-lcci
 */
public class Q1713 {

    // TODO
    public static void main(String[] args) {
        final TestCase tc1 = new TestCase("resources/Q1713/Case001");
        System.out.println(new Q1713().reSpace(LCUtil.stringToStringArray(tc1.getData(0)), tc1.getData(1))); // 7
        final TestCase tc2 = new TestCase("resources/Q1713/Case002");
        System.out.println(new Q1713().reSpace(LCUtil.stringToStringArray(tc2.getData(0)), tc2.getData(1))); // 31
        final TestCase tc3 = new TestCase("resources/Q1713/Case003");
        System.out.println(new Q1713().reSpace(LCUtil.stringToStringArray(tc3.getData(0)), tc3.getData(1))); // 7
    }

    public int reSpace(String[] dictionary, String sentence) {
        Arrays.sort(dictionary, ((o1, o2) -> o2.length() - o1.length()));
        boolean[] marks = new boolean[1000];
        int count = 0;
        for (String str : dictionary) {
            for (int i = 0; i < sentence.length();) {
                boolean fit = false;
                for (int j = 0; j < str.length() && i + j < sentence.length(); j++) {
                    if (marks[i + j] || sentence.charAt(i + j) != str.charAt(j)) break;
                    fit = j == str.length() - 1;
                }
                if (fit) {
                    count += str.length();
                    for (int j = 0; j < str.length(); j++)
                        marks[i + j] = true;
                    i += str.length();
                } else {
                    i++;
                }
            }
        }
        return sentence.length() - count;
    }
}
