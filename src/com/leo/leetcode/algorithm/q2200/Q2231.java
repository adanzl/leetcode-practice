package com.leo.leetcode.algorithm.q2200;

import java.util.*;

/**
 * 给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。
 * 返回交换 任意 次之后 num 的 最大 可能值。
 * 提示： * 1 <= num <= 10^9
 * 链接：https://leetcode-cn.com/problems/largest-number-after-digit-swaps-by-parity/
 */
public class Q2231 {

    public static void main(String[] args) {
        // 3412
        System.out.println(new Q2231().largestInteger(1234));
        // 87655
        System.out.println(new Q2231().largestInteger(65875));
    }

    public int largestInteger(int num) {
        char[] nums = String.valueOf(num).toCharArray(), ret = new char[nums.length];
        List<Integer> odd = new ArrayList<>(), even = new ArrayList<>();
        for (char c : nums) {
            if ((c - '0') % 2 == 0) odd.add(c - '0');
            else even.add(c - '0');
        }
        odd.sort(Comparator.reverseOrder());
        even.sort(Comparator.reverseOrder());
        for (int i = 0, io = 0, ie = 0; i < nums.length; i++) {
            if ((nums[i] - '0') % 2 == 0) ret[i] = (char) ('0' + odd.get(io++));
            else ret[i] = (char) ('0' + even.get(ie++));
        }
        return Integer.parseInt(new String(ret));
    }
}
