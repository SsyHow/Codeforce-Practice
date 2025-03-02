package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var s, t string
	fmt.Fscan(reader, &s, &t)
	//fmt.Println(s, t)
	n, m := len(s), len(t)

	c := min(n, m)
	i := -1
	for i >= -c {
		if s[n+i] != t[m+i] {
			break
		}
		i -= 1
	}
	fmt.Println(n + m + i + i + 2)
}
