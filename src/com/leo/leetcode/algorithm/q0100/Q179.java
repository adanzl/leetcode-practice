package com.leo.leetcode.algorithm.q0100;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
 * 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、0 <= nums[i] <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/largest-number
 */
public class Q179 {

    public static void main(String[] args) {
        // 9876543210
        System.out.println(new Q179().largestNumber(stringToIntegerArray("[1,2,3,4,5,6,7,8,9,0]")));
        // 0
        System.out.println(new Q179().largestNumber(stringToIntegerArray("[0,0]")));
        // 210
        System.out.println(new Q179().largestNumber(stringToIntegerArray("[10,2]")));
        // 9534330
        System.out.println(new Q179().largestNumber(stringToIntegerArray("[3,30,34,5,9]")));
        // 1
        System.out.println(new Q179().largestNumber(stringToIntegerArray("[1]")));
        // 10
        System.out.println(new Q179().largestNumber(stringToIntegerArray("[10]")));
    }

    public String largestNumber(int[] nums) {
        sort(nums, 0, nums.length - 1);
        StringBuilder sb = new StringBuilder();
        boolean nonZero = false;
        for (int n : nums) {
            if (!nonZero && n == 0) continue;
            nonZero = true;
            sb.append(n);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }

    void sort(int[] a, int left, int right) {
        if (left < right) {
            int mid = partition(a, left, right);
            sort(a, left, mid - 1);
            sort(a, mid + 1, right);
        }
    }

    int partition(int[] a, int low, int high) {
        int key = a[low];
        while (low < high) {
            while (low < high && compare(a[high], key) >= 0) high--;
            a[low] = a[high];
            while (low < high && compare(a[low], key) <= 0) low++;
            a[high] = a[low];
        }
        a[low] = key;
        return low;
    }

    int compare(int o1, int o2) {
        String v1 = Integer.toString(o1), v2 = Integer.toString(o2);
        int len1 = v1.length();
        int len2 = v2.length();
        int lim = len1 + len2;
        int k = 0;
        while (k < lim) {
            char c1 = k > len1 - 1 ? v2.charAt(k - len1) : v1.charAt(k);
            char c2 = k > len2 - 1 ? v1.charAt(k - len2) : v2.charAt(k);
            if (c1 != c2) return c2 - c1;
            k++;
        }
        return len1 - len2;
    }
}
