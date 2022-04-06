package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;
import java.util.Comparator;
import java.util.TreeMap;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个区间数组 intervals ，其中 intervals[i] = [start_i, end_i] ，且每个  start_i 都 不同 。
 * 区间 i 的 右侧区间 可以记作区间 j ，并满足 start_j >= end_i ，且 start_j 最小化 。
 * 返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。
 * 提示：
 * 1 <= intervals.length <= 2 * 10^4
 * intervals[i].length == 2
 * -10^6 <= start_i <= end_i <= 10^6
 * 每个间隔的起点都 不相同
 * 链接：https://leetcode-cn.com/problems/find-right-interval
 */
public class Q436 {

    public static void main(String[] args) {
        // [-1,2,-1]
        System.out.println(Arrays.toString(new Q436().findRightInterval(stringToInt2dArray("[[1,4],[2,3],[3,4]]"))));
        // [-1,0,1]
        System.out.println(Arrays.toString(new Q436().findRightInterval(stringToInt2dArray("[[3,4],[2,3],[1,2]]"))));
        // [-1]
        System.out.println(Arrays.toString(new Q436().findRightInterval(stringToInt2dArray("[[1,2]]"))));
    }

    public int[] findRightInterval(int[][] intervals) {
        int len = intervals.length;
        int[] ret = new int[len];
        TreeMap<int[], Integer> tMap = new TreeMap<>(Comparator.comparingInt(o -> o[0]));
        for (int i = 0; i < len; i++) tMap.put(intervals[i], i);
        for (int i = 0; i < len; i++) {
            int[] idx = tMap.ceilingKey(new int[]{intervals[i][1]});
            if (null == idx) ret[i] = -1;
            else ret[i] = tMap.get(idx);
        }
        return ret;
    }
}
