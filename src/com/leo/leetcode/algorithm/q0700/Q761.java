package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 特殊的二进制序列是具有以下两个性质的二进制序列：
 * 1、0 的数量与 1 的数量相等。
 * 2、二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。
 * 给定一个特殊的二进制序列 S，以字符串形式表示。定义一个操作 为首先选择 S 的两个连续且非空的特殊的子串，然后将它们交换。
 * （两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)
 * 在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？
 * 说明:
 * 1、S 的长度不超过 50。
 * 2、S 保证为一个满足上述定义的特殊 的二进制序列。
 * 链接：https://leetcode.cn/problems/special-binary-string
 */
public class Q761 {

    public static void main(String[] args) {
        // "11100100"
        System.out.println(new Q761().makeLargestSpecial("11011000"));
    }

    public String makeLargestSpecial(String s) {
        int count = 0, pre = 0, n = s.length();
        if (n == 0) return "";
        List<String> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '1') count++;
            else {
                count--;
                if (count == 0) {
                    list.add("1" + makeLargestSpecial(s.substring(pre + 1, i)) + "0");
                    pre = i + 1;
                }
            }
        }
        Collections.sort(list);
        StringBuilder ans = new StringBuilder();
        for (int i = list.size() - 1; i >= 0; i--) ans.append(list.get(i));
        return ans.toString();
    }
}
