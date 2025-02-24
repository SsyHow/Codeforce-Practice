package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	ans := 0
	for a > 0 {
		if a >= 100 {
			ans += a / 100
			a %= 100
		}
		if a >= 20 {
			ans += a / 20
			a %= 20
		}
		if a >= 10 {
			ans += a / 10
			a %= 10
		}
		if a >= 5 {
			ans += a / 5
			a %= 5
		}
		if a >= 1 {
			ans += a / 1
			a %= 1
		}

	}
	fmt.Println(ans)
}
