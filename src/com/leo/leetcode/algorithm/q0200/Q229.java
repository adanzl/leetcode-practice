package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
 * 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
 * <p>
 * 提示：
 * 1、1 <= nums.length <= 5 * 10^4
 * 2、-10^9 <= nums[i] <= 10^9
 * <p>
 * 链接：https://leetcode-cn.com/problems/majority-element-ii
 */
public class Q229 {

    public static void main(String[] args) {
        // []
        System.out.println(new Q229().majorityElement(stringToIntegerArray("[1,2,3,4]")));
        // [3]
        System.out.println(new Q229().majorityElement(stringToIntegerArray("[3,2,3]")));
        // [3]
        System.out.println(new Q229().majorityElement(stringToIntegerArray("[3,2,3,3,3,3,3]")));
        // [1]
        System.out.println(new Q229().majorityElement(stringToIntegerArray("[1]")));
        // [1,2]
        System.out.println(new Q229().majorityElement(stringToIntegerArray("[1,1,1,3,3,2,2,2]")));
        // []
        System.out.println(new Q229().majorityElement(stringToIntegerArray("[]")));
    }

    public List<Integer> majorityElement(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        int c0 = 0, c1 = 0, v0 = 0, v1 = 0, sum0 = 0, sum1 = 0;
        for (int n : nums) {
            if (c0 > 0 && c1 > 0 && n != v0 && n != v1) {
                c0--;
                c1--;
            } else {
                if (c0 > 0 && n == v0) c0++;
                else if (c1 > 0 && n == v1) c1++;
                else if (c0 == 0) {
                    c0 = 1;
                    v0 = n;
                } else {
                    c1 = 1;
                    v1 = n;
                }
            }
        }
        for (int n : nums) {
            if (n == v0) sum0++;
            else if (n == v1) sum1++;
        }
        if (sum0 > nums.length / 3) ret.add(v0);
        if (sum1 > nums.length / 3) ret.add(v1);
        return ret;
    }
}
