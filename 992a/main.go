package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	L := make(map[int]bool)
	for i := 1; i <= a; i++ {
		x := 0
		fmt.Fscan(reader, &x)
		if x != 0 {
			L[x] = true
		}
	}
	fmt.Println(len(L))

}
