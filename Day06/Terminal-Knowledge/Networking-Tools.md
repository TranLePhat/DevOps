# Networking Tools

## 1. What are Networking Tools?

Networking Tools are command-line utilities used to configure, analyze, troubleshoot, and monitor network connectivity on Linux systems.

They help administrators and engineers understand how systems communicate across networks, from network interfaces and IP addresses to DNS resolution and application-level connections.

---
## 2. Why are They Important?

Networking tools help answer a critical question:

```text
Why can't two systems communicate?
```

They help identify issues such as:

* Network connectivity failures
* Firewall restrictions
* DNS problems
* Routing issues
* Application ports not listening
* Packet loss and latency

Without these tools, troubleshooting network-related incidents becomes extremely difficult.

---
## 3. How Do They Work Internally?

Most networking tools interact directly with the Linux TCP/IP networking stack inside the kernel.

They typically:

* Create sockets
* Send specially crafted packets
* Query kernel networking tables
* Capture packets from network interfaces

Examples:

* `ping` sends ICMP Echo Requests
* `tcpdump` captures packets in promiscuous mode
* `ss` reads socket information from the kernel
* `dig` queries DNS servers

---
## 4. Core Components

### ip

Displays and manages network interfaces, IP addresses, and routing information.

```bash
ip a
```

Useful for:

* Checking IP addresses
* Viewing network interfaces
* Verifying interface status

---
### ping

Tests connectivity using ICMP.

```bash
ping 8.8.8.8
```

Useful for:

* Connectivity testing
* Latency measurement
* Basic network diagnostics

---
### ss

Displays sockets and listening ports.

```bash
ss -tulpn
```

Useful for:

* Checking open ports
* Identifying listening services
* Finding process ownership

---
### netstat

Legacy networking tool similar to ss.

```bash
netstat -tulpn
```

---
### lsof

Displays network connections and open files.

```bash
lsof -i
```

Example:

```bash
lsof -i :80
```

---
### tcpdump

Captures and analyzes network traffic.

```bash
sudo tcpdump -i eth0
```

Example:

```bash
sudo tcpdump -i eth0 port 80
```

Useful for:

* Packet analysis
* Connectivity troubleshooting
* Traffic inspection

---
### nc (Netcat)

The "Swiss Army Knife" of networking.

Examples:

```bash
nc -zv google.com 443
```

```bash
nc -l 8080
```

Common uses:

* Port testing
* TCP/UDP connections
* Temporary servers
* Data transfer

---
### dig

DNS troubleshooting tool.

```bash
dig google.com
```

---
### nslookup

Simple DNS query tool.

```bash
nslookup google.com
```

---
### host

Quick DNS lookup utility.

```bash
host google.com
```

---
## 5. Dependencies and Related Concepts

### OSI Model

Important layers:

* Layer 3: Network
* Layer 4: Transport

---
### TCP/IP Stack

Fundamental networking model used by Linux systems.

---
### IP Addressing

Must understand:

* IPv4
* IPv6
* Subnet Mask
* CIDR notation

---
### Default Gateway

Used to route traffic outside the local network.

---
### DNS

Resolves domain names into IP addresses.

Example:

```text
google.com
↓
142.x.x.x
```

---
### TCP vs UDP

#### TCP

* Reliable
* Connection-oriented
* Three-way handshake

Examples:

* HTTP
* HTTPS
* SSH
* MySQL

---
#### UDP

* Faster
* Connectionless
* No delivery guarantee

Examples:

* DNS
* VoIP
* Streaming

---
## 6. Common Misconceptions

### "Ping Fails = Server Is Down"

Incorrect.

Many production systems intentionally block ICMP traffic.

Example:

```text
Ping: Failed
Website: Working
```

Always verify using application ports.

Example:

```bash
nc -zv server 443
```

---
## 7. Common Production Issues

### Port Collision

Symptoms:

```text
Address already in use
```

Cause:

Another process is already listening on the port.

Check:

```bash
ss -tulpn
```

---
### Incorrect Bind Address

Application only listens on:

```text
127.0.0.1
```

instead of:

```text
0.0.0.0
```

Result:

The application works locally but cannot be accessed remotely.

Check:

```bash
ss -tulpn
```

---
### DNS Problems

Symptoms:

* Service cannot resolve hostnames
* External APIs become unreachable

Check:

```bash
dig domain.com
```

or

```bash
nslookup domain.com
```

---
### Firewall Blocking Traffic

Symptoms:

* Service is running
* Port is listening
* Clients cannot connect

Check:

```bash
sudo ufw status
```

or cloud firewall/security group rules.

---
## 8. Troubleshooting Runbook

### Scenario

A web server cannot connect to a database server.

---

### Step 1: Check Connectivity

```bash
ping <DB_IP>
```

If ICMP is blocked, continue to Step 2.

---
### Step 2: Check Port Accessibility

```bash
nc -zv <DB_IP> 3306
```

Possible results:

```text
succeeded
```

or

```text
connection refused
```

---
### Step 3: Verify Database Is Listening

On the database server:

```bash
ss -tulpn | grep 3306
```

Expected:

```text
0.0.0.0:3306
LISTEN
```

Bad:

```text
127.0.0.1:3306
```

---
### Step 4: Capture Traffic

```bash
sudo tcpdump -i eth0 port 3306
```

If no packets arrive:

* Firewall issue
* Routing issue
* Security group issue

---
## 9. Build It Yourself

Simple Client-Server Lab using Netcat.

### Terminal 1 (Server)

```bash
nc -l 8080
```

---
### Terminal 2 (Client)

Verify port:

```bash
ss -tulpn | grep 8080
```

Connect:

```bash
nc 127.0.0.1 8080
```

Send messages.

Anything typed in one terminal appears in the other.

This demonstrates a basic TCP client-server connection without writing any code.

---
## Frequently Used Commands

```bash
ip a

ping 8.8.8.8

ss -tulpn

netstat -tulpn

lsof -i

lsof -i :80

dig google.com

nslookup google.com

host google.com

nc -zv google.com 443

nc -l 8080

sudo tcpdump -i eth0
```
