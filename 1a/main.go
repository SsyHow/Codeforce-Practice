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
	var a, b, c int
	fmt.Fscan(reader, &a, &b, &c)
	n := (a + c - 1) / c
	m := (b + c - 1) / c
	fmt.Println(m * n)
}
