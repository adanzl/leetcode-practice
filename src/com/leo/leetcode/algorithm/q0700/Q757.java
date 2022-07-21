package com.leo.leetcode.algorithm.q0700;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 一个整数区间 [a, b] ( a < b ) 代表着从 a 到 b 的所有连续整数，包括 a 和 b。
 * 给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。
 * 输出这个最小集合S的大小。
 * 注意:
 * 1、intervals 的长度范围为[1, 3000]。
 * 2、intervals[i] 长度为 2，分别代表左、右边界。
 * 3、intervals[i][j] 的值是 [0, 10^8]范围内的整数。
 * 链接：https://leetcode.cn/problems/set-intersection-size-at-least-two
 */
public class Q757 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q757().intersectionSizeTwo(stringToInt2dArray("[[1,3],[1,2],[0,1]]")));
        // 5
        System.out.println(new Q757().intersectionSizeTwo(stringToInt2dArray("[[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]")));
        // 2
        System.out.println(new Q757().intersectionSizeTwo(stringToInt2dArray("[[1,3000],[1,3000],[1,3000],[1,3000]]")));
        // 3
        System.out.println(new Q757().intersectionSizeTwo(stringToInt2dArray("[[1,3],[1,3000],[2,5],[3,5]]")));
        // 5
        System.out.println(new Q757().intersectionSizeTwo(stringToInt2dArray("[[1,2],[2,3],[2,4],[4,5]]")));
    }

    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] == b[1] ? b[0] - a[0] : a[1] - b[1]);
        int ret = 2, p1 = intervals[0][1] - 1, p2 = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int[] inter = intervals[i];
            if (inter[0] <= p1) continue;
            if (inter[0] > p2) {
                ret += 2;
                p1 = inter[1] - 1;
                p2 = inter[1];
            } else if (p2 == inter[1]) {
                ret++;
                p1 = p2 - 1;
            } else {
                ret++;
                p1 = p2;
                p2 = inter[1];
            }
        }
        return ret;
    }
}
