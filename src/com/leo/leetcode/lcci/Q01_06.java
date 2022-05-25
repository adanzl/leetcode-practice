package com.leo.leetcode.lcci;

/**
 * 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
 * 比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
 * 提示：字符串长度在[0, 50000]范围内。
 * 链接：https://leetcode.cn/problems/compress-string-lcci
 */
public class Q01_06 {
    public static void main(String[] args) {
        System.out.println(new Q01_06().compressString("aabcccccaaa")); // a2b1c5a3
        System.out.println(new Q01_06().compressString("abbccd")); // abbccd
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
