package com.leo.leetcode.algorithm.q0600;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
 * 整数 a 比整数 b 更接近 x 需要满足：
 * 1、|a - x| < |b - x| 或者
 * 2、|a - x| == |b - x| 且 a < b
 * 提示：
 * 1、1 <= k <= arr.length
 * 2、1 <= arr.length <= 10^4
 * 3、arr 按 升序 排列
 * 4、-10^4 <= arr[i], x <= 10^4
 * 链接：https://leetcode-cn.com/problems/find-k-closest-elements
 */
public class Q658 {

    public static void main(String[] args) {
        // [10]
        System.out.println(new Q658().findClosestElements(stringToIntegerArray("[1,1,1,10,10,10]"), 1, 9));
        // [1,2,3,4]
        System.out.println(new Q658().findClosestElements(stringToIntegerArray("[1,2,3,4,5]"), 4, 3));
        // [1,2,3,4]
        System.out.println(new Q658().findClosestElements(stringToIntegerArray("[1,2,3,4,5]"), 4, -1));
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ret = new ArrayList<>(k);
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (x <= arr[mid]) r = mid - 1;
            else l = mid + 1;
        }
        int count = 0, p1 = l - 1, p2 = l;
        while (p1 >= 0 && p2 <= arr.length - 1 && count < k) {
            if (Math.abs(arr[p1] - x) <= Math.abs(arr[p2] - x)) p1--;
            else p2++;
            count++;
        }
        if (p1 >= 0) p1 -= k - count;
        if (p2 < arr.length) p2 += k - count;
        for (int i = p1 + 1; i < p2; i++) ret.add(arr[i]);
        return ret;
    }
}
