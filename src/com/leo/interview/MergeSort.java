package com.leo.interview;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {
        new MergeSort().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(mergeSort(LCUtil.stringToIntegerArray("[1,3,2,3,1]")))); // [1, 1, 2, 3, 3]
        System.out.println(Arrays.toString(mergeSort(LCUtil.stringToIntegerArray("[7,5,6,4]")))); // [4, 5, 6, 7]
        System.out.println(Arrays.toString(mergeSort(LCUtil.stringToIntegerArray("[4,3,12,1,5,5,2,6]")))); // [1, 2, 3, 4, 5, 5, 6, 12]
    }

    int[] mergeSort(int[] arr) {
        mSort(arr, 0, arr.length, new int[arr.length]);
        return arr;
    }

    void mSort(int[] arr, int start, int end, int[] tmp) {
        if (start >= end - 1) return;
        int m = (start + end) >> 1;
        mSort(arr, start, m, tmp);
        mSort(arr, m, end, tmp);
        merge(arr, start, m, end, tmp);
    }

    void merge(int[] arr, int start, int mid, int end, int[] temp) {
        int i = start, l1 = start, l2 = mid;
        while (l1 < mid && l2 < end) {
            if (arr[l1] <= arr[l2]) {
                temp[i++] = arr[l1++];
            } else {
                temp[i++] = arr[l2++];
            }
        }
        while (l1 < mid) temp[i++] = arr[l1++];
        while (l2 < end) temp[i++] = arr[l2++];
        while (start < end) arr[start] = temp[start++];
    }
}
