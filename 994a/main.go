package main

import "fmt"

func contain(k int, s []int) bool {
	for _, v := range s {
		if v == k {
			return true
		}
	}
	return false
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	L := make([]int, a)
	M := make([]int, b)
	for i := 0; i <= a-1; i++ {
		fmt.Scan(&L[i])
	}
	for i := 0; i <= b-1; i++ {
		fmt.Scan(&M[i])
	}
	//fmt.Println(L)
	for _, v := range L {
		if contain(v, M) {
			fmt.Print(v, " ")
		}
	}
	fmt.Println()

}
