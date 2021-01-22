package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;
import java.util.Comparator;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
 * 注意:
 * 1、可以认为区间的终点总是大于它的起点。
 * 2、区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
 * <p>
 * 链接：https://leetcode-cn.com/problems/non-overlapping-intervals
 */
public class Q435 {

    public static void main(String[] args) {
        //  0
        System.out.println(new Q435().eraseOverlapIntervals(stringToInt2dArray("[]")));
        //  0
        System.out.println(new Q435().eraseOverlapIntervals(stringToInt2dArray("[[1,2],[2,3]]")));
        //  2
        System.out.println(new Q435().eraseOverlapIntervals(stringToInt2dArray("[[1,100],[11,22],[1,11],[2,12]]")));
        //  1
        System.out.println(new Q435().eraseOverlapIntervals(stringToInt2dArray("[[1,2],[2,3],[3,4],[1,3]]")));
        //  2
        System.out.println(new Q435().eraseOverlapIntervals(stringToInt2dArray("[[1,2],[1,2],[1,2]]")));
    }


    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        // Arrays.sort(intervals, (a, b) -> a[0] - b[0]); 用这个会从3ms优化到1ms
        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));
        int ret = 0, r = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (r <= intervals[i][0]) {
                r = intervals[i][1];
            } else {
                ret++;
                r = Math.min(r, intervals[i][1]);
            }
        }
        return ret;
    }

}
