package com.leo.leetcode.algorithm.q2000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 下标从 0 开始 的整数数组 candies 。数组中的每个元素表示大小为 candies[i] 的一堆糖果。
 * 你可以将每堆糖果分成任意数量的 子堆 ，但 无法 再将两堆合并到一起。
 * 另给你一个整数 k 。你需要将这些糖果分配给 k 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。
 * 返回每个小孩可以拿走的 最大糖果数目 。
 * 提示：
 * 1、1 <= candies.length <= 10^5
 * 2、1 <= candies[i] <= 10^7
 * 3、1 <= k <= 10^12
 * 链接：https://leetcode-cn.com/problems/maximum-candies-allocated-to-k-children
 */
public class Q2226 {
    public static void main(String[] args) {
        // 5
        System.out.println(new Q2226().maximumCandies(stringToIntegerArray("[5,8,6]"), 3));
        // 3
        System.out.println(new Q2226().maximumCandies(stringToIntegerArray("[5,6,4,10,10,1,1,2,2,2]"), 9));
        // 3
        System.out.println(new Q2226().maximumCandies(stringToIntegerArray("[4,7,5]"), 4));
        // 0
        System.out.println(new Q2226().maximumCandies(stringToIntegerArray("[2,5]"), 11));
    }

    public int maximumCandies(int[] candies, long k) {
        int l = 1, r = 10_000_000, ret = 0;
        while (l <= r) {
            int mid = (l + r) >> 1;
            long count = 0;
            for (int candy : candies) count += (long) candy / mid;
            if (count < k) r = mid - 1;
            else {
                l = mid + 1;
                ret = mid;
            }
        }
        return ret;
    }
}
