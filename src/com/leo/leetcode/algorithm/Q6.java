package com.leo.leetcode.algorithm;

public class Q6 {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        StringBuilder sbArr[] = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            sbArr[i] = new StringBuilder();
        }
        int group = (2 * numRows - 2);
        for (int i = 0; i < s.length(); i++) {
            int index = i % group;
            if (index >= numRows) {
                index = group - index;
            }
            StringBuilder sb = sbArr[index];
            sb.append(s.charAt(i));
        }
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            ret.append(sbArr[i]);
        }
        return ret.toString();
    }
}
