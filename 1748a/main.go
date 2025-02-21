package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		b := 0
		fmt.Scan(&b)
		fmt.Println((b + 1) / 2)
	}
}
