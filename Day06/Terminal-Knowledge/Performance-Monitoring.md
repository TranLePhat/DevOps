# Performance Monitoring

## 1. What is Performance Monitoring?

Performance Monitoring is the practice of measuring, tracking, and analyzing overall system resource utilization, including:

* CPU usage
* Memory (RAM) usage
* Swap usage
* Disk I/O performance
* System load

The goal is to understand the health and performance of a Linux system in real time or through historical metrics.

---
## 2. Why is it Important?

Performance monitoring helps identify system bottlenecks.

It answers questions such as:

* Why is the server slow?
* Is CPU overloaded?
* Is memory exhausted?
* Is the system swapping?
* Is disk I/O saturated?

Without monitoring, troubleshooting becomes guesswork.

---
## 3. How Does It Work Internally?

Linux exposes performance metrics through the **/proc pseudo-filesystem**.

Examples:

```bash
/proc/loadavg
/proc/meminfo
/proc/stat
/proc/vmstat
```

The Linux kernel continuously updates these files.

Monitoring tools simply read and process this information to provide human-readable statistics.

---
## 4. Core Components

### uptime

Displays system uptime and load average.

```bash
uptime
```

Example:

```text
load average: 0.42, 0.31, 0.25
```

Represents average system load during:

* Last 1 minute
* Last 5 minutes
* Last 15 minutes

---
### free

Displays memory and swap usage.

```bash
free -h
```

Useful fields:

* Total
* Used
* Free
* Available
* Swap

---
### vmstat

Displays virtual memory statistics.

```bash
vmstat 1
```

Useful columns:

| Column | Description       |
| ------ | ----------------- |
| si     | Swap In           |
| so     | Swap Out          |
| wa     | I/O Wait          |
| b      | Blocked Processes |

---
### iostat

Displays disk performance statistics.

```bash
iostat -xz 1
```

Useful for:

* Disk utilization
* Read/write throughput
* Disk latency

---
### iotop

Displays processes performing disk I/O.

```bash
sudo iotop
```

Useful for identifying disk-intensive processes.

---
### pidstat

Displays CPU, memory, and I/O usage per process over time.

```bash
pidstat 1
```

Useful for historical process monitoring.

---

## 5. Dependencies and Related Concepts

### Virtual Memory

Linux provides each process with its own virtual memory space.

---
### Page Faults

Occur when requested memory pages are not currently available in RAM.

---
### Disk Caching

Linux uses unused RAM as filesystem cache to improve disk performance.

---
### CPU Scheduler

The kernel scheduler determines which processes receive CPU time.

---
## 6. Common Misconceptions

### High Load Average Means High CPU Usage

Incorrect.

Load Average includes:

* Running processes
* Processes waiting for CPU
* Processes blocked waiting for I/O

A high Load Average may indicate disk bottlenecks rather than CPU problems.

---
### Low Free Memory Means the Server Is Running Out of RAM

Incorrect.

Linux intentionally uses free RAM for filesystem cache.

Focus on:

```bash
free -h
```

Specifically:

```text
available
```

rather than:

```text
free
```

---
## 7. Common Production Issues

### Thrashing

Occurs when physical memory is exhausted.

The kernel continuously swaps pages between RAM and disk.

Symptoms:

* High Swap In/Out
* Slow system response
* High I/O wait

Check:

```bash
vmstat 1
```

Watch:

```text
si
so
```

---
### Disk I/O Bottleneck

Occurs when storage cannot keep up with application requests.

Common causes:

* Database workloads
* Heavy logging
* Backup jobs

Symptoms:

* High I/O wait
* Slow application response

Check:

```bash
iostat -xz 1
```

and

```bash
iotop
```

---
### Memory Pressure

Applications consume memory faster than the system can provide it.

Symptoms:

* High memory usage
* Swap activity
* OOM Killer events

Check:

```bash
free -h
```

and

```bash
vmstat 1
```

---
## 8. Troubleshooting Runbook

### Step 1: Check System Load

```bash
uptime
```

Look for unusually high Load Average.

---
### Step 2: Check Memory Usage

```bash
free -h
```

Look at:

* Available memory
* Swap usage

---
### Step 3: Check Swap Activity

```bash
vmstat 1
```

Watch:

```text
si
so
```

Continuous activity usually indicates memory pressure.

---
### Step 4: Check Disk Wait

```bash
vmstat 1
```

Watch:

```text
wa
b
```

High values indicate disk-related bottlenecks.

---
### Step 5: Identify Disk Usage

```bash
iostat -xz 1
```

and

```bash
sudo iotop
```

Find:

* Busy disks
* Processes generating excessive I/O

---
### Step 6: Identify Resource-Hungry Processes

```bash
pidstat 1
```

or

```bash
top
```

Find processes consuming excessive CPU or memory.

---
## 9. Building a Simple Performance Monitor

A basic monitoring script can be built using Bash.

Example data sources:

```bash
cat /proc/loadavg
cat /proc/meminfo
cat /proc/vmstat
```

The script can:

1. Read system metrics
2. Parse values using awk
3. Compare metrics against thresholds
4. Trigger alerts when limits are exceeded

Example alert condition:

```text
Load Average > Number of CPU Cores
```

Possible alert targets:

* Email
* Slack
* Telegram
* Discord

---
## Frequently Used Commands

```bash
uptime

free -h

vmstat 1

iostat -xz 1

sudo iotop

pidstat 1

top

htop
```
