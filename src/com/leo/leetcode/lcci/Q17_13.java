package com.leo.leetcode.lcci;

import com.leo.utils.LCUtil;
import com.leo.utils.TestCase;

/**
 * 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
 * 像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
 * 在处理标点符号和大小写之前，你得先把它断成词语。
 * 当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
 * 假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
 * 提示：
 * 1、0 <= len(sentence) <= 1000
 * 2、dictionary中总字符数不超过 150000。
 * 3、你可以认为dictionary和sentence中只包含小写字母。
 * 链接：https://leetcode-cn.com/problems/re-space-lcci
 */
public class Q17_13 {

    public static void main(String[] args) {
        final TestCase tc1 = new TestCase("resources/lcci/Q1713/Case003");
        System.out.println(new Q17_13().reSpace(LCUtil.stringToStringArray(tc1.getData(0)), tc1.getData(1))); // 7
        final TestCase tc2 = new TestCase("resources/lcci/Q1713/Case002");
        System.out.println(new Q17_13().reSpace(LCUtil.stringToStringArray(tc2.getData(0)), tc2.getData(1))); // 31
        final TestCase tc3 = new TestCase("resources/lcci/Q1713/Case003");
        System.out.println(new Q17_13().reSpace(LCUtil.stringToStringArray(tc3.getData(0)), tc3.getData(1))); // 7
    }

    public int reSpace(String[] dictionary, String sentence) {
        // build tree
        CNode root = new CNode(' ');
        for (String str : dictionary) {
            CNode node = root;
            for (int i = str.length() - 1; i >= 0; i--) {
                char c = str.charAt(i);
                if (node.next[c - 'a'] == null) node.next[c - 'a'] = new CNode(c);
                node = node.next[c - 'a'];
            }
            node.end = true; // EOW
        }
        char[] sen = sentence.toCharArray();
        int[] marks = new int[sen.length + 1];
        for (int i = 0; i < sen.length; i++) {
            marks[i + 1] = marks[i] + 1;
            for (int j = i; j >= 0; j--) {
                int ret = fitTree(sen, j, i, root);
                if (ret == -1) break;
                if (ret == 1) marks[i + 1] = Math.min(marks[i + 1], marks[j]);
            }
        }
        return marks[sen.length];
    }

    int fitTree(char[] str, int l, int r, CNode root) {
        CNode node = root;
        for (int i = r; i >= l; i--) {
            node = node.next[str[i] - 'a'];
            if (node == null) return -1; // error char
        }
        return node.end ? 1 : 0; // not EOW
    }

    static class CNode {

        char c;

        boolean end = false;

        CNode[] next = new CNode[26];

        CNode(char c) {
            this.c = c;
        }
    }
}
