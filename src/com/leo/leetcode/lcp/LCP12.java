package com.leo.leetcode.lcp;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 为了提高自己的代码能力，小张制定了 LeetCode 刷题计划，他选中了 LeetCode 题库中的 n 道题，编号从 0 到 n-1，
 * 并计划在 m 天内按照题目编号顺序刷完所有的题目（注意，小张不能用多天完成同一题）。
 * 在小张刷题计划中，小张需要用 time[i] 的时间完成编号 i 的题目。
 * 此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。
 * 为了防止“小张刷题计划”变成“小杨刷题计划”，小张每天最多使用一次求助。
 * 我们定义 m 天中做题时间最多的一天耗时为 T（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 T是多少。
 * 限制：
 * 1、1 <= time.length <= 10^5
 * 2、1 <= time[i] <= 10000
 * 3、1 <= m <= 1000
 * 链接：https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua
 */
public class LCP12 {

    public static void main(String[] args) {
        // 3
        System.out.println(new LCP12().minTime(stringToIntegerArray("[1,2,3,3]"), 2));
        // 7
        System.out.println(new LCP12().minTime(stringToIntegerArray("[1,2,3,4,5,6,7,8,9,10]"), 5));
        // 0
        System.out.println(new LCP12().minTime(stringToIntegerArray("[999,999,999]"), 4));
        // 1
        System.out.println(new LCP12().minTime(stringToIntegerArray("[1,2]"), 1));
    }

    // greedy
    public int minTime(int[] time, int m) {
        int l = 0, r = 1_000_000_000, ret = 0, n = time.length;
        while (l <= r) {
            int mid = l + (r - l) / 2, d = 0;
            for (int i = 0; i < n; ) {
                int max = time[i++], sum = 0;
                d++;
                while (i < n && sum < mid) {
                    if (time[i] > max) {
                        sum += max;
                        max = time[i];
                    } else sum += time[i];
                    if (sum <= mid) i++;
                }
            }
            if (d > m) l = mid + 1;
            else {
                ret = mid;
                r = mid - 1;
            }
        }
        return ret;
    }
}
