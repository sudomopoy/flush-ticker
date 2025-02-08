package main

import (
	"flag"
	"fmt"
	"time"
)

func main() {
	serviceURL := flag.String("url", "", "The URL of the service")
	flag.Parse()

	if *serviceURL == "" {
		fmt.Println("url args not found")
		return
	}

	ticker := time.NewTicker(1 * time.Minute)
	defer ticker.Stop()
	tickClient := NewTickClient(*serviceURL)
	for {
		select {
		case <-ticker.C:
			tickClient.Tick()
		}
	}
}
