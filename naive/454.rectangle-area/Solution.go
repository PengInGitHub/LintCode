package main

import (
	"fmt"
)

func main() {
	r := Rectangle{}
	r.NewRectangle(5, 20)
	fmt.Println(r.getArea())
}

type Rectangle struct {
	weight int
	height int
}

//made mistake here
//forgot pointer
//func (r Rectangle) NewRectangle(w, h int) {
func (r *Rectangle) NewRectangle(w, h int) {
	r.weight = w
	r.height = h
}

func (r Rectangle) getArea() int {
	return r.weight * r.height
}
