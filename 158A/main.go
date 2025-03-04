package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(reader, &a, &b)

	arr := make([]int, a)
	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &arr[i])
	}
	k := arr[b-1]
	ans := 0
	for _, v := range arr {
		if v > 0 && v >= k {
			ans++
		}
	}
	fmt.Println(ans)
}
