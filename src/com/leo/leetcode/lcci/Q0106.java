package com.leo.leetcode.lcci;

public class Q0106 {
    public static void main(String[] args) {
        System.out.println(new Q0106().compressString("aabcccccaaa")); // a2b1c5a3
        System.out.println(new Q0106().compressString("abbccd")); // abbccd
    }

    public String compressString(String S) {
        char[] str = S.toCharArray();
        if (str.length <= 1) return S;
        char c, pre = str[0];
        int count = 1;
        StringBuilder out = new StringBuilder();
        for (int i = 1; i < str.length; i++) {
            c = str[i];
            if (c == pre) {
                count++;
            } else {
                out.append(pre).append(count);
                count = 1;
            }
            pre = c;
        }
        out.append(pre).append(count);
        return out.length() < S.length() ? out.toString() : S;
    }
}
