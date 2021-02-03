package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
 * <p>
 * 例如：
 * [2,3,4]，中位数是 3
 * [2,3]，中位数是 (2 + 3) / 2 = 2.5
 * 给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
 * 你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
 * <p>
 * 提示：
 * 1、你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
 * 2、与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
 * <p>
 * 链接：https://leetcode-cn.com/problems/sliding-window-median
 */
public class Q480 {

    public static void main(String[] args) {
        // [-2147483648.00000,-2147483648.00000,-2147483648.00000,-2147483648.00000,-2147483648.00000,2147483647.00000
        // ,2147483647.00000,2147483647.00000,2147483647.00000,2147483647.00000,-2147483648.00000]
        System.out.println(Arrays.toString(new Q480().medianSlidingWindow(
                stringToIntegerArray("[-2147483648,-2147483648,2147483647,-2147483648,-2147483648,-2147483648,2147483647,2147483647,2147483647,2147483647,-2147483648,2147483647,-2147483648]")
                , 3)));
        // [1]
        System.out.println(Arrays.toString(new Q480().medianSlidingWindow(stringToIntegerArray("[1]"), 1)));
        // [1,-1,-1,3,5,6]
        System.out.println(Arrays.toString(new Q480().medianSlidingWindow(stringToIntegerArray("[1,3,-1,-3,5,3,6,7]"), 3)));
        // [2147483647]
        System.out.println(Arrays.toString(new Q480().medianSlidingWindow(stringToIntegerArray("[2147483647,2147483647]"), 2)));
        // [2.5]
        System.out.println(Arrays.toString(new Q480().medianSlidingWindow(stringToIntegerArray("[1,4,2,3]"), 4)));
    }

    Queue<Double> queueLeft;
    Queue<Double> queueRight;
    int limit_l;
    int limit_r;

    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] ret = new double[nums.length - k + 1];
        int flag = k & 1;
        limit_l = (k + 1) / 2;
        limit_r = k / 2;
        queueLeft = new PriorityQueue<>(limit_l + 1, (o1, o2) -> (int) (o2 - o1));
        queueRight = new PriorityQueue<>(limit_r + 1);
        for (int i = 0; i < k - 1; i++) addQueue(nums[i]);
        for (int i = k - 1; i < nums.length; i++) {
            if (i >= k) removeQueue(nums[i - k]);
            addQueue(nums[i]);
            if (flag == 0) {
                double v1 = queueLeft.isEmpty() ? 0 : queueLeft.peek(), v2 = queueRight.isEmpty() ? 0 : queueRight.peek();
                ret[i - k + 1] = (v1 + v2) / 2.0;
            } else {
                ret[i - k + 1] = queueLeft.isEmpty() ? 0 : queueLeft.peek();
            }
        }
        return ret;
    }

    void addQueue(double v) {
        while (!queueRight.isEmpty() && queueRight.peek() < v && queueLeft.size() < limit_l)
            queueLeft.add(queueRight.poll());
        if (queueLeft.size() < limit_l) {
            queueLeft.add(v);
        } else if (!queueLeft.isEmpty() && queueLeft.peek() > v) {
            queueRight.add(queueLeft.poll());
            queueLeft.add(v);
        } else {
            queueRight.add(v);
        }
    }

    void removeQueue(double v) {
        if (!queueLeft.isEmpty() && v <= queueLeft.peek()) queueLeft.remove(v);
        else if (!queueRight.isEmpty() && v >= queueRight.peek()) queueRight.remove(v);
    }
}
