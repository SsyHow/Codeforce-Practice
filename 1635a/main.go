package main

import "fmt"

func solve() {
	var b, ans int
	fmt.Scan(&b)
	for i := 1; i <= b; i++ {
		var c int
		fmt.Scan(&c)
		ans |= c
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
