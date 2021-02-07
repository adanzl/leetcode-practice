package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
 * 1、若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
 * 2、或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
 * <p>
 * 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
 * 返回 A 的最大湍流子数组的长度。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 40000
 * 2、0 <= A[i] <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/longest-turbulent-subarray/
 */
public class Q978 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q978().maxTurbulenceSize(stringToIntegerArray("[9,9]")));
        // 5
        System.out.println(new Q978().maxTurbulenceSize(stringToIntegerArray("[9,4,2,10,7,8,8,1,9]")));
        // 2
        System.out.println(new Q978().maxTurbulenceSize(stringToIntegerArray("[4,8,12,16]")));
        // 1
        System.out.println(new Q978().maxTurbulenceSize(stringToIntegerArray("[100]")));
    }

    public int maxTurbulenceSize(int[] arr) {
        int l = 0, r = 1, ret = 1, pre = 0;
        while (r < arr.length) {
            int diff = (arr[r] - arr[r - 1]);
            if (diff == 0) l = r;
            else if (pre != 0 && (pre ^ diff) >= 0) l = r - 1;
            pre = diff;
            ret = Math.max(ret, r - l + 1);
            r++;
        }
        return ret;
    }

}
