package com.leo.leetcode.lcci;

import java.util.Arrays;

/**
 * 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
 * 返回的长度需要从小到大排列。
 * 提示：
 * 1、0 < shorter <= longer
 * 2、0 <= k <= 100000
 * 链接：https://leetcode-cn.com/problems/diving-board-lcci
 */
public class Q1611 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q1611().divingBoard(1, 2, 3))); // [3,4,5,6]
        System.out.println(Arrays.toString(new Q1611().divingBoard(1, 2, 0))); // []
        System.out.println(Arrays.toString(new Q1611().divingBoard(1, 2, 100000))); // []
    }

    public int[] divingBoard(int shorter, int longer, int k) {
        if (k == 0) return new int[0];
        if (shorter == longer) return new int[]{shorter * k};
        int count = k + 1;
        int[] ret = new int[count];
        ret[count - 1] = longer * k;
        for (int i = count - 2; i >= 0; i--) ret[i] = ret[i + 1] + shorter - longer;
        return ret;
    }
}
