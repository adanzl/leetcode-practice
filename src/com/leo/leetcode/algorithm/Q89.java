package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
 * 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
 * 格雷编码序列必须以 0 开头。
 * 链接：https://leetcode-cn.com/problems/gray-code
 */
public class Q89 {

    public static void main(String[] args) {
        System.out.println(new Q89().grayCode(0)); // [0]
        System.out.println(new Q89().grayCode(1)); // [0,1]
        System.out.println(new Q89().grayCode(2)); // [0,1,3,2]
        System.out.println(new Q89().grayCode(3)); // [0,1,3,2,6,7,5,4]
        System.out.println(new Q89().grayCode(4)); // [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
    }

    public List<Integer> grayCode(int n) {
        List<Integer> out = new ArrayList<>(1 << n);
        out.add(0);
        int i = 0;
        while (i < n) {
            int len = out.size();
            for (int j = len - 1; j >= 0; j--) {
                int v = out.get(j) + (1 << i);
                out.add(v);
            }
            i++;
        }
        return out;
    }

}
