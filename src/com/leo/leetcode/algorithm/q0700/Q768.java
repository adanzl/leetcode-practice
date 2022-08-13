package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayDeque;
import java.util.Deque;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10^8。
 * arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
 * 我们最多能将数组分成多少块？
 * 注意:
 * 1、arr的长度在[1, 2000]之间。
 * 2、arr[i]的大小在[0, 10^8]之间。
 * 链接：https://leetcode.cn/problems/max-chunks-to-make-sorted-ii
 */
public class Q768 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q768().maxChunksToSorted(stringToIntegerArray("[1,1,0,0,1]")));
        // 1
        System.out.println(new Q768().maxChunksToSorted(stringToIntegerArray("[4,2,2,1,1]")));
        // 1
        System.out.println(new Q768().maxChunksToSorted(stringToIntegerArray("[5,4,3,2,1]")));
        // 4
        System.out.println(new Q768().maxChunksToSorted(stringToIntegerArray("[2,1,3,4,4]")));
        //
        System.out.println(new Q768().maxChunksToSorted(stringToIntegerArray("[2,1,3,1,4,4]")));
    }

    public int maxChunksToSorted(int[] arr) {
        Deque<Integer> s = new ArrayDeque<>();
        for (int num : arr) {
            if (s.isEmpty() || num >= s.peek()) s.push(num);
            else {
                int max = 0;
                while (!s.isEmpty() && num < s.peek()) max = Math.max(max, s.pop());
                s.push(max);
            }
        }
        return s.size();
    }
}
