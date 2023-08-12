/*
 * 给你一个整数数组 nums 。一个子数组 [num1, nums2, ...] 的 和的绝对值 为 abs(nums1 + nums2 + ... ) 。
 * 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
 * abs(x) 定义如下：
 * 1、如果 x 是负整数，那么 abs(x) = -x 。
 * 2、如果 x 是非负整数，那么 abs(x) = x 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^4 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
 */
package main

import (
	"fmt"
	"util"
)

func maxAbsoluteSum(nums []int) int {
	var mx, mn, sm = 0, 0, 0
	for _, num := range nums {
		sm += num
		mx = max(mx, sm)
		mn = min(mn, sm)
	}
	return mx - mn
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	// 5
	fmt.Println(maxAbsoluteSum(LCUtil.StringToIntArray("[1, -3, 2, 3, -4]")))
	// 8
	fmt.Println(maxAbsoluteSum(LCUtil.StringToIntArray("[2, -5, 1, -4, 3, -2]")))
}
