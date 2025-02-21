package main

import "fmt"

func solve() {
	var a int
	fmt.Scan(&a)
	c := make([]int, a)
	for i := 0; i < a; i++ {
		var tmp int
		fmt.Scan(&tmp)
		c[i] = tmp
	}

	fmt.Println(1, a)
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
