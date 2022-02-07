package com.leo.leetcode.algorithm.q0000;

/**
 * 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
 * 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
 * 说明:
 * 为什么返回数值是整数，但输出的答案是数组呢?
 * 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
 * 你可以想象内部操作如下:
 * // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
 * int len = removeDuplicates(nums);
 * // 在函数里修改输入数组对于调用者是可见的。
 * // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
 * for (int i = 0; i < len; i++) {
 *     print(nums[i]);
 * }
 * 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
 */
public class Q80 {
    public static void main(String[] args) {
        System.out.println(new Q80().removeDuplicates(new int[]{1, 1, 1, 2, 2, 3})); // 5   1, 1, 2, 2, 3
        System.out.println(new Q80().removeDuplicates(new int[]{0, 0, 1, 1, 1, 1, 2, 3, 3})); // 7   0, 0, 1, 1, 2, 3, 3
        System.out.println(new Q80().removeDuplicates(new int[]{})); // 0
    }

    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int index = 0, count = 1;
        for (int v : nums) {
            nums[index] = v;
            if (index > 0 && nums[index - 1] == v) count++;
            else count = 1;
            if (index == 0 || count <= 2) index++;
        }
//        System.out.print(Arrays.toString(nums));
        return index;
    }
}
