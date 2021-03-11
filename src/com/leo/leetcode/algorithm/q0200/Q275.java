package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。
 * h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
 * （其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
 * <p>
 * 说明: 如果 h 有多有种可能的值 ，h 指数是其中最大的那个。
 * 进阶：
 * 1、这是 H 指数 的延伸题目，本题中的 citations 数组是保证有序的。
 * 2、你可以优化你的算法到对数时间复杂度吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/h-index-ii
 */
public class Q275 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q275().hIndex(stringToIntegerArray("[0]")));
        // 1
        System.out.println(new Q275().hIndex(stringToIntegerArray("[1,1,1]")));
        // 1
        System.out.println(new Q275().hIndex(stringToIntegerArray("[1]")));
        // 2
        System.out.println(new Q275().hIndex(stringToIntegerArray("[0,0,11,11]")));
        // 4
        System.out.println(new Q275().hIndex(stringToIntegerArray("[0,1,4,4,4,4]")));
        // 3
        System.out.println(new Q275().hIndex(stringToIntegerArray("[0,1,3,5,6]")));
        // 2
        System.out.println(new Q275().hIndex(stringToIntegerArray("[1,2,100]")));
    }

    public int hIndex(int[] citations) {
        int len = citations.length, l = 0, r = len;
        while (l < r) {
            int mid = l + ((r - l) >> 1), n = len - mid;
            if (citations[mid] >= n) r = mid;
            else l = mid + 1;
        }
        return l < len ? Math.min(len - l, citations[l]) : len - l;
    }
}
