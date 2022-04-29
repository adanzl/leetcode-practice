package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [start_i, end_i] 表示第 i 朵花的 花期 从 start_i 到 end_i （都 包含）。
 * 同时给你一个下标从 0 开始大小为 n 的整数数组 persons ，persons[i] 是第 i 个人来看花的时间。
 * 请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。
 * 提示：
 * 1、1 <= flowers.length <= 5 * 10^4
 * 2、flowers[i].length == 2
 * 3、1 <= start_i <= end_i <= 10^9
 * 4、1 <= persons.length <= 5 * 10^4
 * 5、1 <= persons[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/number-of-flowers-in-full-bloom
 */
public class Q2251 {

    public static void main(String[] args) {
        // [1,2,2,2]
        System.out.println(Arrays.toString(new Q2251().fullBloomFlowers(
                stringToInt2dArray("[[1,6],[3,7],[9,12],[4,13]]"),
                stringToIntegerArray("[2,3,7,11]"))));
        // [2,2,1]
        System.out.println(Arrays.toString(new Q2251().fullBloomFlowers(
                stringToInt2dArray("[[1,10],[3,3]]"),
                stringToIntegerArray("[3,3,2]"))));
    }

    public int[] fullBloomFlowers(int[][] flowers, int[] persons) {
        int[] ret = new int[persons.length];
        int[] startTimes = Arrays.stream(flowers).mapToInt(x -> x[0]).sorted().toArray();
        int[] endTimes = Arrays.stream(flowers).mapToInt(x -> x[1]).sorted().toArray();
        for (int i = 0; i < persons.length; i++) {
            ret[i] = lowerBound(startTimes, persons[i]) - lowerBound(endTimes, persons[i] - 1);
        }
        return ret;
    }

    // 插入位置
    int lowerBound(int[] arr, int x) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] > x) r = mid - 1;
            else l = mid + 1;
        }
        return l;
    }
}
