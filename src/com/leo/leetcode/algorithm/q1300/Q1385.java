package com.leo.leetcode.algorithm.q1300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
 * 「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
 * 提示：
 * 1、1 <= arr1.length, arr2.length <= 500
 * 2、-10^3 <= arr1[i], arr2[j] <= 10^3
 * 3、0 <= d <= 100
 * 链接：https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays
 */
public class Q1385 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q1385().findTheDistanceValue(stringToIntegerArray("[-3,-3,4,-1,-10]"), stringToIntegerArray("[7,10]"), 12));
        // 0
        System.out.println(new Q1385().findTheDistanceValue(stringToIntegerArray("[-8,-7]"), stringToIntegerArray("[4,10,-4,5,2]"), 55));
        // 2
        System.out.println(new Q1385().findTheDistanceValue(stringToIntegerArray("[1,4,2,3]"), stringToIntegerArray("[-4,-3,6,10,20,30]"), 3));
        // 2
        System.out.println(new Q1385().findTheDistanceValue(stringToIntegerArray("[4,5,8]"), stringToIntegerArray("[10,9,1,8]"), 2));
        // 1
        System.out.println(new Q1385().findTheDistanceValue(stringToIntegerArray("[2,1,100,3]"), stringToIntegerArray("[-5,-2,10,-3,7]"), 6));
    }

    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2);
        int ret = 0;
        for (int num : arr1) {
            int idx = binarySearch(arr2, num);
            if (idx == 0) {
                if (arr2[0] - num > d) ret++;
            } else if (idx == arr2.length) {
                if (num - arr2[idx - 1] > d) ret++;
            } else if (num - arr2[idx - 1] > d && arr2[idx] - num > d) ret++;
        }
        return ret;
    }

    int binarySearch(int[] arr, int v) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] <= v) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}
