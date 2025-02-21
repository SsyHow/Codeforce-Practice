package main

import "fmt"

func solve() {
	var b int
	fmt.Scan(&b)
	fmt.Println(b / 2)
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
