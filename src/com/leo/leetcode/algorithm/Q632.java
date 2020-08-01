package com.leo.leetcode.algorithm;

import java.util.Arrays;
import java.util.List;

import com.leo.utils.LCUtil;

/**
 * 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
 * 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
 * 链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists
 * 注意:
 * 1、给定的列表可能包含重复元素，所以在这里升序表示 >= 。
 * 2、1 <= k <= 3500
 * 3、-105 <= 元素的值 <= 105
 * 4、对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
 * 链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists
 */
public class Q632 {

    public static void main(String[] args) {
        // [1,1]
        System.out.println(Arrays.toString(new Q632().smallestRange(LCUtil.stringToListListInt("[[1,2,3],[1,2,3],[1,2,3]]"))));
        // [20, 24]
        System.out.println(Arrays.toString(new Q632().smallestRange(LCUtil.stringToListListInt("[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]"))));
    }

    public int[] smallestRange(List<List<Integer>> nums) {
        int l = 105, r = -105;
        for (List<Integer> list : nums) {
            l = Math.min(l, list.get(list.size() - 1));
        }
        for (List<Integer> list : nums) {
            for (int v : list) {
                if (v >= l) {
                    r = Math.max(r, v);
                    break;
                }
            }
        }
        return new int[] { l, r };
    }
}