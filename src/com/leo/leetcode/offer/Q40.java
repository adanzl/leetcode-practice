package com.leo.leetcode.offer;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q40 {

    public static void main(String[] args) {
        new Q40().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(getLeastNumbers(LCUtil.stringToIntegerArray("[0,0,1,2,4,2,2,3,1,4]"), 8))); // [0,0,1,1,2,2,2,3]
        System.out.println(Arrays.toString(getLeastNumbers(LCUtil.stringToIntegerArray("[3,2,1]"), 2))); // [1,2]
    }

    public int[] getLeastNumbers(int[] arr, int k) {
        if (arr.length <= k) return arr;
        if (k == 0) return new int[0];
        int f = 0, start = 0, end = arr.length;
        while (f != k - 1) {
            f = search(arr, start, end);
            if (f < k - 1) {
                start = f + 1; //
            } else if (f > k - 1) {
                end = f;
            }
        }
        return Arrays.copyOf(arr, k);
    }

    void swap(int[] arr, int l, int r) {
        int t = arr[l];
        arr[l] = arr[r];
        arr[r] = t;
    }

    int search(int[] arr, int start, int end) {
        int l = start, r = end - 1;
        int v = arr[l];
        while (l < r) {
            while (l < r && arr[r] >= v) r--; // 因为把pivot放在了开始，所以r指针先走
            while (l < r && arr[l] <= v) l++;
            if (l != r) swap(arr, l, r);
        }
        swap(arr, start, l);
        return l;
    }
}
