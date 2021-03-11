package com.leo.leetcode.algorithm.q0300;

/**
 * 给定一个经过编码的字符串，返回它解码后的字符串。
 * 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
 * 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
 * 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
 * <p>
 * 链接：https://leetcode-cn.com/problems/decode-string
 */
public class Q394 {

    public static void main(String[] args) {
        // "aaaabcbc"
        System.out.println(new Q394().decodeString("3[a]a2[bc]"));
        // "accaccacc"
        System.out.println(new Q394().decodeString("3[a2[c]]"));
        // "abcabccdcdcdef"
        System.out.println(new Q394().decodeString("2[abc]3[cd]ef"));
        // "aaabcbc"
        System.out.println(new Q394().decodeString("3[a]2[bc]"));
    }

    private int index;

    public String decodeString(String s) {
        index = 0;
        StringBuilder sb = new StringBuilder();
        while (index < s.length()) {
            sb.append(decode(s));
        }
        return sb.toString();
    }

    private StringBuilder decode(String s) {
        StringBuilder content = new StringBuilder();
        int k;
        if (isNum(s.charAt(index))) {
            int i = 0;
            while (s.charAt(index + i) != '[') i++;
            k = Integer.parseInt(s.substring(index, index + i));
            index += i + 1;

            while (s.charAt(index) != ']') {
                if (isNum(s.charAt(index))) {
                    content.append(decode(s));
                } else {
                    content.append(s.charAt(index));
                    index++;
                }
            }
            index++;
        } else {
            k = 1;
            while (index < s.length() && !isNum(s.charAt(index))) {
                content.append(s.charAt(index));
                index++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            sb.append(content);
        }
        return sb;
    }

    private boolean isNum(char c) {
        return c >= '0' && c <= '9';
    }
}
