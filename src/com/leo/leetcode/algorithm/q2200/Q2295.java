package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的数组 nums ，它包含 n 个 互不相同 的正整数。
 * 请你对这个数组执行 m 个操作，在第 i 个操作中，你需要将数字 operations[i][0] 替换成 operations[i][1] 。
 * 题目保证在第 i 个操作中：
 * 1、operations[i][0] 在 nums 中存在。
 * 2、operations[i][1] 在 nums 中不存在。
 * 请你返回执行完所有操作后的数组。
 * 提示：
 * 1、n == nums.length
 * 2、m == operations.length
 * 3、1 <= n, m <= 10^5
 * 4、nums 中所有数字 互不相同 。
 * 5、operations[i].length == 2
 * 6、1 <= nums[i], operations[i][0], operations[i][1] <= 10^6
 * 7、在执行第 i 个操作时，operations[i][0] 在 nums 中存在。
 * 8、在执行第 i 个操作时，operations[i][1] 在 nums 中不存在。
 * 链接：https://leetcode.cn/problems/replace-elements-in-an-array
 */
public class Q2295 {

    public static void main(String[] args) {
        // [3,2,7,1]
        System.out.println(Arrays.toString(new Q2295().arrayChange(stringToIntegerArray("[1,2,4,6]"), stringToInt2dArray("[[1,3],[4,7],[6,1]]"))));
        // [2,1]
        System.out.println(Arrays.toString(new Q2295().arrayChange(stringToIntegerArray("[1,2]"), stringToInt2dArray("[[1,3],[2,1],[3,2]]"))));

    }

    public int[] arrayChange(int[] nums, int[][] operations) {
        Map<Integer, Integer> nMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            nMap.put(nums[i], i);
        }
        for (int[] op : operations) {
            nums[nMap.get(op[0])] = op[1];
            nMap.put(op[1], nMap.get(op[0]));
            nMap.remove(op[0]);
        }
        return nums;
    }
}
