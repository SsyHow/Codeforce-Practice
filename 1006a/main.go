package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	var x int
	for i := 0; i < a; i++ {
		Fscan(in, &x)
		if x&1 == 0 {
			Print(x-1, " ")
		} else {
			Print(x, " ")
		}
	}
	Println()

}

func main() {
	run(os.Stdin, os.Stdout)
}
