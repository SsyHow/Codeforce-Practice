package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	if a != 1 {
		fmt.Println(a, a)
	} else {
		fmt.Println(-1)
	}
}
