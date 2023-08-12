/*
 * 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
 * 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
 * 提示：
 * 1、n == mat.length == mat[i].length
 * 2、1 <= n <= 100
 * 3、1 <= mat[i][j] <= 100
 * 链接：https://leetcode-cn.com/problems/matrix-diagonal-sum/
 */
package main

import (
	"fmt"
	LCUtil "util"
)

func diagonalSum(mat [][]int) int {
	n := len(mat)
	var ans = 0
	for i := 0; i < n; i++ {
		ans += mat[i][i] + mat[i][n-i-1]
	}
	if n%2 == 1 {
		ans -= mat[n/2][n/2]
	}
	return ans
}

func main() {
	// 25
	fmt.Println(diagonalSum(LCUtil.StringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]")))
	// 8
	fmt.Println(diagonalSum(LCUtil.StringToInt2dArray("[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]")))
	// 5
	fmt.Println(diagonalSum(LCUtil.StringToInt2dArray("[[5]]")))
}
