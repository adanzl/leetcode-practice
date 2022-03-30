package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
 * 珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。
 * 如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
 * 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
 * 返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
 * 提示：
 * 1、1 <= piles.length <= 10^4
 * 2、piles.length <= H <= 10^9
 * 3、1 <= piles[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/koko-eating-bananas
 */
public class Q875 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q875().minEatingSpeed(stringToIntegerArray("[2,2]"), 2));
        // 4
        System.out.println(new Q875().minEatingSpeed(stringToIntegerArray("[3,6,7,11]"), 8));
        // 30
        System.out.println(new Q875().minEatingSpeed(stringToIntegerArray("[30,11,23,4,20]"), 5));
        // 23
        System.out.println(new Q875().minEatingSpeed(stringToIntegerArray("[30,11,23,4,20]"), 6));
    }

    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 1000_000_000;
        while (l <= r) {
            int mid = l + ((r - l) >> 1), sum = 0;
            for (int pile : piles) {
                sum += pile / mid;
                if (pile % mid != 0) sum++;
                if (sum > h) break;
            }
            if (sum > h) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}
