package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q43 {
    @Test
    public void TestOJ() {
        System.out.println(multiply("9", "9")); // "81"
        System.out.println(multiply("123", "456")); // "56088"
    }

    public String multiply(String num1, String num2) {
        char[] n1 = num1.toCharArray(), n2 = num2.toCharArray();
        int[] result = new int[300];
        int size = -1;
        for (int i = n2.length - 1; i >= 0; i--) {
            size = multi(n1, n2[i], n2.length - 1 - i, result);
        }
        StringBuilder sb = new StringBuilder();
        boolean head = false;
        while (size >= 0) {
            int v = result[size--];
            if (v != 0) head = true;
            if (!head) continue;
            sb.append(v);
        }
        if (!head) return "0";
        return sb.toString();
    }

    int multi(char[] num, char n, int offset, int[] result) {
        int flag = 0;
        int n2 = n - '0';
        for (int i = num.length - 1; i >= 0; i--) {
            int n1 = num[i] - '0';
            int v = n1 * n2 + flag + result[offset + num.length - 1 - i];
            flag = v / 10;
            v %= 10;
            result[offset + num.length - 1 - i] = v;
        }
        int v = result[offset + num.length - 1 + 1] + flag;
        if (v == 0) return offset + num.length - 1;
        result[offset + num.length - 1 + 1] = v % 10;
        if (v > 10) {
            result[offset + num.length - 1 + 1 + 1] = v / 10;
            return offset + num.length - 1 + 1 + 1;
        }
        return offset + num.length - 1 + 1;
    }
}
