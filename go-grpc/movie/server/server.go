package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	pb "github.com/rifannurmuhammad/go-grpc/movie/proto"

	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 6565, "The server port")
)

type movieServer struct {
	pb.MovieMessageList
	pb.MovieMessage
	pb.UnimplementedMovieServiceServer
}

func (s *movieServer) FindAll(ctx context.Context, empty *pb.Empty) (*pb.MovieMessageList, error) {
	var movieMessages = []*pb.MovieMessage{
		&pb.MovieMessage{
			Title:    "Captain america",
			Author:   "Stan Lee",
			Isbn:     "1234567800",
			Category: "comic",
		},
		&pb.MovieMessage{
			Title:    "Iron Man",
			Author:   "Stan Lee",
			Isbn:     "1234567800",
			Category: "comic",
		},
	}

	return &pb.MovieMessageList{Movie: movieMessages}, nil
}

func (s *movieServer) AddMovie(ctx context.Context, MovieMessage *pb.MovieMessage) (*pb.MovieMessage, error) {
	fmt.Println("receive add movie")
	return MovieMessage, nil
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	log.Println("Starting server localhost:", *port)
	server := &movieServer{}
	grpcServer := grpc.NewServer()
	pb.RegisterMovieServiceServer(grpcServer, server)
	grpcServer.Serve(lis)
}
