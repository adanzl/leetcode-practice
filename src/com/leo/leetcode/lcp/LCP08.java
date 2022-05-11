package com.leo.leetcode.lcp;


import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（C），资源储备（R）以及人口数量（H）。
 * 在游戏开始时（第 0 天），三种属性的值均为 0。
 * 随着游戏进程的进行，每一天玩家的三种属性都会对应增加，我们用一个二维数组 increase 来表示每天的增加情况。
 * 这个二维数组的每个元素是一个长度为 3 的一维数组，例如 [[1,2,1],[3,4,2]] 表示第一天三种属性分别增加 1,2,1 而第二天分别增加 3,4,2。
 * 所有剧情的触发条件也用一个二维数组 requirements 表示。
 * 这个二维数组的每个元素是一个长度为 3 的一维数组，对于某个剧情的触发条件 c[i], r[i], h[i]，如果当前 C >= c[i] 且 R >= r[i] 且 H >= h[i] ，则剧情会被触发。
 * 根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。
 * 限制：
 * 1、1 <= increase.length <= 10000
 * 2、1 <= requirements.length <= 100000
 * 3、0 <= increase[i] <= 10
 * 4、0 <= requirements[i] <= 100000
 * 链接：https://leetcode.cn/problems/ju-qing-hong-fa-shi-jian
 */
public class LCP08 {

    public static void main(String[] args) {
        // [2,-1,3,-1]
        System.out.println(Arrays.toString(new LCP08().getTriggerTime(
                stringToInt2dArray("[[2,8,4],[2,5,0],[10,9,8]]"),
                stringToInt2dArray("[[2,11,3],[15,10,7],[9,17,12],[8,1,14]]"))));
        // [-1,4,3,3,3]
        System.out.println(Arrays.toString(new LCP08().getTriggerTime(
                stringToInt2dArray("[[0,4,5],[4,8,8],[8,6,1],[10,10,0]]"),
                stringToInt2dArray("[[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]"))));
        // [0]
        System.out.println(Arrays.toString(new LCP08().getTriggerTime(
                stringToInt2dArray("[[1,1,1]]"),
                stringToInt2dArray("[[0,0,0]]"))));
    }

    public int[] getTriggerTime(int[][] increase, int[][] requirements) {
        int n = increase.length;
        int[] ret = new int[requirements.length], cArr = new int[n + 1], rArr = new int[n + 1], hArr = new int[n + 1];
        for (int i = 0; i < n; i++) {
            cArr[i + 1] = cArr[i] + increase[i][0];
            rArr[i + 1] = rArr[i] + increase[i][1];
            hArr[i + 1] = hArr[i] + increase[i][2];
        }
        for (int i = 0; i < requirements.length; i++) {
            int ic = bSearch(cArr, requirements[i][0]);
            int ir = bSearch(rArr, requirements[i][1]);
            int ih = bSearch(hArr, requirements[i][2]);
            if (ic > n || ir > n || ih > n) {
                ret[i] = -1;
            } else {
                ret[i] = Math.max(ic, Math.max(ir, ih));
            }
        }
        return ret;
    }

    int bSearch(int[] arr, int target) {
        int l = 0, r = arr.length - 1, ret = arr.length;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] < target) l = mid + 1;
            else {
                ret = mid;
                r = mid - 1;
            }
        }
        return ret;
    }
}
