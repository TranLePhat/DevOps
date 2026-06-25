# Container

## What is a Container?

A **Container** is a standardized software package that bundles an application together with all of its dependencies, libraries, configuration files, and runtime environment into a single unit.

Unlike a Virtual Machine (VM), a container performs **Operating System-level virtualization**. Multiple containers share the same Linux kernel while remaining isolated from one another.

---

## Why do we need Containers?

Containers solve one of the biggest problems in software deployment:

> "It works on my machine."

Because the application and its dependencies are packaged together, the runtime environment becomes consistent across development, testing, staging, and production.

Containers also provide:

* Fast startup (milliseconds)
* Lightweight resource usage
* High deployment density
* Easy scaling for Microservices
* Portable deployments across environments

---

## Before Containers

Before containers became popular, applications were typically deployed inside **Virtual Machines (VMs)**.

Each VM required:

* A Hypervisor
* A complete Guest Operating System
* Separate system libraries
* Large storage space
* Longer boot time

This approach provided strong isolation but consumed significantly more CPU, memory, and storage.

---

## How Containers Work

Containers are **not virtual computers**.

Instead, they are simply Linux processes running inside isolated environments created by the operating system.

A container shares the Host's Linux kernel but receives its own isolated view of:

* Processes
* Network interfaces
* File system
* Hostname
* Users
* IPC resources

From inside the container, it appears as if it owns an independent operating system, while in reality it is sharing the same kernel with other containers.

---

## Core Components

### Image

A read-only template containing:

* Base operating system
* Application code
* Dependencies
* Configuration

An Image acts as the blueprint for creating containers.

---

### Container Runtime

The runtime is responsible for executing an Image as a running container.

Examples include:

* Docker Engine
* containerd
* CRI-O
* Podman
* LXC

---

## Linux Technologies Behind Containers

Containers are built using several Linux kernel features.

### 1. Namespaces

Provide isolation between containers.

Examples include:

* PID Namespace
* Network Namespace
* Mount Namespace
* User Namespace
* IPC Namespace

Each container receives its own isolated environment.

---

### 2. Control Groups (cgroups)

Limit and manage hardware resources.

Examples:

* CPU
* Memory
* Disk I/O
* Network bandwidth

Without cgroups, one container could consume all host resources.

---

### 3. Union File System (UnionFS)

Provides layered filesystems.

Multiple containers can share identical read-only layers while writing only their own changes, reducing storage usage and improving efficiency.

---

## Common Misconceptions

### Container = Lightweight Virtual Machine

False.

Virtual Machines virtualize hardware.

Containers virtualize the operating system.

---

### Container Data is Permanent

False.

Containers are **ephemeral**.

Deleting a container also removes its internal filesystem unless persistent storage (Volumes) is used.

---

## Common Production Issues

### Resource Starvation

Running containers without CPU or memory limits may allow one faulty application to consume all host resources.

Typical causes include:

* Memory leaks
* Infinite loops
* Heavy CPU workloads

---

### Data Loss

Running databases inside containers without Persistent Volumes may result in permanent data loss after the container is removed.

---

## Debugging Containers

Common debugging steps include:

### View application logs

```bash
docker logs <container>
```

---

### Enter a running container

```bash
docker exec -it <container> bash
```

or

```bash
docker exec -it <container> sh
```

---

### Inspect container configuration

```bash
docker inspect <container>
```

---

### View running containers

```bash
docker ps
```

---

### Advanced Debugging

For low-level troubleshooting, Linux tools such as **nsenter** can attach directly to a container's namespaces from the host system.

---

## Build a Simple Container from Scratch

To understand the underlying concepts without Docker:

1. Create a fake root filesystem using **chroot**.
2. Create isolated namespaces using the Linux `clone()` system call.
3. Configure CPU and memory limits through **cgroups**.
4. Launch a process inside the isolated environment.

This demonstrates that Docker is essentially an automation layer built on top of Linux kernel features.

---

## Key Takeaways

* Containers package applications and dependencies into a portable unit.
* Containers share the Host Linux Kernel.
* Containers are lightweight compared to Virtual Machines.
* Linux Namespaces provide isolation.
* cgroups manage hardware resources.
* Union File Systems optimize image storage.
* Containers are ephemeral unless persistent storage is used.
* Docker is a container platform, not the container technology itself.
