package main

import "fmt"

func solve(b, c int) {
	fmt.Println(min(min(b, c), (b+c)/4))
}

func main() {
	var a, b, c int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		fmt.Scan(&b, &c)
		//fmt.Println(b, c)
		solve(b, c)
	}
}
