/*
 * 你会得到一个字符串 s (索引从 0 开始)，你必须对它执行 k 个替换操作。替换操作以三个长度均为 k 的并行数组给出：indices, sources,  targets。
 * 要完成第 i 个替换操作:
 * 1、检查 子字符串  sources[i] 是否出现在 原字符串 s 的索引 indices[i] 处。
 * 2、如果没有出现， 什么也不做 。
 * 3、如果出现，则用 targets[i] 替换 该子字符串。
 * 例如，如果 s = "abcd" ， indices[i] = 0 , sources[i] = "ab"， targets[i] = "eee" ，那么替换的结果将是 "eeecd" 。
 * 所有替换操作必须 同时 发生，这意味着替换操作不应该影响彼此的索引。测试用例保证元素间不会重叠 。
 * 例如，一个 s = "abc" ，  indices = [0,1] ， sources = ["ab"，"bc"] 的测试用例将不会生成，因为 "ab" 和 "bc" 替换重叠。
 * 在对 s 执行所有替换操作后返回 结果字符串 。
 * 子字符串 是字符串中连续的字符序列。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、k == indices.length == sources.length == targets.length
 * 3、1 <= k <= 100
 * 4、0 <= indexes[i] < s.length
 * 5、1 <= sources[i].length, targets[i].length <= 50
 * 6、s 仅由小写英文字母组成
 * 7、sources[i] 和 targets[i] 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/find-and-replace-in-string/
 */
package main

import (
	"fmt"
	"sort"
	"strings"
	. "util"
)

func findReplaceString(s string, indices []int, sources []string, targets []string) string {
	ans := ""
	pairs := make([][]int, 0)
	for i := 0; i < len(indices); i++ {
		pair := []int{indices[i], i}
		pairs = append(pairs, pair)
	}
	sort.Slice(pairs, func(i int, j int) bool {
		return pairs[i][0] < pairs[j][0]
	})
	for i, ii := 0, 0; i < len(s); {
		if ii < len(indices) && pairs[ii][0] == i {
			str := sources[pairs[ii][1]]
			if len(str) <= len(s)-i && strings.Compare(s[i:i+len(str)], str) == 0 {
				ans += targets[pairs[ii][1]]
				i += len(str)
			} else {
				ans += string(s[i])
				i++
			}
			ii += 1
		} else {
			ans += string(s[i])
			i++
		}
	}
	return ans
}

func main() {
	// "vbfrssozp"
	fmt.Println(findReplaceString("vmokgggqzp",
		StringToIntArray("[3,5,1]"),
		StringToStringArray("[\"kg\",\"ggq\",\"mo\"]"),
		StringToStringArray("[\"s\",\"so\",\"bfr\"]")))
	// "eeebffff"
	fmt.Println(findReplaceString("abcd",
		StringToIntArray("[0,2]"),
		StringToStringArray("[\"a\",\"cd\"]"),
		StringToStringArray("[\"eee\",\"ffff\"]")))
	// "eeecd"
	fmt.Println(findReplaceString("abcd",
		StringToIntArray("[0,2]"),
		StringToStringArray("[\"ab\",\"ec\"]"),
		StringToStringArray("[\"eee\",\"ffff\"]")))
}
