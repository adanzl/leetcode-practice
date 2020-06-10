package com.leo.interview;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.Arrays;

public class QSort {


    @Test
    public void TestOJ() {
        System.out.println(Arrays.toString(qSort(LCUtil.stringToIntegerArray("[4,3,12,1,5,5,2,6]")))); // [1, 2, 3, 4, 5, 5, 6, 12]
    }

    int[] qSort(int[] arr) {
        sort(arr, 0, arr.length);
        return arr;
    }

    int walk(int[] arr, int start, int end) {
        int l = start, r = end - 1;
        if (l >= r) return l;
        int v = arr[start];
        while (l < r) {
            while (l < r && arr[r] >= v) r--;
            while (l < r && arr[l] <= v) l++;
            swap(arr, l, r);
        }
        swap(arr, start, l);
        return l;
    }

    void sort(int[] arr, int l, int r) {
        if (l >= r) return;
        int m = walk(arr, l, r);
        sort(arr, l, m);
        sort(arr, m + 1, r);
    }

    void swap(int[] arr, int l, int r) {
        int t = arr[l];
        arr[l] = arr[r];
        arr[r] = t;
    }
}
