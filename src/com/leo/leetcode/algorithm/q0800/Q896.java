package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 如果数组是单调递增或单调递减的，那么它是单调的。
 * 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
 * 当给定的数组 A 是单调数组时返回 true，否则返回 false。
 * <p>
 * 提示：
 * 1、1 <= A.length <= 50000
 * 2、-100000 <= A[i] <= 100000
 * <p>
 * 链接：https://leetcode-cn.com/problems/monotonic-array
 */
public class Q896 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q896().isMonotonic(stringToIntegerArray("[1,2,2,3]")));
        // true
        System.out.println(new Q896().isMonotonic(stringToIntegerArray("[6,5,4,4]")));
        // false
        System.out.println(new Q896().isMonotonic(stringToIntegerArray("[1,3,2]")));
        // true
        System.out.println(new Q896().isMonotonic(stringToIntegerArray("[1,2,4,5]")));
        // true
        System.out.println(new Q896().isMonotonic(stringToIntegerArray("[1,1,1]")));
    }

    public boolean isMonotonic(int[] A) {
        int flag = 0;
        for (int i = 1; i < A.length; i++) {
            if (A[i] == A[i - 1]) continue;
            if (A[i] < A[i - 1]) {
                if (flag == 1) return false;
                flag = -1;
            } else {
                if (flag == -1) return false;
                flag = 1;
            }
        }
        return true;
    }
}
