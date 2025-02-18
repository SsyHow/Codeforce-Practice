package main

import "fmt"

func solve() {
	var b, c int
	fmt.Scan(&b, &c)
	fmt.Println((b+c-2)/c + 1)

}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
