package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 特殊楼层 ，仅用于放松。
 * 给你两个整数 bottom 和 top ，表示 Alice 租用了从 bottom 到 top（含 bottom 和 top 在内）的所有楼层。另给你一个整数数组 special ，其中 special[i] 表示 Alice 指定用于放松的特殊楼层。
 * 返回不含特殊楼层的 最大 连续楼层数。
 * 提示
 * 1、1 <= special.length <= 10^5
 * 2、1 <= bottom <= special[i] <= top <= 10^9
 * 3、special 中的所有值 互不相同
 * 链接：https://leetcode.cn/problems/maximum-consecutive-floors-without-special-floors
 */
public class Q2274 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2274().maxConsecutive(2, 9, stringToIntegerArray("[4,6]")));
        // 0
        System.out.println(new Q2274().maxConsecutive(6, 8, stringToIntegerArray("[7,6,8]")));
    }

    public int maxConsecutive(int bottom, int top, int[] special) {
        Arrays.sort(special);
        int max = Math.max(special[0] - bottom, 0);
        for (int i = 1; i < special.length; i++) {
            max = Math.max(max, special[i] - special[i - 1] - 1);
        }
        max = Math.max(max, Math.max(top - special[special.length - 1], 0));
        return max;
    }
}
