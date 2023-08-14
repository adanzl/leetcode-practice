/*
 * 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
 * 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 * 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
 * 提示：
 * 1、1 <= k <= nums.length <= 10^4
 * 2、-10^4 <= nums[i] <= 10^4
 * 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
 */
package main

import (
	"fmt"
	. "util"
)

func findKthLargest(nums []int, k int) int {
	return quickSelect(nums, 0, len(nums)-1, len(nums)-k)
}

// 快速选择
func quickSelect(arr []int, l, r, target int) int {
	if l == r {
		return arr[l]
	}
	start, end, v := l, r, arr[l]
	for l < r {
		for l < r && arr[r] >= v {
			r--
		}
		for l < r && arr[l] <= v {
			l++
		}
		arr[l], arr[r] = arr[r], arr[l]
	}
	arr[l], arr[start] = arr[start], arr[l]
	if l == target {
		return arr[l]
	} else if l < target {
		return quickSelect(arr, l+1, end, target)
	}
	return quickSelect(arr, start, l-1, target)
}

func main() {
	// 5
	fmt.Println(findKthLargest(StringToIntArray("[3,2,1,5,6,4]"), 2))
	// 4
	fmt.Println(findKthLargest(StringToIntArray("[3,2,3,1,2,4,5,5,6]"), 4))
	// 2
	fmt.Println(findKthLargest(StringToIntArray("[3,2]"), 2))
	// 3
	fmt.Println(findKthLargest(StringToIntArray("[3]"), 1))
}
