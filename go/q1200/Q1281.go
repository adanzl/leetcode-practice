/*
 * 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
 */
package main

import (
	"fmt"
)

func subtractProductAndSum(n int) int {
	var product, sum int = 1, 0
	for n > 0 {
		product *= n % 10
		sum += n % 10
		n /= 10
	}
	return product - sum
}

func main() {
	// 15
	fmt.Println(subtractProductAndSum(234))
	// 21
	fmt.Println(subtractProductAndSum(4421))
}
