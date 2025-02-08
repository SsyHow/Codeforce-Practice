package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	c := 0
	for i := 0; i < a; i++ {
		var b int
		fmt.Scan(&b)
		if b > 0 {
			c += b
		} else {
			c -= b
		}
	}
	fmt.Println(c)
}
