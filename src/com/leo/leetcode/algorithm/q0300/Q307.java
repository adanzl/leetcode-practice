package com.leo.leetcode.algorithm.q0300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个数组 nums ，请你完成两类查询。
 * 其中一类查询要求 更新 数组 nums 下标对应的值
 * 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
 * 实现 NumArray 类：
 * 1、NumArray(int[] nums) 用整数数组 nums 初始化对象
 * 2、void update(int index, int val) 将 nums[index] 的值 更新 为 val
 * 3、int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （
 * 即，nums[left] + nums[left + 1], ..., nums[right]）
 * 提示：
 * 1、1 <= nums.length <= 3 * 10^4
 * 2、-100 <= nums[i] <= 100
 * 3、0 <= index < nums.length
 * 4、-100 <= val <= 100
 * 5、0 <= left <= right < nums.length
 * 6、调用 update 和 sumRange 方法次数不大于 3 * 10^4
 * 链接：https://leetcode-cn.com/problems/range-sum-query-mutable
 */
public class Q307 {
    // 线段树
    public static void main(String[] args) {
        NumArray numArray = new NumArray(stringToIntegerArray("[-28,-39,53,65,11,-56,-65,-39,-43,97]"));
        System.out.println(numArray.sumRange(5, 6)); // -121
        numArray.update(9, 27);
        System.out.println(numArray.sumRange(2, 3)); // 118
        System.out.println(numArray.sumRange(6, 7)); // -104
        numArray.update(1, -82);
        numArray.update(3, -72);
        System.out.println(numArray.sumRange(3, 7)); // -221
        System.out.println(numArray.sumRange(1, 8)); // -293
        numArray.update(5, 13);
        numArray.update(4, -67);
        System.out.println("===========================");
        numArray = new NumArray(stringToIntegerArray("[9,-8]"));
        numArray.update(0, 3);
        System.out.println(numArray.sumRange(1, 1)); // -8
        System.out.println(numArray.sumRange(0, 1)); // -5
        numArray.update(1, -3);
        System.out.println(numArray.sumRange(0, 1)); // 0
        System.out.println("===========================");
        numArray = new NumArray(stringToIntegerArray("[1, 3, 5]"));
        System.out.println(numArray.sumRange(0, 2)); // 返回 1 + 3 + 5 = 9
        numArray.update(1, 2);   // nums = [1,2,5]
        System.out.println(numArray.sumRange(0, 2)); // 返回 1 + 2 + 5 = 8
    }
}

class NumArray {

    private final int[][] bArr;
    private final int[] nums;

    public NumArray(int[] nums) {
        bArr = new int[nums.length << 2][4]; // l-r-v-d
        this.nums = nums;
        // build tree
        this.buildTree(0, 0, nums.length - 1);
    }

    private int buildTree(int root, int l, int r) {
        bArr[root][0] = l;
        bArr[root][1] = r;
        if (l == r) return bArr[root][2] = nums[l];
        int mid = (l + r) >> 1, sl = (root << 1) + 1, sr = sl + 1;
        int lv = buildTree(sl, l, mid);
        int rv = buildTree(sr, mid + 1, r);
        return bArr[root][2] = lv + rv;
    }

    public void update(int index, int val) {
        set(0, index, val);
    }

    private void set(int root, int idx, int val) {
        int[] rn = bArr[root];
        if (rn[0] == rn[1]) {
            rn[2] = val;
            return;
        }
        int mid = (rn[0] + rn[1]) >> 1, sl = (root << 1) + 1, sr = sl + 1;
        if (idx > mid) set(sr, idx, val);
        else set(sl, idx, val);
        rn[2] = bArr[sl][2] + bArr[sr][2];
    }

    public int sumRange(int left, int right) {
        return query(0, left, right);
    }

    private int query(int root, int l, int r) {
        int[] rn = bArr[root];
        if (rn[0] == l && rn[1] == r) return rn[2];
        int mid = (rn[0] + rn[1]) >> 1, sl = (root << 1) + 1, sr = sl + 1;
        if (r <= mid) return query(sl, l, r);
        if (l >= mid + 1) return query(sr, l, r);
        return query(sl, l, mid) + query(sr, mid + 1, r);
    }
}
