package com.leo.leetcode.algorithm.q1600;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 等差数列 。更正式地，数列 s 是等差数列，只需要满足：对于每个有效的 i ， s[i+1] - s[i] == s[1] - s[0] 都成立。
 * 例如，下面这些都是 等差数列 ：
 * 1, 3, 5, 7, 9
 * 7, 7, 7, 7
 * 3, -1, -5, -9
 * 下面的数列 不是等差数列 ：
 * 1, 1, 2, 5, 7
 * 给你一个由 n 个整数组成的数组 nums，和两个由 m 个整数组成的数组 l 和 r，后两个数组表示 m 组范围查询，其中第 i 个查询对应范围 [l[i], r[i]] 。
 * 所有数组的下标都是 从 0 开始 的。
 * 返回 boolean 元素构成的答案列表 answer 。如果子数组 nums[l[i]], nums[l[i]+1], ... , nums[r[i]] 可以 重新排列 形成 等差数列 ，answer[i] 的值就是 true；否则answer[i] 的值就是 false 。
 * 提示：
 * 1、n == nums.length
 * 2、m == l.length
 * 3、m == r.length
 * 4、2 <= n <= 500
 * 5、1 <= m <= 500
 * 6、0 <= l[i] < r[i] < n
 * 7、-10^5 <= nums[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/arithmetic-subarrays
 */
public class Q1630 {

    public static void main(String[] args) {
        // [true,false,true]
        System.out.println(new Q1630().checkArithmeticSubArrays(
                stringToIntegerArray("[4,6,5,9,3,7]"),
                stringToIntegerArray("[0,0,2]"),
                stringToIntegerArray("[2,3,5]")));
        // [false,true,false,false,true,true]
        System.out.println(new Q1630().checkArithmeticSubArrays(
                stringToIntegerArray("[-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]"),
                stringToIntegerArray("[0,1,6,4,8,7]"),
                stringToIntegerArray("[4,4,9,7,9,10]")));
    }

    public List<Boolean> checkArithmeticSubArrays(int[] nums, int[] l, int[] r) {
        List<Boolean> ret = new ArrayList<>();
        for (int i = 0; i < l.length; i++) {
            int s = l[i], e = r[i];
            int[] arr = new int[e - s + 1];
            System.arraycopy(nums, s, arr, 0, arr.length);
            Arrays.sort(arr);
            boolean ans = true;
            for (int j = 1; j < arr.length; j++) {
                if (arr[j] - arr[j - 1] != arr[1] - arr[0]) {
                    ans = false;
                    break;
                }
            }
            ret.add(ans);
        }
        return ret;
    }
}
