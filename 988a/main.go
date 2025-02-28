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
	cnt := 0
	L := make(map[int]bool)
	M := make([]int, b)
	pos := 0
	for i := 1; i <= a; i++ {
		var x int
		fmt.Fscan(reader, &x)
		pos += 1
		if _, x := L[x]; x {
			continue
		}
		M[cnt] = pos
		cnt += 1
		L[x] = true
		if cnt == b {
			break
		}

	}

	if cnt == b {
		fmt.Println("YES")
		for _, x := range M {
			fmt.Print(x, " ")
		}
		fmt.Println()
	} else {
		fmt.Println("NO")
	}
}
