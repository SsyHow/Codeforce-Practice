package main

import "fmt"

func solve() {
	var a int
	fmt.Scan(&a)
	var b, c string
	fmt.Scan(&b)
	fmt.Scan(&c)
	r := 0
	k := 0
	for i := 0; i < a; i++ {
		if b[i] > c[i] {
			r++
		} else if b[i] < c[i] {
			k++
		}
	}

	if r == k {
		fmt.Println("EQUAL")
	} else if r > k {
		fmt.Println("RED")
	} else {
		fmt.Println("BLUE")
	}
}
func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
