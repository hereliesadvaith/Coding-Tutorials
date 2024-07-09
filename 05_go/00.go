package main

import (
	"bufio"
	"fmt"
	f "fmt"
	"log"
	"os"
)

var print = f.Println

func main() {
	fmt.Println("Hello there")
	print("What is your name ?")
	reader := bufio.NewReader(os.Stdin)
	name, err := reader.ReadString('\n')
	if err == nil {
		print("Hello", name)
	} else {
		log.Fatal(err)
	}
}
