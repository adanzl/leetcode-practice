package com.leo.leetcode.algorithm.q1800;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。
 * 同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 removable ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。
 * 请你找出一个整数 k（0 <= k <= removable.length），选出 removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。
 * 整数 k 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。
 * 更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。
 * 返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。
 * 字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。
 * 提示：
 * 1、1 <= p.length <= s.length <= 10^5
 * 2、0 <= removable.length < s.length
 * 3、0 <= removable[i] < s.length
 * 4、p 是 s 的一个 子字符串
 * 5、s 和 p 都由小写英文字母组成
 * 6、removable 中的元素 互不相同
 * 链接：https://leetcode-cn.com/problems/maximum-number-of-removable-characters
 */
public class Q1898 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q1898().maximumRemovals("x", "x", stringToIntegerArray("[0]")));
        // 1
        System.out.println(new Q1898().maximumRemovals("abcbddddd", "abcd", stringToIntegerArray("[3,2,1,4,5,6]")));
        // 0
        System.out.println(new Q1898().maximumRemovals("abcab", "abc", stringToIntegerArray("[0,1,2,3,4]")));
        // 2
        System.out.println(new Q1898().maximumRemovals("abcacb", "ab", stringToIntegerArray("[3,1,0]")));
    }

    public int maximumRemovals(String s, String p, int[] removable) {
        int ret = 0, l = 0, r = removable.length - 1;
        char[] sStr = s.toCharArray(), pStr = p.toCharArray();
        while (l <= r) {
            int mid = l + ((r - l) >> 1);
            if (check(sStr, pStr, removable, mid)) {
                l = mid + 1;
                ret = mid + 1;
            } else r = mid - 1;
        }
        return ret;
    }

    boolean check(char[] sStr, char[] pStr, int[] r, int idx) {
        boolean[] flag = new boolean[sStr.length];
        for (int i = 0; i <= idx; i++) flag[r[i]] = true;
        int i = 0, j = 0;
        boolean ret = false;
        for (; i < pStr.length && j < sStr.length; i++, j++) {
            while (j < sStr.length && (sStr[j] != pStr[i] || flag[j])) j++;
            ret = j != sStr.length;
        }
        ret &= i == pStr.length;
        return ret;
    }
}
