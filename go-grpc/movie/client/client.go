package main

import (
	"context"
	"log"

	pb "github.com/rifannurmuhammad/go-grpc/movie/proto"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial(":6565", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %s", err)
	}
	defer conn.Close()

	client := pb.NewMovieServiceClient(conn)

	response, err := client.FindAll(context.Background(), &pb.Empty{})
	log.Printf("Response from server: %v \n", response)
}
