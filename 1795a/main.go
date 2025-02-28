package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b, c int
	fmt.Fscan(reader, &b, &c)
	m, n := 0, 0

	for i := 0; i < b; i++ {
		var x, y int
		fmt.Fscan(reader, &x, &y)
		if x == c {
			m = 1
		}
		if y == c {
			n = 1
		}
	}
	if m == 1 && n == 1 {
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
