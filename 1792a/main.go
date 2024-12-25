package main

import "fmt"

func solve() {
	var n int
	fmt.Scan(&n)
	t := 0
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
		if a[i] == 1 {
			t++
		}
	}
	fmt.Println(n - t/2)
}
func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
