package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscan(reader, &b)
	var s string
	fmt.Fscan(reader, &s)
	ans := 0
	for _, x := range s {
		if x == 'U' {
			ans += 1

		}
	}
	if ans&1 == 1 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 1; i <= a; i++ {
		solve(reader)
	}
}
