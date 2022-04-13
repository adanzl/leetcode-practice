package com.leo.leetcode.algorithm.q1900;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 一个 2D 网格中的 顶峰元素 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。
 * 给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 顶峰元素 mat[i][j] 并 返回其位置 [i,j] 。
 * 你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。
 * 要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、1 <= m, n <= 500
 * 4、1 <= mat[i][j] <= 10^5
 * 5、任意两个相邻元素均不相等.
 * 链接：https://leetcode-cn.com/problems/find-a-peak-element-ii
 */
public class Q1901 {

    public static void main(String[] args) {
        // [0, 0]
        System.out.println(Arrays.toString(new Q1901().findPeakGrid(stringToInt2dArray("[[20,43,38,24,31],[36,34,23,28,48],[22,23,45,30,18],[20,17,15,8,47],[13,21,8,48,35],[49,45,12,13,14],[48,31,18,47,38],[49,34,39,19,7]]"))));
        // [0, 0]
        System.out.println(Arrays.toString(new Q1901().findPeakGrid(stringToInt2dArray("[[48,36,35,17,48],[38,28,38,26,24],[15,9,33,32,6],[49,4,8,10,41]]"))));
        // [2, 2]
        System.out.println(Arrays.toString(new Q1901().findPeakGrid(stringToInt2dArray("[[10,20,15],[21,30,14],[7,16,32]]"))));
        // [0, 1]
        System.out.println(Arrays.toString(new Q1901().findPeakGrid(stringToInt2dArray("[[1,4],[3,2]]"))));
    }

    public int[] findPeakGrid(int[][] mat) {
        int m = mat.length;
        int[] maxArr = new int[m];
        for (int i = 0; i < m; i++) maxArr[i] = maxIdx(mat[i]);
        int left = 0, right = m - 1;
        while (left <= right) {
            int mid = (left + right) / 2, maxMid = mat[mid][maxArr[mid]];
            int maxUp = mid == 0 ? -1 : mat[mid - 1][maxArr[mid - 1]];
            int maxDown = mid == m - 1 ? -1 : mat[mid + 1][maxArr[mid + 1]];
            if (maxMid >= Math.max(maxDown, maxUp)) return new int[]{mid, maxArr[mid]};
            else if (maxUp >= Math.max(maxMid, maxDown)) right = mid - 1;
            else left = mid + 1;
        }
        return new int[2];
    }

    int maxIdx(int[] arr) {
        if (arr.length == 0) return -1;
        int ret = 0;
        for (int i = 1; i < arr.length; i++) if (arr[i] > arr[ret]) ret = i;
        return ret;
    }
}
