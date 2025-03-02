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
	var x, y, z, ans int

	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &x, &y, &z)
		if x+y+z > 1 {
			ans += 1
		}
	}
	fmt.Println(ans)
}
