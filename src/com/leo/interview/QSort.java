package com.leo.interview;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class QSort {

    public static void main(String[] args) {
        new QSort().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(qSort(LCUtil.stringToIntegerArray("[4,3,12,1,5,5,2,6]")))); // [1, 2, 3, 4, 5, 5, 6, 12]
    }

    int[] qSort(int[] arr) {
        sort(arr, 0, arr.length);
        return arr;
    }

    void sort(int[] arr, int start, int end) {
        int l = start, r = end - 1;
        if (l >= r) return;
        int v = arr[l];
        while (l < r) {
            while (l < r && arr[r] >= v) r--;
            while (l < r && arr[l] <= v) l++;
            swap(arr, l, r);
        }
        swap(arr, start, l);
        sort(arr, start, l);
        sort(arr, l + 1, end);
    }

    void swap(int[] arr, int l, int r) {
        int t = arr[l];
        arr[l] = arr[r];
        arr[r] = t;
    }
}
