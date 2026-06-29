# Nginx

## What is Nginx?

**Nginx** (Engine-X) is an open-source web server widely used as a **Reverse Proxy**, **Load Balancer**, and **HTTP Cache**. It sits in front of backend applications and manages incoming client requests.

Common deployment:

* Installed directly on a Linux server or VM.
* Deployed as an **Ingress Controller** in Kubernetes.

```text
Client
   │
   ▼
 Nginx
   │
   ▼
Backend Servers
```

---

## Main Purposes

* **Reverse Proxy** – Forwards requests to backend applications.
* **Load Balancing** – Distributes traffic across multiple servers.
* **SSL/TLS Termination** – Handles HTTPS encryption and decryption.
* **Static File Serving** – Delivers HTML, CSS, JavaScript, and images efficiently.
* **Caching** – Reduces backend workload and improves performance.

---

## How It Works

1. Nginx listens on **port 80 (HTTP)** or **443 (HTTPS)**.
2. It receives client requests.
3. Based on the configuration, it routes requests to the appropriate backend.
4. The backend processes the request and returns the response through Nginx.

---

## Core Configuration

### `upstream`

Defines backend servers.

```nginx
upstream backend {
    server 127.0.0.1:8000;
}
```

### `server`

Defines the listening port and domain.

```nginx
server {
    listen 80;
    server_name example.com;
}
```

### `location`

Matches request paths and forwards traffic.

```nginx
location / {
    proxy_pass http://backend;
}
```

---

## Load Balancing Methods

* **Round Robin** (default)
* **Least Connections**
* **IP Hash**

---

## Common Issues

* **502 Bad Gateway** (backend is down or unreachable)
* Incorrect `proxy_pass`
* Backend service not running
* Port mismatch
* SSL/TLS configuration errors

---

## Troubleshooting

Useful commands:

```bash
sudo nginx -t
sudo systemctl status nginx
sudo systemctl reload nginx
ss -ntpl
curl http://127.0.0.1:8000
tail -f /var/log/nginx/error.log
```

Important log files:

* `/var/log/nginx/access.log`
* `/var/log/nginx/error.log`

---

## Best Practices

* Always validate configuration before reloading:

```bash
sudo nginx -t
```

* Configure backend failover:

```nginx
server 127.0.0.1:8000 max_fails=2 fail_timeout=5s;
```

* Serve static files directly with Nginx.
* Enable HTTPS in production.
* Never expose backend servers directly to the Internet.

---