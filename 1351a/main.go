package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		fmt.Println(x + y)
	}
}
