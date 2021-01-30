package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
 * 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
 * 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
 * <p>
 * 链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
 */
public class Q448 {

    public static void main(String[] args) {
        System.out.println(new Q448().findDisappearedNumbers(LCUtil.stringToIntegerArray("[4,3,2,7,8,2,3,1]"))); // [5,6]
        System.out.println(new Q448().findDisappearedNumbers(LCUtil.stringToIntegerArray("[1]"))); // []
        System.out.println(new Q448().findDisappearedNumbers(LCUtil.stringToIntegerArray("[2,2]"))); // [1]
    }

    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        go:
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i] - 1;
            while (true) {
                if (v == nums[v] - 1) {
                    continue go;
                }
                int t = v;
                v = nums[v] - 1;
                nums[t] = t + 1;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                ret.add(i + 1);
            }
        }
        return ret;
    }
}
