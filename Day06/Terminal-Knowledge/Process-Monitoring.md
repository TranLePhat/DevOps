# Process Monitoring

## 1. What is Process Monitoring?

Process Monitoring is the practice of observing, analyzing, and managing running processes on a Linux system using command-line tools such as `ps`, `top`, `htop`, `lsof`, and `strace`.

A process is simply a program that is currently being executed in memory.

---
## 2. Why is it Important?

Process monitoring helps identify system bottlenecks and application issues.

Common use cases:

* Detect high CPU usage
* Detect memory leaks
* Identify stuck or hung applications
* Find processes consuming excessive resources
* Troubleshoot production incidents

Without process monitoring, it is difficult to determine why a server becomes slow or unresponsive.

---
## 3. How Does It Work Internally?

Linux exposes process information through the **/proc pseudo-filesystem**.

Each running process has its own directory:

```bash
/proc/<PID>
```

Examples:

```bash
/proc/1234/status
/proc/1234/fd
/proc/1234/cmdline
```

The Linux kernel continuously updates these files.

Tools such as `ps`, `top`, and `lsof` simply read information from `/proc` and display it in a human-friendly format.

---
## 4. Core Components

### ps

Displays a snapshot of running processes.

```bash
ps aux
```

Useful information:

* PID
* CPU usage
* Memory usage
* Process state

---
### top

Real-time process monitoring tool.

```bash
top
```

Useful shortcuts:

* `P` → Sort by CPU usage
* `M` → Sort by Memory usage

---
### htop

Enhanced version of top with a more user-friendly interface.

```bash
htop
```

---
### lsof

Lists files, directories, sockets, and ports opened by a process.

```bash
lsof -p <PID>
```

Example:

```bash
lsof -i :80
```

---

### strace

Traces system calls made by a process.

```bash
strace -p <PID>
```

Useful when an application is hanging or behaving unexpectedly.

---
## 5. Dependencies and Related Concepts

Process Monitoring relies on:

### Process IDs

* PID (Process ID)
* PPID (Parent Process ID)

Example:

```bash
ps -ef
```

---
### Virtual Memory

Every process operates within its own virtual memory space managed by the kernel.

---
### Signals

Signals are used to communicate with processes.

Common signals:

| Signal       | Description       |
| ------------ | ----------------- |
| SIGTERM (15) | Graceful shutdown |
| SIGKILL (9)  | Force termination |
| SIGSTOP      | Pause process     |
| SIGCONT      | Resume process    |

Example:

```bash
kill <PID>
kill -9 <PID>
```

---
## 6. Common Misconceptions

### Process State D Means High CPU Usage

Wrong.

State `D` (Uninterruptible Sleep) means the process is waiting for I/O operations such as:

* Disk access
* Network storage
* Hardware response

It is not actively consuming CPU.

---
### Ignoring Threads

Sometimes the resource-consuming component is a thread rather than the main process.

Useful commands:

```bash
ps -eLf
```

or in top:

```text
Press H
```

to display threads.

---
## 7. Common Production Issues

### Zombie Processes

Zombie processes appear as:

```text
<defunct>
```

Cause:

* Child process exits
* Parent process fails to call wait()

Impact:

* Does not consume memory
* Consumes PID table entries

Large numbers of zombies can prevent new process creation.

---
### File Descriptor Leaks

Applications open files or sockets but never close them.

Symptoms:

```text
Too many open files
```

Check:

```bash
lsof -p <PID>
```

---
### Memory Leaks

An application continuously allocates memory without releasing it.

Symptoms:

* Increasing RAM usage
* Increasing Swap usage
* OOM Killer events

---
## 8. Troubleshooting Runbook

### Step 1: Identify the Problematic Process

```bash
top
```

or

```bash
htop
```

Find the PID consuming excessive CPU or Memory.

---
### Step 2: Inspect Open Files

```bash
lsof -p <PID>
```

Check:

* Open files
* Active network connections
* Listening ports

---
### Step 3: Trace the Process

```bash
strace -p <PID>
```

Identify:

* Infinite loops
* Waiting system calls
* Blocked database connections

---

### Step 4: Stop the Process

Graceful termination:

```bash
kill <PID>
```

Force termination:

```bash
kill -9 <PID>
```

---
## 9. Building a Simple Process Monitor

A basic process monitoring tool can be built using Bash or Python.

Steps:

1. Scan `/proc`
2. Find directories with numeric names (PIDs)
3. Read:

```bash
/proc/<PID>/status
```

4. Extract:

* Name
* State
* VmRSS (memory usage)

5. Display the data as a table

This is essentially how tools like `ps` and `top` work internally.

---
## Frequently Used Commands

```bash
ps aux

top

htop

lsof -p <PID>

lsof -i :80

strace -p <PID>

kill <PID>

kill -9 <PID>
```
