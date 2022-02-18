package com.leo.leetcode.algorithm.q0900;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。
 * 一次煎饼翻转的执行过程如下：
 * 选择一个整数 k ，1 <= k <= arr.length
 * 反转子数组 arr[0...k-1]（下标从 0 开始）
 * 例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。
 * 以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。
 * 提示：
 * 1、1 <= arr.length <= 100
 * 2、1 <= arr[i] <= arr.length
 * 3、arr 中的所有整数互不相同（即，arr 是从 1 到 arr.length 整数的一个排列）
 * 链接：https://leetcode-cn.com/problems/pancake-sorting
 */
public class Q969 {
    public static void main(String[] args) {
        // [3, 4, 2, 3, 1, 2]
        System.out.println(new Q969().pancakeSort(stringToIntegerArray("[3,2,4,1]")));
        // []
        System.out.println(new Q969().pancakeSort(stringToIntegerArray("[1,2,3]")));
    }

    List<Integer> ret = new ArrayList<>();

    public List<Integer> pancakeSort(int[] arr) {

        for (int i = arr.length - 1; i >= 0; i--) {
            if (i + 1 == arr[i]) continue;
            int idx = 0;
            for (; idx < arr.length; idx++) {
                if (arr[idx] == i + 1) break;
            }
            swap(arr, idx + 1);
            swap(arr, i + 1);
        }
        return ret;
    }

    void swap(int[] arr, int n) {
        int len = n >> 1;
        for (int i = 0; i < len; i++) {
            int t = arr[i];
            arr[i] = arr[n - i - 1];
            arr[n - i - 1] = t;
        }
        ret.add(n);
    }
}
