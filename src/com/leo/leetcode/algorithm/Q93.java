package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
 * 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
 * 链接：https://leetcode-cn.com/problems/restore-ip-addresses
 */
public class Q93 {
    public static void main(String[] args) {
        System.out.println(new Q93().restoreIpAddresses("25525511135")); // ["1.1.1.1"]
        System.out.println(new Q93().restoreIpAddresses("1111")); // ["1.1.1.1"]
        System.out.println(new Q93().restoreIpAddresses("25525511135")); // ["255.255.11.135", "255.255.111.35"]
        System.out.println(new Q93().restoreIpAddresses("0000")); // ["0.0.0.0"]
    }

    public List<String> restoreIpAddresses(String s) {
        List<String> out = new ArrayList<>();
        build(s.toCharArray(), 0, 1, new char[s.length() + 3], 0, out);
        return out;
    }

    void build(char[] str, int l, int r, char[] ans, int pCount, List<String> out) {
        if (pCount > 3) return;
        if (l == str.length) {
            if (pCount == 3 && ans[ans.length - 1] != '.')
                out.add(new String(ans));
            return;
        }
        int n = getNum(str, l, r);
        while (n >= 0) {
            ans[r - 1 + pCount] = str[r - 1];
            boolean bDot = r + pCount < ans.length;
            if (bDot) ans[r + pCount] = '.';
            build(str, r, r + 1, ans, bDot ? pCount + 1 : pCount, out);
            r++;
            n = getNum(str, l, r);
        }
    }

    int getNum(char[] str, int l, int r) {
        if (r > str.length) return -1;
        if (str[l] == '0' && l != r - 1) return -1;
        int v = Integer.parseInt(new String(str, l, r - l));
        if (v >= 0 && v <= 255) return v;
        return -1;
    }
}
