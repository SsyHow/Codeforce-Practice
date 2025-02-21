package main

import "fmt"

func solve() {
	var b, c int
	fmt.Scan(&b, &c)

	if (b-c)&1 == 1 {
		fmt.Println(-1)
	} else if b == c && b == 0 {
		fmt.Println(0)
	} else if b == c {
		fmt.Println(1)
	} else {
		fmt.Println(2)
	}

}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
