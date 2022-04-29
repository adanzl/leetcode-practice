package com.leo.leetcode.algorithm.q0300;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
 * 注意：数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
 * 链接：https://leetcode-cn.com/problems/random-pick-index
 */
public class Q398 {

    public static void main(String[] args) {
        Q398 obj = new Q398(stringToIntegerArray("[1,2,3,3,3]"));
        // 2,3,4
        System.out.println(obj.pick(3));
        System.out.println(obj.pick(3));
        System.out.println(obj.pick(3));
        // 0
        System.out.println(obj.pick(1));
    }

    private final Map<Integer, List<Integer>> nMap = new HashMap<>();
    public Q398(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            nMap.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int pick(int target) {
        List<Integer> list = nMap.get(target);
        int index = (int) (Math.random() * list.size());
        return list.get(index);
    }
}
