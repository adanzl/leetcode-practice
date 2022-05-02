package com.leo.leetcode.algorithm.q6000;

/**
 * 给你一个表示某个正整数的字符串 number 和一个字符 digit 。
 * 从 number 中 恰好 移除 一个 等于 digit 的字符后，找出并返回按 十进制 表示 最大 的结果字符串。生成的测试用例满足 digit 在 number 中出现至少一次。
 * 提示：
 * 1、2 <= number.length <= 100
 * 2、number 由数字 '1' 到 '9' 组成
 * 3、digit 是 '1' 到 '9' 中的一个数字
 * 4、digit 在 number 中出现至少一次
 * 链接：https://leetcode-cn.com/problems/remove-digit-from-number-to-maximize-result
 */
public class Q2259 {

    public static void main(String[] args) {
        // 12
        System.out.println(new Q2259().removeDigit("123", 'c'));
        // 231
        System.out.println(new Q2259().removeDigit("1231", '1'));
        // 51
        System.out.println(new Q2259().removeDigit("551", '5'));
    }

    public String removeDigit(String number, char digit) {

        char[] str = number.toCharArray();
        String max = "";
        for (int i = 0; i < str.length; i++) {
            if (str[i] == digit) {
                String newStr = number.substring(0, i) + number.substring(i + 1, str.length);
                if (newStr.compareTo(max) > 0) max = newStr;
            }
        }
        return max;
    }
}
