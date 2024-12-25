package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		var b, c int
		fmt.Scan(&b)
		c = b / 2020
		//fmt.Println(b, c)
		if c == 0 {
			fmt.Println("NO")
		} else if c*2020 <= b && b <= c*2021 {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}
