package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
 * <p>
 * 提示：
 * 1、S 的长度不超过12。
 * 2、S 仅由数字和字母组成。
 * 链接：https://leetcode-cn.com/problems/letter-case-permutation/
 */
public class Q784 {

    public static void main(String[] args) {
        // ["a1b2", "a1B2", "A1b2", "A1B2"]
        System.out.println(new Q784().letterCasePermutation("a1b2"));
        // ["3z4", "3Z4"]
        System.out.println(new Q784().letterCasePermutation("3z4"));
        // ["12345"]
        System.out.println(new Q784().letterCasePermutation("12345"));
        //
        System.out.println(new Q784().letterCasePermutation("a1b2"));
    }

    List<String> ret = new ArrayList<>();

    public List<String> letterCasePermutation(String s) {
        func(s.toCharArray(), 0);
        return ret;
    }

    void func(char[] s, int i) {
        if (i == s.length) {
            ret.add(new String(s));
            return;
        }
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            char[] str = Arrays.copyOf(s, s.length);
            str[i] = (char) (c - 'a' + 'A');
            func(str, i + 1);
            func(s, i + 1);
        } else if (c >= 'A' && c <= 'Z') {
            char[] str = Arrays.copyOf(s, s.length);
            str[i] = (char) (c - 'A' + 'a');
            func(str, i + 1);
            func(s, i + 1);
        } else {
            func(s, i + 1);
        }
    }
}
