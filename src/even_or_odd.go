package main

import "fmt"

func isEven(num int) bool {
    return num % 2 == 0
}

func main() {
    testNumbers := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    for _, num := range testNumbers {
        fmt.Printf("%d is ", num)
        if isEven(num) {
            fmt.Println("even")
        } else {
            fmt.Println("odd")
        }
    }
}
