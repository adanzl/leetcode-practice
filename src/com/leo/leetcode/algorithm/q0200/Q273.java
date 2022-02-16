package com.leo.leetcode.algorithm.q0200;

/**
 * 将非负整数 num 转换为其对应的英文表示。
 * 提示：0 <= num <= 2^31 - 1
 * 链接：https://leetcode-cn.com/problems/integer-to-english-words/
 */
public class Q273 {

    public static void main(String[] args) {
        // "Zero"
        System.out.println(new Q273().numberToWords(0));
        // "One"
        System.out.println(new Q273().numberToWords(1));
        // "One Hundred Thousand Five"
        System.out.println(new Q273().numberToWords(100005));
        // "Twelve Thousand Three Hundred Forty Five"
        System.out.println(new Q273().numberToWords(12345));
        // One Thousand Five
        System.out.println(new Q273().numberToWords(1005));
        // Ten Thousand Five
        System.out.println(new Q273().numberToWords(10005));
        // "One Hundred Twenty Three"
        System.out.println(new Q273().numberToWords(123));
        // "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        System.out.println(new Q273().numberToWords(1234567));
        // "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        System.out.println(new Q273().numberToWords(1234567891));
        // "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
        System.out.println(new Q273().numberToWords(2147483647));
    }

    String[] unit = new String[]{"", " Thousand", " Million", " Billion"};
    String[] num_s = new String[]{"", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten",
            " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen", " Twenty"};
    String[] num_ten = new String[]{" Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety", " Hundred"};

    public String numberToWords(int num) {
        if(num == 0) return "Zero";
        StringBuilder out = new StringBuilder();
        int[] parts = new int[4];
        for (int i = 0; i < 4; i++) {
            parts[i] = num % 1000;
            num /= 1000;
        }
        for (int i = 3; i >= 0; i--) {
            if (func_3(parts[i], out) != 0) out.append(unit[i]);
        }
        return out.substring(1);
    }

    int func_3(int num, StringBuilder out) {
        int h = num / 100;
        out.append(num_s[h]);
        if (h != 0) out.append(num_ten[8]);
        func_2(num % 100, out);
        return num;
    }

    void func_2(int num, StringBuilder out) {
        int t = num / 10, n = num % 10;
        if (num < 20) out.append(num_s[num]);
        else {
            out.append(num_ten[t - 2]);
            out.append(num_s[n]);
        }
    }

}
