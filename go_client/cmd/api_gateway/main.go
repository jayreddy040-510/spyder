package main

import (
	"context"
	"log"
	"net/http"

	pb "github.com/jayreddy040-510/spyder"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	listenAddr := "localhost:8080"
	gRPCAddress := "localhost:50051"

	// Set up a connection to the gRPC server.
	conn, err := grpc.Dial(gRPCAddress, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("couldnt connect to gRPC server: %v", err)
	}
	defer conn.Close()

	chatClient := pb.NewChatServiceClient(conn)

	http.HandleFunc("/chat", func(w http.ResponseWriter, r *http.Request) {
		message := r.URL.Query().Get("msg")
		model := r.URL.Query().Get("model")

		// Prepare gRPC request
		req := &pb.ChatRequest{
			Msg:   message,
			Model: model,
		}

		// Call gRPC method
		resp, err := chatClient.GetChat(context.Background(), req)
		if err != nil {
			http.Error(w, "error calling gRPC server: "+err.Error(), http.StatusInternalServerError)
			return
		}

		// Write response
		w.Write([]byte(resp.Msg))
	})

	log.Printf("Server listening at %v", listenAddr)
	log.Fatal(http.ListenAndServe(listenAddr, nil))
}
