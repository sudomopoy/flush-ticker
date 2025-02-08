package main

import (
	"context"
	"log"
	"time"

	pb "github.com/sudomopoy/flush-ticker/gen/go/tick/v1"
	"google.golang.org/grpc"
)

type GrpcClient struct {
	conn         *grpc.ClientConn
	tickerClient pb.TickerClient
}

func NewTickClient(url string) (*GrpcClient, error) {
	conn, err := grpc.Dial(url, grpc.WithInsecure(), grpc.WithBlock(), grpc.WithTimeout(5*time.Second))
	if err != nil {
		return nil, err
	}

	client := pb.NewTickerClient(conn)
	return &GrpcClient{conn, client}, nil
}

func (c *GrpcClient) Tick() (*pb.TickResponse, error) {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	req := &pb.TickRequest{}

	return c.tickerClient.Tick(ctx, req)
}

func (c *GrpcClient) Close() error {
	return c.conn.Close()
}

func main() {
	client, err := NewTickClient("localhost:8080")
	if err != nil {
		log.Fatalf("failed to create client: %v", err)
	}
	defer client.Close()

	resp, err := client.Tick()
	if err != nil {
		log.Fatalf("failed to call Tick: %v", err)
	}
	log.Printf("Tick response: %v", resp)
}
