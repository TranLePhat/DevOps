# Reverse Proxy

## What is a Reverse Proxy?

A **Reverse Proxy** is an intermediary server that sits in front of one or more backend servers. It receives requests from clients and forwards them to the appropriate backend service.

```text
Client → Reverse Proxy → Backend Server
```

Common reverse proxy software:

* Nginx
* Apache HTTP Server
* HAProxy
* Traefik

---
## Main Purposes

* **Traffic Routing** – Routes requests to different backend services based on domain names or URL paths.
* **Caching** – Serves static content (HTML, CSS, JavaScript, images) to reduce backend workload.
* **Security** – Hides backend servers from direct Internet access.
* **Load Balancing** – Distributes traffic across multiple backend servers.

---
## How It Works

1. A client sends a request to the Reverse Proxy.
2. The proxy examines the request (host, URL, headers).
3. It forwards the request to the correct backend server using `proxy_pass`.
4. The backend processes the request and returns the response through the proxy.

---
## Core Components

* **server** – Defines the listening port and domain name.
* **location** – Matches URL paths.
* **proxy_pass** – Specifies the backend server destination.

Example:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://localhost:8000;
    }
}
```

---
## Common Misconceptions

* **Reverse Proxy ≠ Forward Proxy**

  * Forward Proxy represents **clients**.
  * Reverse Proxy represents **servers**.
* A Reverse Proxy is **not only** a Load Balancer. It also provides routing, caching, SSL termination, and security.

---
## Common Issues

* **502 Bad Gateway** (backend is down or unreachable)
* Incorrect `proxy_pass`
* Backend service not running
* Wrong listening port
* SSL/TLS configuration issues

---
## Troubleshooting

Useful commands:

```bash
ss -ntpl
curl http://127.0.0.1:8000
systemctl status nginx
tail -f /var/log/nginx/error.log
```

Always verify:

* Backend service status
* Backend port
* `proxy_pass` configuration
* Nginx error logs

---
