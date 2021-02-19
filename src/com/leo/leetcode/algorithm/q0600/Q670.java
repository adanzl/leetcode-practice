package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

/**
 * 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
 * <p>
 * 注意:
 * 给定数字的范围是 [0, 108]
 * <p>
 * 链接：https://leetcode-cn.com/problems/maximum-swap/
 */
public class Q670 {

    public static void main(String[] args) {
        // 7236
        System.out.println(new Q670().maximumSwap(2736));
        // 9973
        System.out.println(new Q670().maximumSwap(9973));
    }

    public int maximumSwap(int num) {
        if (num < 10) return num;
        int[] arr = new int[8];
        int i = 0, out = 0;
        while (num != 0) {
            arr[i++] = num % 10;
            num /= 10;
        }

        int[] flag = new int[10];
        Arrays.fill(flag, -1);
        for (int j = 0; j < i; j++) {
            if (flag[arr[j]] == -1) flag[arr[j]] = j;
        }
        int l = 0, r = 0;
        loop:
        for (int j = i - 1; j > 0; j--) {
            int v = arr[j];
            for (int k = 9; k > v; k--) {
                int p = flag[k];
                if (p >= 0 && p < j) {
                    l = j;
                    r = p;
                    break loop;
                }
            }
        }
        swap(arr, l, r);
        for (int j = i - 1; j > 0; j--) {
            out += arr[j];
            out *= 10;
        }
        out += arr[0];
        return out;
    }

    void swap(int[] arr, int l, int r) {
        int t = arr[l];
        arr[l] = arr[r];
        arr[r] = t;
    }
}
