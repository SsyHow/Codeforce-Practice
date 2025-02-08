package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	c := 0
	for i := 1; i <= a; i++ {
		var tmp int
		fmt.Scan(&tmp)
		c += tmp

	}
	if c < 0 {
		c = -c
	}
	fmt.Println((c + b - 1) / b)
}
