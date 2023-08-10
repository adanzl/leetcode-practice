// import json
package LCUtil

import (
	"container/list"
	"encoding/json"
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	val   int
	left  *TreeNode
	right *TreeNode
}

func (node TreeNode) String() string {
	return TreeNodeToString(&node)
}

type ListNode struct {
	val  int
	next *ListNode
}

func (node ListNode) String() string {
	return ListNodeToString(&node)
}

func ArrayToTreeNode(_input []string) *TreeNode {
	if len(_input) == 0 {
		return nil
	}
	v, _ := strconv.Atoi(_input[0])
	root := TreeNode{v, nil, nil}
	q := list.New()
	q.PushBack(&root)
	index := 1
	for q.Len() > 0 {
		f := q.Front()
		q.Remove(f)
		node := f.Value.(TreeNode)
		if index == len(_input) {
			break
		}
		item := strings.TrimSpace(_input[index])
		index += 1
		if item != "null" {
			left_num, _ := strconv.Atoi(item)
			node.left = &TreeNode{left_num, nil, nil}
			q.PushBack(node.left)
		}
		if index == len(_input) {
			break
		}
		item = strings.TrimSpace(_input[index])
		index += 1
		if item != "null" {
			right_num, _ := strconv.Atoi(item)
			node.right = &TreeNode{right_num, nil, nil}
			q.PushBack(node.right)
		}
	}
	return &root
}

func StringToTreeNode(_input string) *TreeNode {
	_input = strings.TrimSpace(_input)
	_input = _input[1 : len(_input)-1]
	if len(_input) == 0 {
		return nil
	}
	return ArrayToTreeNode(strings.Split(_input, ","))
}

func StringListToStrArray(l *list.List) []string {
	ret := make([]string, l.Len())
	i := 0
	for e := l.Front(); e != nil; e = e.Next() {
		ret[i] = e.Value.(string)
	}
	return ret
}

func TreeNodeToString(root *TreeNode) string {
	if root == nil {
		return "[]"
	}
	ret := list.New()
	q := list.New()
	q.PushBack(root)
	for q.Len() > 0 {
		node := q.Front()
		q.Remove(node)
		if node.Value == nil {
			ret.PushBack("null")
			continue
		}
		ret.PushBack(strconv.Itoa(node.Value.(TreeNode).val))
		q.PushBack(node.Value.(TreeNode).left)
		q.PushBack(node.Value.(TreeNode).right)
	}
	for ret.Len() > 0 {
		if ret.Back().Value == "null" {
			ret.Remove(ret.Back())
		} else {
			break
		}
	}
	return strings.Join(StringListToStrArray(ret), ",")
}

func StringToInt2dArray(input string) [][]int {
	var ret [][]int
	err := json.Unmarshal([]byte(input), &ret)
	if err != nil {
		fmt.Println("解析 JSON 出错:", err)
		return nil
	}
	return ret
}

func StringToIntArray(input string) []int {
	input = strings.Trim(input, " \t\n")
	input = input[1 : len(input)-1]
	if len(input) == 0 {
		return []int{}
	}
	parts := strings.Split(input, ",")
	ret := make([]int, len(parts))
	for i := 0; i < len(parts); i++ {
		ret[i], _ = strconv.Atoi(strings.TrimSpace(parts[i]))
	}
	return ret
}

func TreeNodeListToString(treeNodeList *list.List) string {
	if treeNodeList == nil {
		return "[]"
	}
	ret := list.New()
	for e := treeNodeList.Front(); e != nil; e = e.Next() {
		ret.PushBack(TreeNodeToString(e.Value.(*TreeNode)))
	}
	return "[" + strings.Join(StringListToStrArray(ret), ",") + "]"
}

func StringToListNode(_input string) *ListNode {
	_input = strings.TrimSpace(_input)
	_input = _input[1 : len(_input)-1]
	if len(_input) == 0 {
		return nil
	}
	nodeValues := strings.Split(_input, ",")

	dummyRoot := &ListNode{0, nil}
	ptr := dummyRoot
	for _, item := range nodeValues {
		v, _ := strconv.Atoi(item)
		ptr.next = &ListNode{v, nil}
		ptr = ptr.next
	}
	return dummyRoot.next
}

func ListNodeToString(node *ListNode) string {
	if node == nil {
		return "[]"
	}
	ret := list.New()
	for node != nil {
		ret.PushBack(strconv.Itoa(node.val))
		node = node.next
	}
	return "[" + strings.Join(StringListToStrArray(ret), ",") + "]"
}
