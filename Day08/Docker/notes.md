# Docker Notes

## 1. Container

A **container** is an isolated runtime environment that shares the host operating system kernel.

### Key concepts

- **Docker Engine**: The runtime responsible for building and running containers.
- **Image**: A read-only template that contains the application, dependencies, libraries, and base operating system.
- **Container**: A running instance of an image.

Containers provide:

- Process isolation
- Lightweight virtualization
- Fast startup
- Consistent runtime across environments

---

## 2. Docker Basics

Docker is an open-source platform for packaging, distributing, and running applications inside containers.

### Common Commands

```bash
docker run hello-world
docker ps -a
docker images
docker logs <container-id>
docker exec -it <container-id> bash
docker stop <container-id>
docker start <container-id>
docker rm -f <container-id>
```

Run an Nginx container in detached mode:

```bash
docker run -d -p 8080:80 nginx
```

Test the service:

```bash
curl localhost:8080
```

---

## 3. Microservices with Docker

A microservice architecture splits an application into multiple independent services.

Example:

- Web
- API
- Database

Each service runs inside its own container.

### Benefits

- Independent deployment
- Easier scaling
- Better fault isolation
- Simplified debugging

### Debugging

```bash
docker ps -a
docker logs <container-id>
docker exec -it <container-id> bash
docker rm -f <container-id>
```

Container Exit Codes

- Exit code **0** → Normal termination
- Exit code **non-zero** → Application or configuration error

---

# 4. Dockerfile

A Dockerfile defines how to build a Docker image.

## Common Instructions

```dockerfile
FROM ubuntu:22.04
WORKDIR /app
COPY app.py .
RUN apt update && apt install -y python3
ENV APP_ENV=production
EXPOSE 8080
CMD ["python3","app.py"]
```

### Instruction Summary

| Instruction | Purpose |
|------------|---------|
| FROM | Base image |
| RUN | Execute commands during build |
| COPY | Copy files into image |
| WORKDIR | Set working directory |
| ENV | Environment variables |
| EXPOSE | Document listening port |
| CMD | Default startup command |
| ENTRYPOINT | Fixed executable |

---

## Docker Layer Cache

Docker builds images layer by layer.

To maximize cache efficiency:

- Copy dependency files first
- Install dependencies
- Copy application source code last

Example:

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
```

---

## Multi-stage Build

Use multiple build stages to reduce image size.

Example:

```dockerfile
FROM python:3.9 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .

CMD ["python","app.py"]
```

Benefits:

- Smaller images
- Better security
- Faster deployment

---

## Image Optimization

Best practices:

- Use lightweight images (Slim, Alpine)
- Combine RUN commands
- Remove unnecessary cache
- Use `.dockerignore`
- Order Dockerfile instructions for cache efficiency
- Prefer multi-stage builds

---

## Dockerized Application Workflow

```
Code
 ↓
Git Commit
 ↓
CI Pipeline
 ↓
Build Image
 ↓
Push Registry
 ↓
CD Pipeline
 ↓
Deploy Container
```

---

# 5. Docker Compose

Docker Compose manages multiple containers using a single YAML file.

Example services:

- API
- Database
- Redis
- Nginx

Advantages:

- One command deployment
- Shared networking
- Easy volume management
- Service dependency management

---

# 6. Docker Networking

Docker provides networking so containers can communicate.

## Bridge Network

- Default network
- Single-host communication
- NAT to external network

## Host Network

- Shares the host network stack
- Higher performance
- No network isolation

## Overlay Network

- Multi-host communication
- Used by Docker Swarm

## None Network

- No networking
- Fully isolated container

---

# 7. Docker Volumes

Containers are ephemeral.

Volumes provide persistent storage.

Common use cases:

- Databases
- Configuration files
- User uploads
- Logs

Benefits:

- Persistent data
- Easy backup
- Managed by Docker

---

# 8. Docker Swarm

Docker Swarm is Docker's native orchestration platform.

Components:

- Manager Node
- Worker Node
- Service
- Replica

Compose manages multiple containers on a single host.

Swarm manages containers across multiple hosts.

---

# 9. Docker Security

Security best practices:

- Scan images before deployment
- Use official images
- Run containers as non-root users
- Limit CPU and memory usage
- Mount root filesystem as read-only whenever possible
- Use tmpfs for temporary files

Security tools:

- Trivy
- Docker Scout
- Clair
- Snyk

---

# 10. Docker CI/CD

Typical pipeline:

```
Developer
      ↓
Git Repository
      ↓
CI Pipeline
      ↓
Build
      ↓
Test
      ↓
Push Image
      ↓
Deploy
```

Core components:

- Source Control (GitHub / GitLab)
- CI Pipeline (GitHub Actions, Jenkins, GitLab CI)
- Dockerfile
- Docker Registry

---

# 11. Docker Monitoring

Common monitoring stack:

- Prometheus
- Grafana
- cAdvisor

Capabilities:

- Metrics collection
- Dashboards
- Alerting
- Resource monitoring

---

# 12. Resource Optimization

Improve container efficiency by:

- Limiting CPU and memory
- Using lightweight images
- Regular runtime updates
- Adding HEALTHCHECK
- Removing unnecessary packages

---

# 13. Microservices Principles

Each service should have a single responsibility.

Key principles:

- Single Responsibility
- Loose Coupling
- Independent Deployment
- Separate Database per Service
- API-based Communication

---

# 14. Private Docker Registry

A private registry allows organizations to store Docker images securely.

Main features:

- Private image storage
- Authentication with htpasswd
- HTTPS using TLS certificates
- Image version management

Common workflow:

```text
Build Image
      ↓
Tag Image
      ↓
Login Registry
      ↓
Push Image
      ↓
Registry
      ↓
Pull Image
      ↓
Run Container
```

Useful commands:

```bash
docker login localhost:5000

docker tag myapp:latest localhost:5000/myapp:latest

docker push localhost:5000/myapp:latest

docker pull localhost:5000/myapp:latest
```

List repositories:

```bash
curl -k -u username:password https://localhost:5000/v2/_catalog
```

List image tags:

```bash
curl -k -u username:password https://localhost:5000/v2/myapp/tags/list
```

---

# Best Practices

- Use official base images
- Keep images as small as possible
- Never store secrets inside images
- Use environment variables or Docker Secrets
- Pin image versions instead of using `latest`
- Scan images regularly
- Use volumes for persistent data
- Use health checks
- Keep containers stateless whenever possible
- Follow the principle: **One Process per Container**