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
	var a, b int
	Fscan(in, &a, &b)
	L := make([]int, a)
	M := make([]int, b)
	ans := 0
	k := 0
	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	for i := 0; i < b; i++ {
		Fscan(in, &M[i])
	}

	for i := 0; i < a; i++ {
		if k < b && L[i] <= M[k] {
			ans += 1
			k += 1
		}
	}
	Println(ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}
