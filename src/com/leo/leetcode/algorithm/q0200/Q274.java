package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
 * h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
 * 且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。
 * 例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
 * 提示：如果 h 有多种可能的值，h 指数是其中最大的那个。
 * 链接：https://leetcode-cn.com/problems/h-index
 */

public class Q274 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q274().hIndex(stringToIntegerArray("[1,7,9,4]")));
        // 2
        System.out.println(new Q274().hIndex(stringToIntegerArray("[11,11,0,0]")));
        // 2
        System.out.println(new Q274().hIndex(stringToIntegerArray("[11,15]")));
        // 1
        System.out.println(new Q274().hIndex(stringToIntegerArray("[3]")));
        // 0
        System.out.println(new Q274().hIndex(stringToIntegerArray("[0]")));
        // 1
        System.out.println(new Q274().hIndex(stringToIntegerArray("[3,1]")));
        // 3
        System.out.println(new Q274().hIndex(stringToIntegerArray("[3,0,6,1,5]")));
        // 1
        System.out.println(new Q274().hIndex(stringToIntegerArray("[1,3,1]")));
        // 1
        System.out.println(new Q274().hIndex(stringToIntegerArray("[1,1,1]")));
    }

    public int hIndex(int[] citations) {
        int count = 0, pre = 0, len = citations.length;
        int[] marks = new int[citations.length + 1];
        for (int c : citations) marks[Math.min(c, len)]++;
        for (int i = len; i > 0; i--) {
            count += marks[i];
            if (count >= i) return Math.max(pre, i);
            pre = count;
        }
        return count;
    }
}
