package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscan(reader, &b)
	if b&1 == 0 {
		fmt.Print(1, " ", 3, " ")
		for i := 0; i < b-2; i++ {
			fmt.Print(2, " ")
		}
		fmt.Println()
	} else {
		for i := 0; i < b; i++ {
			fmt.Print(b, " ")
		}
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
