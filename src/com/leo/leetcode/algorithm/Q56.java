package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.Arrays;

public class Q56 {
    @Test
    public void TestOJ() {
        System.out.println(LCUtil.int2dArrayToString(merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}}))); // [[1,6],[8,10],[15,18]]
        System.out.println(LCUtil.int2dArrayToString(merge(new int[][]{{1, 4}, {5, 6}}))); // [[1,4],[5,6]]
        System.out.println(LCUtil.int2dArrayToString(merge(new int[][]{{2, 3}, {4, 5}, {6, 7}, {8, 9}, {1, 10}}))); // [[1,10]]
        System.out.println(LCUtil.int2dArrayToString(merge(new int[][]{{2, 3}, {5, 5}, {3, 4}, {3, 4}}))); // [[2, 4],[5, 5]]
    }

    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;
        int index = 0;
        for (int i = 1; i < intervals.length; i++) {
            int[] range = intervals[i];
            for (int j = 0; j <= index; j++) {
                int[] oriRange = intervals[j];
                if (oriRange[1] < range[0] || oriRange[0] > range[1]) {
                    if (j == index) {
                        index++;
                        intervals[index][0] = range[0];
                        intervals[index][1] = range[1];
                        break;
                    }
                } else {
                    oriRange[0] = Math.min(range[0], oriRange[0]);
                    oriRange[1] = Math.max(range[1], oriRange[1]);
                    break;
                }
            }
        }
        if (index + 1 == intervals.length) {
            return Arrays.copyOf(intervals, index + 1);
        }
        return merge(Arrays.copyOf(intervals, index + 1));
    }
}
