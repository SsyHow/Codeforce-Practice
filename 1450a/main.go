package main

import (
	"fmt"
	"strings"
)

func solve() {
	var b int
	var s string
	fmt.Scan(&b)
	fmt.Scan(&s)
	c := strings.Count(s, "b")
	ans := strings.Repeat("b", c)

	for _, j := range s {
		if j != 'b' {
			ans += string(j)
		}

	}
	fmt.Println(ans)
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
