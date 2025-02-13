package main

import "fmt"

func solve() {
	var b int
	fmt.Scan(&b)
	L := make([]int, b)
	for i := 0; i < b; i++ {
		fmt.Scan(&L[i])
	}

	for i := 1; i < b-1; i++ {
		if L[i-1] < L[i] && L[i] > L[i+1] {
			fmt.Println("YES")
			fmt.Println(i, i+1, i+2)
			return
		}

	}

	fmt.Println("NO")

}
func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
