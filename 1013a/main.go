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
	var x, L, M int
	for i := 0; i < a; i++ {
		Fscan(in, &x)
		L += x
	}
	for i := 0; i < a; i++ {
		Fscan(in, &x)
		M += x
	}
	if L >= M {
		Println("YES")
	} else {
		Println("NO")
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
