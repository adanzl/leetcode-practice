package com.leo.leetcode.algorithm.q0100;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
 * 你需要按照以下要求，帮助老师给这些孩子分发糖果：
 * 1、每个孩子至少分配到 1 个糖果。
 * 2、评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
 * 那么这样下来，老师至少需要准备多少颗糖果呢？
 * <p>
 * 链接：https://leetcode-cn.com/problems/candy
 */
public class Q135 {

    public static void main(String[] args) {
        // 9
        System.out.println(new Q135().candy(stringToIntegerArray("[1,2,3,1,0]")));
        // 13
        System.out.println(new Q135().candy(stringToIntegerArray("[1,2,87,87,87,2,1]")));
        // 7
        System.out.println(new Q135().candy(stringToIntegerArray("[1,3,2,2,1]")));
        // 5
        System.out.println(new Q135().candy(stringToIntegerArray("[1,0,2]")));
        // 4
        System.out.println(new Q135().candy(stringToIntegerArray("[1,2,2]")));
    }

    public int candy(int[] ratings) {
        if (ratings.length == 0) return 0;
        int ret = 1, pre = 1;
        int[] candy = new int[ratings.length];
        Arrays.fill(candy, 1);
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                pre++;
            } else {
                if (ratings[i] < ratings[i - 1] && pre == 1) {
                    int l = i;
                    while (l > 0 && ratings[l - 1] > ratings[l] && candy[l - 1] - candy[l] < 1) {
                        l--;
                        candy[l]++;
                    }
                    ret += (i - l);
                }
                pre = 1;
            }
            candy[i] = pre;
            ret += pre;

        }
        return ret;
    }
}
