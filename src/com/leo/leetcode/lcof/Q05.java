package com.leo.leetcode.lcof;

public class Q05 {

    public static void main(String[] args) {
        System.out.println(new Q05().replaceSpace("We are happy.")); // "We%20are%20happy."
    }

    public String replaceSpace(String s) {
        StringBuilder out = new StringBuilder();
        char[] str = s.toCharArray();
        for (char c : str) {
            if (c == ' ') out.append("%20");
            else out.append(c);

        }
        return out.toString();
    }
}
