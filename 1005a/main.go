package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		fmt.Scan(&L[i])
	}
	L = append(L, 1)
	var ans []int
	//fmt.Println(L)
	for i := 1; i <= a; i++ {
		if L[i] <= L[i-1] {
			ans = append(ans, L[i-1])
		}
	}
	fmt.Println(len(ans))
	for _, v := range ans {
		fmt.Print(v, " ")
	}
	fmt.Println()
}
