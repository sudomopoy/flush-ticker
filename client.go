package main

import (
	"context"
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
