# Text Manipulation

## 1. What is Text Manipulation?

Text Manipulation is the practice of searching, filtering, extracting, counting, transforming, and modifying text data using command-line tools.

It is one of the most important Linux skills because almost everything in Linux is represented as text:

* Log files
* Configuration files
* Command output
* Process information
* Network statistics

---
## 2. Why is it Important?

Text Manipulation allows engineers to process large amounts of data quickly and efficiently.

Common use cases:

* Analyzing application logs
* Extracting specific information from files
* Searching for errors
* Generating reports
* Automating system administration tasks

Without text processing tools, engineers would need to manually inspect thousands or millions of lines of data.

---
## 3. How Does It Work Internally?

Most text processing tools rely on Linux Standard I/O.

### Standard Input (STDIN)

Input data received from:

* Keyboard
* Files
* Another command

---
### Standard Output (STDOUT)

Output displayed on:

* Terminal
* File
* Another command

---
### Data Flow

```text
Input
 ↓
Process Text
 ↓
Output
```

Most tools read input line-by-line, process it, and send the result to STDOUT.

---
## 4. Core Components

### grep

Searches for matching text patterns.

```bash
grep "error" application.log
```

Common options:

```bash
grep -i "error" file
grep -r "keyword" directory
grep -n "text" file
```

Useful for:

* Log analysis
* Error detection
* Pattern matching

---
### awk

Text extraction and processing tool.

Example:

```bash
ls -l | awk '{print $5}'
```

Prints:

```text
File size column
```

Useful for:

* Extracting columns
* Data transformation
* Report generation

---
### sed

Stream editor for modifying text.

Replace text:

```bash
sed 's/old/new/'
```

Delete lines:

```bash
sed '3,6d' file.txt
```

Useful for:

* Search and replace
* Configuration management
* Batch editing

---
### cut

Extracts specific fields.

Example:

```bash
cut -d ':' -f1 /etc/passwd
```

Prints usernames.

---
### wc

Counts data.

```bash
wc -l file.txt
```

Common options:

* `-l` → lines
* `-w` → words
* `-c` → characters

---
### head

Displays the first lines of a file.

```bash
head file.txt
```

Example:

```bash
head -n 10 file.txt
```

---
### tail

Displays the last lines of a file.

```bash
tail file.txt
```

Real-time log monitoring:

```bash
tail -f application.log
```

---
### cat

Displays file content.

```bash
cat file.txt
```

Useful for:

* Quick file viewing
* Combining files
* Redirecting output

---
## 5. Dependencies and Related Concepts

### Pipelines

Pipelines connect commands together.

```bash
command1 | command2
```

Output of the first command becomes input for the second.

Example:

```bash
ps -ef | grep nginx
```

---
### Redirection

Redirect output or input.

Overwrite file:

```bash
echo "text" > file.txt
```

Append to file:

```bash
echo "text" >> file.txt
```

Read input from file:

```bash
command < file.txt
```

---
### Regular Expressions (Regex)

Pattern matching language used by many tools.

Examples:

```text
^
$
.*
[0-9]
[a-z]
```

Useful for:

* Searching logs
* Validating data
* Advanced filtering

---
## 6. Common Misconceptions

### awk Is Just a Command

Incorrect.

Awk is actually a complete programming language designed for text processing.

It supports:

* Variables
* Loops
* Conditions
* Functions

---
### sed Is Just Search-and-Replace

Incorrect.

Sed is a stream editor capable of:

* Replacing text
* Deleting lines
* Inserting text
* Transforming streams

---
## 7. Common Production Issues

### Accidental File Overwrite

Dangerous mistake:

```bash
echo "config" > config.txt
```

This replaces the entire file.

Safer option:

```bash
echo "config" >> config.txt
```

which appends content.

---
### Incorrect Regex

A poorly written regex may:

* Match too much
* Match too little
* Corrupt data during replacement

Always test before modifying production files.

---
### Processing Huge Files Inefficiently

Commands such as:

```bash
cat huge.log | grep error
```

are less efficient than:

```bash
grep error huge.log
```

---
## 8. Troubleshooting Runbook

### Example

Count running nginx processes.

---
### Step 1: Verify Initial Output

```bash
ps -ef
```

Check that data exists.

---
### Step 2: Apply Filter

```bash
ps -ef | grep nginx
```

Verify filtering works correctly.

---
### Step 3: Count Results

```bash
ps -ef | grep nginx | wc -l
```

Count matching entries.

---
### Rule

Always debug pipelines one stage at a time.

Avoid building long pipelines before verifying intermediate results.

---
## 9. Build It Yourself

A simple version of grep can be written in Python.

Example workflow:

1. Read input from STDIN
2. Split text into lines
3. Search for matching keywords
4. Print matching lines

A simple version of awk can:

1. Read input
2. Split each line into columns
3. Print selected fields

A simple version of sed can:

1. Read text
2. Apply string replacement
3. Output modified content

---
## Frequently Used Commands

```bash
grep "error" file.log

grep -i "warning" file.log

awk '{print $1}'

cut -d ':' -f1 /etc/passwd

sed 's/old/new/'

head -n 10 file.log

tail -f application.log

wc -l file.log

cat file.txt

ps -ef | grep nginx

netstat -tulpn | grep 80
```

---
## Production Examples

Find failed SSH logins:

```bash
grep "Failed password" /var/log/auth.log
```

Find top IP addresses in Nginx logs:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr
```

Count HTTP 500 errors:

```bash
grep " 500 " access.log | wc -l
```

Monitor logs in real time:

```bash
tail -f application.log
```
