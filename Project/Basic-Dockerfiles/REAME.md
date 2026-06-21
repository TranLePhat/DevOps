# Basic Dockerfile

## Objective

Create a simple Docker image using Dockerfile and run a container that prints:

```text
Hello, Captain!
```

## Dockerfile

```dockerfile
FROM alpine:latest

CMD ["echo", "Hello, Captain!"]
```

## Build Image

```bash
docker build -t hello-caption .
```

### Build Result

![Build Result](screenshots/Build%20image.png)

## Verify Image

```bash
docker images
```

### Available Images

![Docker Images](screenshots/Images.png)

## Run Container

```bash
docker run hello-caption
```

### Container Output

![Container Output](screenshots/Output.png)
