package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		fmt.Scan(&L[i])
	}
	l, r := 0, a-1
	ans := 0
	for l <= r {
		if L[l] > b {
			break
		}
		l += 1
		ans += 1
	}

	for l <= r {
		if L[r] > b {
			break
		}
		r -= 1
		ans += 1
	}
	fmt.Println(ans)
}
