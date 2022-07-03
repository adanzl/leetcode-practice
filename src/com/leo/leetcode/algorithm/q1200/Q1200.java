package com.leo.leetcode.algorithm.q1200;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你个整数数组 arr，其中每个元素都 不相同。
 * 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
 * 提示：
 * 1、2 <= arr.length <= 10^5
 * 2、-10^6 <= arr[i] <= 10^6
 */
public class Q1200 {

    public static void main(String[] args) {
        // [[1,2],[2,3],[3,4]]
        System.out.println(new Q1200().minimumAbsDifference(stringToIntegerArray("[4,2,1,3]")));
        // [[1,3]]
        System.out.println(new Q1200().minimumAbsDifference(stringToIntegerArray("[1,3,6,10,15]")));
        // [[-14,-10],[19,23],[23,27]]
        System.out.println(new Q1200().minimumAbsDifference(stringToIntegerArray("[3,8,-10,23,19,-4,-14,27]")));
    }

    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        int n = arr.length, min = Integer.MAX_VALUE;
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(arr);
        for (int i = 1; i < n; i++) {
            min = Math.min(min, arr[i] - arr[i - 1]);
        }
        for (int i = 1; i < n; i++) {
            if (min == arr[i] - arr[i - 1]) {
                ret.add(Arrays.asList(arr[i - 1], arr[i]));
            }
        }
        return ret;
    }
}
