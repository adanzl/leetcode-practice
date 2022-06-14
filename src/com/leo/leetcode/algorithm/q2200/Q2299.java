package com.leo.leetcode.algorithm.q2200;


import java.util.HashSet;
import java.util.Set;

/**
 * 如果一个密码满足以下所有条件，我们称它是一个 强 密码：
 * 1、它有至少 8 个字符。
 * 2、至少包含 一个小写英文 字母。
 * 3、至少包含 一个大写英文 字母。
 * 4、至少包含 一个数字 。
 * 5、至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
 * 6、它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。
 * 7、给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。
 * 提示：
 * 1、1 <= password.length <= 100
 * 2、password 包含字母，数字和 "!@#$%^&*()-+" 这些特殊字符。
 * 链接：https://leetcode.cn/problems/strong-password-checker-ii
 */
public class Q2299 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2299().strongPasswordCheckerII("IloveLe3tcode!"));
        // false
        System.out.println(new Q2299().strongPasswordCheckerII("Me+You--IsMyDream"));
        // false
        System.out.println(new Q2299().strongPasswordCheckerII("1aB!"));
    }

    public boolean strongPasswordCheckerII(String password) {
        if (password.length() < 8) return false;
        boolean bLow = false, bUpper = false, bDigit = false, bSpecial = false;
        Set<Character> sp = new HashSet<>();
        for (char c : "!@#$%^&*()-+".toCharArray()) sp.add(c);
        char pre = ' ';
        for (char c : password.toCharArray()) {
            if (pre == c) return false;
            if (c >= '0' && c <= '9') bDigit = true;
            if (c >= 'a' && c <= 'z') bLow = true;
            if (c >= 'A' && c <= 'Z') bUpper = true;
            if (sp.contains(c)) bSpecial = true;
            pre = c;
        }
        return bLow && bUpper && bDigit && bSpecial;
    }
}
