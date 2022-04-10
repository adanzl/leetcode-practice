package com.leo.leetcode.algorithm.q0800;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如:
 * 1、'a' 对应 ".-" ，
 * 2、'b' 对应 "-..." ，
 * 3、'c' 对应 "-.-." ，以此类推。
 * 为了方便，所有 26 个英文字母的摩尔斯密码表如下：
 * [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
 * 给你一个字符串数组 words ，每个单词可以写成每个字母对应摩尔斯密码的组合。
 * 例如，"cab" 可以写成 "-.-..--..." ，(即 "-.-." + ".-" + "-..." 字符串的结合)。我们将这样一个连接过程称作 单词翻译 。
 * 对 words 中所有单词进行单词翻译，返回不同 单词翻译 的数量。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 12
 * 3、words[i] 由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/unique-morse-code-words
 */
public class Q804 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q804().uniqueMorseRepresentations(stringToStringArray("[\"gin\", \"zen\", \"gig\", \"msg\"]")));
        // 1
        System.out.println(new Q804().uniqueMorseRepresentations(stringToStringArray("[\"a\"]")));
    }

    public static final String[] MORSE = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."};

    public int uniqueMorseRepresentations(String[] words) {
        Set<String> seen = new HashSet<>();
        for (String word : words) {
            StringBuilder code = new StringBuilder();
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                code.append(MORSE[c - 'a']);
            }
            seen.add(code.toString());
        }
        return seen.size();
    }
}
