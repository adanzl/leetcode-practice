/*
 * 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
 * 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
 * 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
 * 		为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。
 *		nums2 的长度为 n 。
 * 提示：
 * 1、nums1.length == m + n
 * 2、nums2.length == n
 * 3、0 <= m, n <= 200
 * 4、1 <= m + n <= 200
 * 5、-10^9 <= nums1[i], nums2[j] <= 10^9
 * 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？
 * 链接：https://leetcode.cn/problems/merge-sorted-array/
 */
package main

import (
	"fmt"
	. "util"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	i0, i1 := m-1, n-1
	for i := m + n - 1; i >= 0; i-- {
		if i0 >= 0 && i1 >= 0 {
			if nums1[i0] > nums2[i1] {
				nums1[i] = nums1[i0]
				i0--
			} else {
				nums1[i] = nums2[i1]
				i1--
			}
		} else if i0 >= 0 {
			nums1[i] = nums1[i0]
			i0--
		} else {
			nums1[i] = nums2[i1]
			i1--
		}
	}
}

func main() {
	var nums1 []int
	// [1,2,2,3,5,6]
	nums1 = StringToIntArray("[1,2,3,0,0,0]")
	merge(nums1, 3, StringToIntArray("[2,5,6]"), 3)
	fmt.Println(nums1)
	// [1]
	nums1 = StringToIntArray("[1]")
	merge(nums1, 1, StringToIntArray("[]"), 0)
	fmt.Println(nums1)
	// [1]
	nums1 = StringToIntArray("[0]")
	merge(nums1, 0, StringToIntArray("[1]"), 1)
	fmt.Println(nums1)
}
