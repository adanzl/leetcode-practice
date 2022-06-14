package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
 * 同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
 * 请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
 * 提示：
 * 1、n == spells.length
 * 2、m == potions.length
 * 3、1 <= n, m <= 10^5
 * 4、1 <= spells[i], potions[i] <= 10^5
 * 5、1 <= success <= 10^10
 * 链接：https://leetcode.cn/problems/successful-pairs-of-spells-and-potions
 */
public class Q2300 {

    public static void main(String[] args) {
        // [4,0,3]
        System.out.println(Arrays.toString(new Q2300().successfulPairs(stringToIntegerArray("[5,1,3]"), stringToIntegerArray("[1,2,3,4,5]"), 7)));
        // [2,0,2]
        System.out.println(Arrays.toString(new Q2300().successfulPairs(stringToIntegerArray("[3,1,2]"), stringToIntegerArray("[8,5,8]"), 16)));
    }

    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length, m = potions.length;
        int[] ret = new int[n];
        Arrays.sort(potions);
        for (int i = 0; i < n; i++) {
            int idx = bSearch(potions, (double) success / spells[i]);
            ret[i] = m - idx;
        }
        return ret;
    }

    int bSearch(int[] arr, double v) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] >= v) r = mid - 1;
            else l = mid + 1;
        }
        return l;
    }
}
