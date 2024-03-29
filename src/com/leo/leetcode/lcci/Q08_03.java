package com.leo.leetcode.lcci;

/**
 * 魔术索引。 
 * 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
 * 给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。
 * 若有多个魔术索引，返回索引值最小的一个。
 * 提示: nums长度在[1, 1000000]之间
 * 链接：https://leetcode-cn.com/problems/magic-index-lcci
 */
public class Q08_03 {

    public static void main(String[] args) {
        System.out.println(new Q08_03().findMagicIndex(new int[] { 0, 2, 3, 4, 5 })); // 0
        System.out.println(new Q08_03().findMagicIndex(new int[] { 1, 1, 1, 1 })); // 1
    }

    public int findMagicIndex(int[] nums) {
        int flag = 0;
        while (flag < nums.length) {
            if (nums[flag] == flag) {
                return flag;
            } else if (nums[flag] > flag) { // 重点 , 过滤掉不需要比较的元素
                flag = nums[flag];
            } else {
                flag++;
            }
        }
        return -1;
    }
}