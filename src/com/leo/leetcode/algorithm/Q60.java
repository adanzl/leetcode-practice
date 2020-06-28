package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
 * 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * 给定 n 和 k，返回第 k 个排列。
 * 说明：
 * 给定 n 的范围是 [1, 9]。
 * 给定 k 的范围是[1,  n!]。
 * 链接：https://leetcode-cn.com/problems/permutation-sequence
 */
public class Q60 {
    public static void main(String[] args) {
        System.out.println(new Q60().getPermutation(3, 3)); // "213"
        System.out.println(new Q60().getPermutation(4, 9)); // "2314"
    }

    public String getPermutation(int n, int k) {
        List<Character> charList = new LinkedList<>();
        for (char i = '1'; i < n + '1'; i++) charList.add(i);
        char[] out = new char[n];
        int index = 0;
        int[] fac = new int[]{0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800};
        --k;
        while (k > 0) {
            int i = k / fac[n - 1];
            out[index++] = charList.get(i);
            charList.remove(i);
            k %= fac[n - 1];
            --n;
        }
        for (Character character : charList) out[index++] = character;
        return new String(out);
    }
}
