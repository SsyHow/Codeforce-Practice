package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)

	if a == 2 {
		fmt.Println(4)
	} else if a&1 == 1 {
		fmt.Println(3)
	} else {
		fmt.Println(a - 2)
	}
}
