package com.leo.codeforces.cf1611;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 链接：https://codeforces.com/problemset/problem/1611/F
 * 链接：https://www.luogu.com.cn/problem/CF1611F
 */
public class CF1611F {

    public static void main(String[] args) {
        // -1
        System.out.println(Arrays.toString(func(3, 1000, new int[]{-100000, -100000, -100000})));
        // 2 4
        System.out.println(Arrays.toString(func(4, 10, new int[]{-16, 2, -6, 8})));
        // 1 2
        System.out.println(Arrays.toString(func(6, 0, new int[]{2, 6, -164, 1, -1, -6543})));

        /*
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt(), s = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[] ans = func(n, s, arr);
            for (int i : ans) System.out.print(i + " ");
            System.out.println();
        }
        */
    }

    static int[] func(int n, int s, int[] arr) {
        long[] preSum = new long[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + arr[i];
        int[] ans = new int[2];
        int l = 0, r = 0, max = 0;
        while (r < n) {
            while (r < n - 1 && preSum[r + 1 + 1] - preSum[l] >= -s) r++;
            if (arr[l] >= -s && r - l + 1 > max) {
                max = r - l + 1;
                ans[0] = l + 1;
                ans[1] = r + 1;
            }
            l++;
            r = Math.max(l, r);
        }
        if (max == 0) return new int[]{-1};
        return ans;
    }
}
