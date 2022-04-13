package com.leo.leetcode.algorithm.q1800;

/**
 * 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
 * 1、nums.length == n
 * 2、nums[i] 是 正整数 ，其中 0 <= i < n
 * 3、abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
 * 4、nums 中所有元素之和不超过 maxSum
 * 5、nums[index] 的值被 最大化
 * 返回你所构造的数组中的 nums[index] 。
 * 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
 * 提示：
 * 1、1 <= n <= maxSum <= 10^9
 * 2、0 <= index < n
 * 链接：https://leetcode-cn.com/problems/maximum-value-at-a-given-index-in-a-bounded-array
 */
public class Q1802 {

    public static void main(String[] args) {
        // 271698267
        System.out.println(new Q1802().maxValue(3, 0, 815094800));
        // 1
        System.out.println(new Q1802().maxValue(8, 2, 8));
        // 2
        System.out.println(new Q1802().maxValue(4, 2, 6));
        // 3
        System.out.println(new Q1802().maxValue(6, 1, 10));
    }

    public int maxValue(int n, int index, int maxSum) {
        int l = 1, r = maxSum, ret = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long sum = 0, lLen = Math.min(mid, index + 1), rLen = Math.min(n - index, mid);
            sum += (mid + mid - lLen + 1) * lLen / 2 + Math.max(0, index - lLen + 1);
            sum += (mid + mid - rLen + 1) * rLen / 2 + Math.max(0, n - rLen -index);
            sum -= mid;
            if (sum <= maxSum) {
                l = mid + 1;
                ret = mid;
            } else r = mid - 1;
        }
        return ret;
    }
}


