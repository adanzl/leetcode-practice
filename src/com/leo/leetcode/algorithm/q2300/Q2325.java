package com.leo.leetcode.algorithm.q2300;

/**
 * 给你字符串 key 和 message ，分别表示一个加密密钥和一段加密消息。解密 message 的步骤如下：
 * 1、使用 key 中 26 个英文小写字母第一次出现的顺序作为替换表中的字母 顺序 。
 * 2、将替换表与普通英文字母表对齐，形成对照表。
 * 3、按照对照表 替换 message 中的每个字母。
 * 4、空格 ' ' 保持不变。
 * 例如，key = "happy boy"（实际的加密密钥会包含字母表中每个字母 至少一次），据此，可以得到部分对照表（'h' -> 'a'、'a' -> 'b'、'p' -> 'c'、'y' -> 'd'、'b' -> 'e'、'o' -> 'f'）。
 * 返回解密后的消息。
 * 提示：
 * 1、26 <= key.length <= 2000
 * 2、key 由小写英文字母及 ' ' 组成
 * 3、key 包含英文字母表中每个字符（'a' 到 'z'）至少一次
 * 4、1 <= message.length <= 2000
 * 5、message 由小写英文字母和 ' ' 组成
 * 链接：https://leetcode.cn/problems/decode-the-message
 */
public class Q2325 {

    public static void main(String[] args) {
        // "this is a secret"
        System.out.println(new Q2325().decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"));
        // "the five boxing wizards jump quickly"
        System.out.println(new Q2325().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"));
    }

    public String decodeMessage(String key, String message) {
        char[] chars = new char[26];
        int idx = 0;
        boolean[] marks = new boolean[26];
        for (int i = 0; i < key.length(); i++) {
            char c = key.charAt(i);
            if (c <= 'z' && c >= 'a' && !marks[c - 'a']) {
                chars[c - 'a'] = (char) (idx++ + 'a');
                marks[c - 'a'] = true;
            }
        }
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (c <= 'z' && c >= 'a') ret.append(chars[c - 'a']);
            else ret.append(c);
        }
        return ret.toString();
    }
}
