# Forward Proxy

## What is a Forward Proxy?

A **Forward Proxy** is an intermediary server that represents clients inside a private network when accessing the Internet. Instead of connecting directly to a web server, all client requests are first sent to the proxy.

```
Client → Forward Proxy → Internet
```

---
## Main Purposes

* **Caching** – Stores frequently accessed content to reduce bandwidth and improve performance.
* **Content Filtering** – Blocks malicious or unauthorized websites and file types.
* **Client Anonymity (NAT)** – Hides clients' private IP addresses behind the proxy's public IP.

---
## How It Works

1. The client sends a request to the Forward Proxy.
2. The proxy checks security policies and cache.
3. If allowed, it forwards the request to the Internet using its own public IP.
4. The response is cached (if applicable) and returned to the client.

---
## Core Components

* Cache Engine
* Access Control / Filtering
* NAT
* Logging System

---
## Common Misconceptions

* **Forward Proxy ≠ VPN**
* Disabling proxy settings does **not** always bypass restrictions, since many organizations use **Transparent Proxy**.

---
## Common Issues

* Outdated cache (stale content)
* Incorrect ACL (Access Control List)
* Authentication failures
* SSL/TLS certificate issues

---
## Troubleshooting

Useful checks:

```bash
curl -x http://proxy:8080 http://example.com
tail -f /var/log/squid/access.log
```

Always verify:

* Access logs
* HTTP status codes
* ACL rules
* Cache hits/misses

---