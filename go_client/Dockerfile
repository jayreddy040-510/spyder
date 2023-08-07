
FROM golang:latest AS builder
WORKDIR /spyder
COPY go.mod go.sum ./
RUN go mod download
COPY ./go_client ./go_client

# debugging
RUN ls -R
# build the application
RUN go build -o api_gateway ./go_client/cmd/api_gateway/main.go

# use a lightweight image for the final image
FROM busybox:latest
WORKDIR /root/
COPY --from=builder /spyder/api_gateway .

EXPOSE 8080
CMD ["./api_gateway"]
