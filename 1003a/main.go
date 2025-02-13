package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		fmt.Scan(&L[i])
	}
	ans := 0
	cnt := make(map[int]int)
	for _, v := range L {
		cnt[v]++
		ans = max(ans, cnt[v])
	}
	fmt.Println(ans)
}
