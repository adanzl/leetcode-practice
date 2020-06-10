package com.leo.leetcode.algorithm;

public class Q42 {
    public void TestOJ() {
        System.out.println(trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1})); // 6
    }

    public int trap(int[] height) {
        if (height.length < 3) return 0;
        int[] l = new int[height.length];
        int[] r = new int[height.length];
        int max = height[0];
        for (int i = 1; i < height.length; i++) {
            l[i] = max;
            max = Math.max(height[i], max);
        }
        max = height[height.length - 1];
        for (int i = height.length - 2; i >= 0; i--) {
            r[i] = max;
            max = Math.max(height[i], max);
        }

        int ret = 0;
        for (int i = 1; i < height.length - 1; i++) {
            int v = Math.min(l[i], r[i]) - height[i];
            v = Math.max(v, 0);
            ret += v;
        }
        return ret;
    }

    public int trap2(int[] height) {

        int left = 0;
        int right = height.length - 1;
        int ans = 0;
        int left_max = 0, right_max = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) left_max = height[left];
                else ans += (left_max - height[left]);
                ++left;
            } else {
                if (height[right] >= right_max) right_max = height[right];
                else ans += (right_max - height[right]);
                --right;
            }
        }
        return ans;
    }
}
