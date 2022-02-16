package com.leo.leetcode.algorithm.q0200;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个无重复元素的有序整数数组 nums 。
 * 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
 * 也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
 * 列表中的每个区间范围 [a,b] 应该按如下格式输出：
 * "a->b" ，如果 a != b
 * "a" ，如果 a == b
 * 提示：
 * 1、0 <= nums.length <= 20
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * 3、nums 中的所有值都 互不相同
 * 4、nums 按升序排列
 * 链接：https://leetcode-cn.com/problems/summary-ranges
 */
public class Q228 {

    public static void main(String[] args) {
        // ["0->2","4->5","7"]
        System.out.println(new Q228().summaryRanges(stringToIntegerArray("[0,1,2,4,5,7]")));
        // ["0","2->4","6","8->9"]
        System.out.println(new Q228().summaryRanges(stringToIntegerArray("[0,2,3,4,6,8,9]")));
        // []
        System.out.println(new Q228().summaryRanges(stringToIntegerArray("[]")));
        // ["-1"]
        System.out.println(new Q228().summaryRanges(stringToIntegerArray("[-1]")));
        // ["0"]
        System.out.println(new Q228().summaryRanges(stringToIntegerArray("[0]")));
    }

    public List<String> summaryRanges(int[] nums) {
        List<String> ret = new ArrayList<>();
        if (nums.length == 0) return ret;
        int pre = nums[0], start = pre, len = 1;
        for (int i = 1; i < nums.length; i++) {
            if (pre != nums[i] - 1) {
                if (len == 1) ret.add(String.valueOf(start));
                else ret.add(start + "->" + pre);
                len = 1;
                start = nums[i];
            } else {
                len++;
            }
            pre = nums[i];
        }
        if (len == 1) ret.add(String.valueOf(start));
        else ret.add(start + "->" + pre);
        return ret;
    }
}
