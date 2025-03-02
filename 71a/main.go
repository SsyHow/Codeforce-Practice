package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b string
	fmt.Fscan(reader, &b)
	n := len(b)
	if n <= 10 {
		fmt.Println(b)
	} else {
		fmt.Printf("%c", b[0])
		fmt.Print(n-2, "")
		fmt.Printf("%c", b[n-1])
		fmt.Println()
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
