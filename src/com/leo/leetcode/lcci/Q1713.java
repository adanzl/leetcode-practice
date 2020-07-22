package com.leo.leetcode.lcci;

import java.util.Arrays;

import com.leo.utils.LCUtil;
import com.leo.utils.TestCase;

/**
 * 
 */
// TODO
public class Q1713 {
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
                    if (marks[i + j] || sentence.charAt(i + j) != str.charAt(j))
                        break;
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
