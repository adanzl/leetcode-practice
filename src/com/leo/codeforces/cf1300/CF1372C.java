package com.leo.codeforces.cf1300;

import java.util.Arrays;

public class CF1372C {
    public static void main(String[] args) {
        // 0
        System.out.println(func(new int[]{1, 2, 3, 4, 5}));
        // 2
        System.out.println(func(new int[]{1, 5, 3, 4, 6, 2}));
        // 2
        System.out.println(func(new int[]{5, 1, 3, 4, 6, 2}));
        // 2
        System.out.println(func(new int[]{1, 5, 3, 4, 2, 6}));
        // 2
        System.out.println(func(new int[]{5, 1, 3, 4, 2, 6}));
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        while (n-- > 0) {
//            int len = sc.nextInt();
//            int[] nums = new int[len];
//            for (int i = 0; i < len; i++) {
//                nums[i] = sc.nextInt();
//            }
//            System.out.println(func(nums));
//        }

    }

    static int func(int[] nums) {
        int[] sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        int cnt = 0, ret = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != sorted[i]) cnt++;
            else {
                if (cnt != 0) ret++;
                cnt = 0;
            }
        }
        if (cnt != 0) ret++;
        return Math.min(ret, 2);
    }
}
