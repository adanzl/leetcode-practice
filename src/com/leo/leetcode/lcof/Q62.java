package com.leo.leetcode.lcof;

/**
 * 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
 * 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
 * 限制：
 * 1、1 <= n <= 10^5
 * 2、1 <= m <= 10^6
 * 链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
 */
public class Q62 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q62().lastRemaining(5, 3));
        // 2
        System.out.println(new Q62().lastRemaining(10, 17));
    }

    public int lastRemaining(int n, int m) {
        int ret = 0;
        for (int i = 2; i < n + 1; i++) {
            ret = (ret + m) % i;
        }
        return ret;
    }

}
