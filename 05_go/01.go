package main

import (
	"fmt"
	"reflect"
	"strconv"
)

func main() {
	var vName string = "Advaith"
	var v1, v2 = 1, 2
	fmt.Println(vName, v1, v2)
	v1 = 3
	fmt.Println(v1)

	// int, float64, bool, string, rune
	fmt.Println(reflect.TypeOf(24))
	fmt.Println(reflect.TypeOf(24.33))
	fmt.Println(reflect.TypeOf(true))
	fmt.Println(reflect.TypeOf("Advaith"))

	// converting
	cV1 := 1.4
	cV2 := int(cV1)
	fmt.Println(cV2)

	cV3 := "2"
	cV4, err := strconv.Atoi(cV3)
	fmt.Println(cV4, err, reflect.TypeOf(cV4))

	cV5 := 50
	cV6 := strconv.Itoa(cV5)
	fmt.Println(cV6, reflect.TypeOf(cV6))

	cV7 := "3.14"
	if cV8, err := strconv.ParseFloat(cV7, 64); err == nil {
		fmt.Println(cV8, reflect.TypeOf(cV8))
	}

	// string format
	cV9 := fmt.Sprintf("%f Pie", 3.14)
	fmt.Println(cV9)
}
