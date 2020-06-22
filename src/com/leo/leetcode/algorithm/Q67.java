package com.leo.leetcode.algorithm;

/**
 * 给你两个二进制字符串，返回它们的和（用二进制表示）。
 * 输入为 非空 字符串且只包含数字 1 和 0。
 * 链接：https://leetcode-cn.com/problems/add-binary
 */
public class Q67 {
    public static void main(String[] args) {
        System.out.println(new Q67().addBinary("11", "1")); // "100"
        System.out.println(new Q67().addBinary("0", "0")); // "0"
        System.out.println(new Q67().addBinary("10", "1")); // "11"
        System.out.println(new Q67().addBinary("1010", "1011")); // "10101"
    }

    public String addBinary(String a, String b) {
        int flag = 0;
        int index = 0, l1 = a.length(), l2 = b.length(), l = Math.max(l1, l2) + 1;
        char[] str = new char[l];
        while (index < l1 || index < l2) {
            int c1 = index < l1 ? a.charAt(l1 - 1 - index) - '0' : 0;
            int c2 = index < l2 ? b.charAt(l2 - 1 - index) - '0' : 0;
            int v = flag + c1 + c2;
            flag = v >> 1;
            str[l - 1 - index++] = (char) ((v & 0x1) + '0');
        }
        if (flag != 0) str[0] = (char) (flag + '0');
        return flag == 0 ? new String(str, 1, l - 1) : new String(str, 0, l);
    }
}
