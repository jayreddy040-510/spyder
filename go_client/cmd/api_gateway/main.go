package main

import (
	// "os"
	"fmt"
	"html"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/chat", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello %q", html.EscapeString(r.URL.Path))
		// fmt.Printf("%q hit\n", html.EscapeString(r.URL.Path))
	})

	log.Fatal(http.ListenAndServe(":8000", nil))
}
