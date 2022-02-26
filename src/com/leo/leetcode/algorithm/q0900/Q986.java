package com.leo.leetcode.algorithm.q0900;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，
 * 其中 firstList[i] = [start_i, end_i] 而 secondList[j] = [start_j, end_j] 。
 * 每个区间列表都是成对 不相交 的，并且 已经排序 。
 * 返回这 两个区间列表的交集 。
 * 形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
 * 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
 * 提示：
 * 1、0 <= firstList.length, secondList.length <= 1000
 * 2、firstList.length + secondList.length >= 1
 * 3、0 <= start_i < end_i <= 10^9
 * 4、end_i < start_i+1
 * 5、0 <= start_j < end_j <= 10^9
 * 6、end_j < start_j+1
 * 链接：https://leetcode-cn.com/problems/interval-list-intersections
 */
public class Q986 {

    public static void main(String[] args) {
        // [[4,4]]
        System.out.println(int2dArrayToString(new Q986().intervalIntersection(stringToInt2dArray("[[4,7],[8,14]]"), stringToInt2dArray("[[3,4]]"))));
        // [[5,10]]
        System.out.println(int2dArrayToString(new Q986().intervalIntersection(stringToInt2dArray("[[3,10]]"), stringToInt2dArray("[[5,10]]"))));
        // [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        System.out.println(int2dArrayToString(new Q986().intervalIntersection(stringToInt2dArray("[[0,2],[5,10],[13,23],[24,25]]"), stringToInt2dArray("[[1,5],[8,12],[15,24],[25,26]]"))));
        // []
        System.out.println(int2dArrayToString(new Q986().intervalIntersection(stringToInt2dArray("[[1,3],[5,9]]"), stringToInt2dArray("[]"))));
        // []
        System.out.println(int2dArrayToString(new Q986().intervalIntersection(stringToInt2dArray("[]"), stringToInt2dArray("[[4,8],[10,12]]"))));
        // [[3,7]]
        System.out.println(int2dArrayToString(new Q986().intervalIntersection(stringToInt2dArray("[[1,7]]"), stringToInt2dArray("[[3,10]]"))));
    }


    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        if (firstList.length == 0 || secondList.length == 0) return new int[0][];
        List<int[]> ret = new ArrayList<>();
        int[] area0 = firstList[0], area1 = secondList[0];
        int i0 = 0, i1 = 0, s0 = area0[0], s1 = area1[0], e0 = area0[1], e1 = area1[1];
        while (true) {
            if (e0 < s1) {
                if (i0 == firstList.length - 1) break;
                area0 = firstList[++i0];
                s0 = area0[0];
                e0 = area0[1];
            } else if (e1 < s0) {
                if (i1 == secondList.length - 1) break;
                area1 = secondList[++i1];
                s1 = area1[0];
                e1 = area1[1];
            } else {
                int v0 = Math.max(s0, s1), v1 = Math.min(e0, e1);
                ret.add(new int[]{v0, v1});
                s0 = v1 + 1;
                s1 = v1 + 1;
                if (s0 > e0) {
                    if (i0 == firstList.length - 1) break;
                    area0 = firstList[++i0];
                    s0 = area0[0];
                    e0 = area0[1];
                }
                if (s1 > e1) {
                    if (i1 == secondList.length - 1) break;
                    area1 = secondList[++i1];
                    s1 = area1[0];
                    e1 = area1[1];
                }
            }
        }
        return ret.toArray(new int[ret.size()][2]);
    }

}
