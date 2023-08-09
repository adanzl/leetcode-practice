/*
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 p 。
 * 请你从 nums 中找到 p 个下标对，每个下标对对应数值取差值，你需要使得这 p 个差值的 最大值 最小。
 * 同时，你需要确保每个下标在这 p 个下标对中最多出现一次。
 * 对于一个下标对 i 和 j ，这一对的差值为 |nums[i] - nums[j]| ，其中 |x| 表示 x 的 绝对值 。
 * 请你返回 p 个下标对对应数值 最大差值 的 最小值 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= p <= (nums.length)/2
 * 链接：https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/
 */
package main

import (
	"fmt"
	"sort"
	"util"
)

func minimizeMax(nums []int, p int) int {
	var ans = 0
	sort.Ints(nums)
	var l, r = 0, nums[len(nums)-1] - nums[0]
	for l <= r {
		mid := (l + r) >> 1
		cnt := 0
		for i := 1; i < len(nums); {
			if nums[i]-nums[i-1] <= mid {
				cnt++
				i += 2
			} else {
				i++
			}
		}
		if cnt >= p {
			ans = mid
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return ans
}

func main() {
	// 1
	fmt.Println(minimizeMax(LCUtil.StringToIntArray("[10, 1, 2, 7, 1, 3]"), 2))
	// 0
	fmt.Println(minimizeMax(LCUtil.StringToIntArray("[4, 2, 1, 2]"), 1))
	//
	// fmt.Println(minimizeMax())
}
