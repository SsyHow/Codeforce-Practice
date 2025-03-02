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
	var b string
	var ans int
	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &b)
		if b == "++X" || b == "X++" {
			ans += 1
		} else {
			ans -= 1
		}
	}
	fmt.Println(ans)
}
