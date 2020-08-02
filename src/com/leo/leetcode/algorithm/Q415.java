package com.leo.leetcode.algorithm;

/**
 * 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
 * 注意：
 * num1 和num2 都只包含数字 0-9.
 * num1 和num2 的长度都小于 5100.
 * num1 和num2 都不包含任何前导零。
 * 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
 * 链接：https://leetcode-cn.com/problems/add-strings
 */
class Q415 {

    public static void main(String[] args) {
        System.out.println(new Q415().addStrings("123", "4356")); // 4479
        System.out.println(new Q415().addStrings("0", "10")); // 10
        System.out.println(new Q415().addStrings("60", "60")); // 120
        System.out.println(new Q415().addStrings("0", "0")); // 0
    }

    public String addStrings(String num1, String num2) {
        char[] out = new char[5101];
        int len = out.length, l1 = num1.length(), l2 = num2.length();
        int index = 0, ext = 0;
        while (index < l1 || index < l2 || ext != 0) {
            int v = ext;
            if (index < l1) v += num1.charAt(l1 - 1 - index) - '0';
            if (index < l2) v += num2.charAt(l2 - 1 - index) - '0';
            ext = v / 10;
            out[len - 1 - index] = (char) (v % 10 + '0');
            ++index;
        }
        return new String(out, len - index, index);
    }
}