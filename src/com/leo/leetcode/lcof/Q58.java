package com.leo.leetcode.lcof;

public class Q58 {

    public static void main(String[] args) {
        new Q58().TestOJ();
    }

    public void TestOJ() {
        System.out.println(reverseWords("   one.   +two three?   ~four   !five- ")); // "!five- ~four three? +two one."
        System.out.println(reverseWords("the sky is blue")); // "blue is sky the"
        System.out.println(reverseWords("  hello world!  ")); // "world! hello"
        System.out.println(reverseWords("a good   example")); // "example good a"
    }

    public String reverseWords(String s) {
        char[] str = s.trim().toCharArray();
        if (str.length <= 0)
            return new String(str);
        int l = 0, flag = -1;
        for (int i = 0; i < str.length; i++) {
            if (str[i] == ' ') {
                if (str[i - 1] == ' ') {
                    continue;
                }

                reverse(str, flag + 1, l - 1);
                flag = l;
            }
            str[l++] = str[i];
        }
        reverse(str, flag + 1, l - 1);
        reverse(str, 0, l - 1);
        return new String(str, 0, l);
    }

    void reverse(char[] str, int s, int e) {
        int m = (e - s + 1) >> 1;
        for (int i = 0; i < m; i++) {
            char c = str[s + i];
            str[s + i] = str[e - i];
            str[e - i] = c;
        }
    }
}
